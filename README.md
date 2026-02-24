# 🤖 Personal AI Assistant

A simple, beginner-friendly AI chatbot built with Python, Streamlit, and the Google Gemini API.

## 🚀 Features
- **Chat Interface**: Clean and intuitive messaging UI.
- **Conversation Memory**: Remembers past messages in the current session.
- **Secured**: API key is loaded from environment variables (no hardcoding!).
- **Fast**: Powered by `gemini-1.5-flash` model.

---

## 🛠️ Local Setup Guide

Follow these steps to run the assistant on your own computer:

### 1. Prerequisites
- Install [Python 3.9+](https://www.python.org/downloads/)
- Get a **Free Gemini API Key** from [Google AI Studio](https://aistudio.google.com/app/apikey)

### 2. Clone/Download the Project
Go to the `assistant` folder:
```bash
cd assistant
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API Key
1. Copy the `.env.example` file and rename it to `.env`.
2. Open `.env` and replace `your_api_key_here` with your actual Google Gemini API key.

### 5. Run the App
```bash
streamlit run app.py
```
The app will open automatically in your browser (usually at `http://localhost:8501`).

---

## 🌐 How to Deploy on Streamlit Cloud (FREE)

Sharing your app with friends is easy and free with Streamlit Cloud:

1. **Push to GitHub**: Upload your `assistant` folder to a new GitHub repository.
2. **Sign in to Streamlit Cloud**: Go to [share.streamlit.io](https://share.streamlit.io/) and connect your GitHub account.
3. **Deploy**:
   - Click "Create app".
   - Select your repository and `app.py` as the main file.
4. **Important: Add API Key**:
   - In the Streamlit Cloud dashboard, go to your app **Settings** -> **Secrets**.
   - Paste the following:
     ```toml
     GEMINI_API_KEY = "your_actual_api_key_here"
     ```
   - Hit save and your app is live!

---

## 📝 Technologies Used
- [Streamlit](https://streamlit.io/)
- [Google Generative AI SDK](https://github.com/google/generative-ai-python)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
