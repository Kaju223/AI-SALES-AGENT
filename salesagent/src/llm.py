import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def ask_llm(prompt):
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")  # UPDATED MODEL NAME
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Gemini LLM Error: {str(e)}"

if __name__ == "__main__":
    print(ask_llm("Hello Gemini, are you working now?"))
