import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

# =====================
# Load Environment
# =====================
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    st.error("❌ GEMINI_API_KEY not found in .env")
    st.stop()

# =====================
# Init Gemini Client (Force v1)
# =====================
client = genai.Client(
    api_key=API_KEY,
    http_options={"api_version": "v1"}
)

MODEL = "models/gemini-2.5-flash"

# =====================
# Page Setup & Styling
# =====================
st.set_page_config(
    page_title="Personal AI Assistant",
    page_icon="🤖",
    layout="centered"
)

# Professional CSS Styling
st.markdown("""
<style>
    /* Main Background and Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    /* Apply Inter font ONLY to text elements, avoiding global inheritance */
    header, .stTitle, .stCaption, [data-testid="stMarkdownContainer"], .stChatMessage, .sidebar .sidebar-content {
        font-family: 'Inter', sans-serif !important;
    }
    
    /* 🛡️ ICON PROTECTION: Force the correct font for all Streamlit symbols */
    [data-testid="stIconMaterial"],
    [data-testid="stSidebarCollapseButton"] *,
    [data-testid="collapsedControl"] *,
    .material-icons,
    .material-symbols-outlined,
    .material-symbols-rounded,
    button[kind="header"] span,
    span[data-testid="stIconMaterial"] {
        font-family: "Material Symbols Rounded", "Material Symbols Outlined", "Material Icons" !important;
        font-feature-settings: "liga" !important; /* Ensure ligatures work */
    }
    
    .main {
        background: linear-gradient(135deg, #f8f9fc 0%, #e2e8f0 100%);
    }
    
    /* Header Styling */
    .stTitle {
        color: #1e293b;
        font-weight: 700;
        letter-spacing: -1px;
    }
    
    /* Chat Message Bubbles */
    .stChatMessage {
        border-radius: 12px;
        padding: 1rem;
        margin-bottom: 1rem;
        box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
        border: 1px solid rgba(255, 255, 255, 0.4);
    }
    
    /* User Message */
    [data-testid="stChatMessage"]:nth-child(even) {
        background-color: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
    }
    
    /* Model/Assistant Message */
    [data-testid="stChatMessage"]:nth-child(odd) {
        background-color: #ffffff;
        border-left: 4px solid #3b82f6;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e2e8f0;
    }
    
    .sidebar-header {
        font-size: 1.2rem;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 1.5rem;
    }

    /* Buttons */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.2s;
    }
    
    .stButton>button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgb(0 0 0 / 0.1);
    }
</style>
""", unsafe_allow_html=True)

# App Content
st.title("🤖 Personal AI Assistant")
st.caption("Custom designed for professional utility • Stable v1 Mode")

# =====================
# Initialize Memory
# =====================
if "messages" not in st.session_state:
    st.session_state.messages = []

# Limit history (Free tier safety)
MAX_HISTORY = 10
st.session_state.messages = st.session_state.messages[-MAX_HISTORY:]

# =====================
# Logic: Convert Messages → Gemini Format
# =====================
def build_gemini_contents(history):
    contents = []
    for msg in history:
        # Map role
        role = "model" if msg["role"] == "assistant" else "user"
        contents.append({
            "role": role,
            "parts": [{"text": msg["content"]}]
        })
    return contents

# =====================
# Show Chat History
# =====================
for msg in st.session_state.messages:
    avatar = "👤" if msg["role"] == "user" else "🤖"
    with st.chat_message(msg["role"], avatar=avatar):
        st.write(msg["content"])

# =====================
# User Input
# =====================
if prompt := st.chat_input("Ask me anything..."):

    # Display & Save user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.write(prompt)

    try:
        with st.spinner("Generating response..."):
            # Prepare contents
            contents = build_gemini_contents(st.session_state.messages)

            # Call Gemini
            response = client.models.generate_content(
                model=MODEL,
                contents=contents
            )
            reply = response.text

    except Exception as e:
        reply = f"❌ Error: {e}"

    # Display & Save AI reply
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant", avatar="🤖"):
        st.write(reply)

# =====================
# Sidebar
# =====================
with st.sidebar:
    st.markdown('<p class="sidebar-header">⚙️ Workspace Settings</p>', unsafe_allow_html=True)
    
    st.info(f"**Model**: {MODEL.replace('models/', '')}")
    
    st.divider()
    
    if st.button("🗑 Clear Conversation"):
        st.session_state.messages = []
        st.rerun()
    
    st.divider()
    st.caption("Personal AI v1.2.0")