import sys
import os
import streamlit as st

# -----------------------------
# Fix for ModuleNotFoundError
# -----------------------------
# Add project root to sys.path so 'src' can be imported
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.append(project_root)

# -----------------------------
# Imports from your src package
# -----------------------------
from src.api import get_recent_orders
from src.llm import ask_llm
from src.utils import parse_date

# -----------------------------
# Streamlit UI
# -----------------------------

# Title of the webpage
st.title("🛒 Sales Insight Agent (Gemini AI)")

# Text box to ask question
question = st.text_input("Ask a question about sales:")

# Button click to analyze
if st.button("Analyze"):

    # Get sales data (offline JSON or API)
    data = get_recent_orders()

    # Check for errors
    if "error" in data:
        st.error("Error loading data: " + data["error"])
    else:
        # Parse date from user question
        date = parse_date(question)

        # Prepare prompt for Gemini AI
        prompt = (
            f"Sales Data: {data}\n"
            f"User Question: {question}\n"
            f"Date Parsed: {date}\n"
            "Give a detailed answer in bullet points."
        )

        # Get AI-generated answer
        answer = ask_llm(prompt)

        # Display AI answer
        st.subheader("📊 AI Answer:")
        st.write(answer)
