# Approach Teller - Gemini AI 🚀

A simple desktop app that uses Google Gemini AI to suggest step-by-step approaches for coding problems. This project was built as a fun learning exercise to understand how AI APIs can be integrated into Python GUI applications.

## Features ✨
- 🖥️ Modern, clean GUI built with [CustomTkinter](https://customtkinter.tomschimansky.com/)
- 🤖 Asks Gemini AI for both brute-force and optimized approaches to coding questions
- 🚫 No code or explanations—just concise, actionable steps
- ⚠️ Error handling for API issues

## How It Works 🛠️
1. ✍️ Enter your coding question in the input box.
2. 👉 Click **Get Approach**.
3. 🤩 The app queries Gemini AI and displays two styles of solution steps: brute-force and optimized.

## Setup & Installation 🧑‍💻

### 1. Clone the repository
```
git clone <repo-url>
cd <project-folder>
```

### 2. Install dependencies
- 🐍 Python 3.7+
- [CustomTkinter](https://pypi.org/project/customtkinter/):
  ```
  pip install customtkinter
  ```
- [google-generativeai](https://pypi.org/project/google-generativeai/):
  ```
  pip install google-generativeai
  ```

### 3. Get a Gemini API Key 🔑
- Sign up for Gemini API access from Google (see [official docs](https://ai.google.dev/)).
- Save your API key in a file named `.apikey` in the project root (same folder as `main_gui.py`). The file should contain only your API key, nothing else.

### 4. Run the app ▶️
```
python main_gui.py
```

## Why This Project? 🤔
This was a simple, fun project to learn how to connect Python apps to AI APIs and build modern GUIs. It helped me understand API integration, prompt engineering, and error handling in a real-world context. The project is intentionally minimal—just enough to demonstrate the core idea and make learning enjoyable!

---
