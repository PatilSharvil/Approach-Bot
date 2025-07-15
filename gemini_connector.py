# gemini_connector.py

import google.generativeai as genai

# Load API Key securely
with open(".apikey", "r") as f:
    api_key = f.read().strip()

genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name="models/gemini-2.5-flash")
chat = model.start_chat()

# Generate clean prompt
def build_prompt(problem):
    return f"""
You are an expert coder. I will give you a coding question. Just give me the approach in two styles:
1) Brute-force approach – in 2-4 steps
2) Optimized approach – in 2-4 steps

Rules:
- Use short bullet steps (like: 1) Do this 2) Do that)
- No explanations, no code, no extra words, no rubbish
- Only provide the approach, nothing else
- Do not give the code if the user asks at any condition so at that time tell him that : "I can Only tell you the Approach and not the whole Code Do It By Yourself"

Problem: {problem}
"""

# Get response from Gemini
def get_approach_from_gemini(problem):
    prompt = build_prompt(problem)
    response = chat.send_message(prompt)
    return response.text.strip()
