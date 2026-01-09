Sales Insight Agent – AI-Powered Sales Analytics

This project is an AI-based Sales Insight System that uses
Google Gemini AI + Python to analyze sales data and answer natural-language questions like:

1.“What were yesterday’s sales?”
2.“Which item sold the most today?”
3.“Show me revenue summary.”

Project supports:
✔ CLI (Command Line Interface)
✔ Streamlit Web App
✔ Gemini AI LLM Integration
✔ Online API key authentication


🛠 Development Environment  
This project was fully developed in the PyCharm IDE.  
PyCharm was used for:
- Creating the Python virtual environment  
- Managing project folders and files  
- Installing libraries via built-in terminal  
- Running the CLI and Streamlit applications  
- Writing and debugging the entire code  


📌 1. Why I Used an API Key?

Google Gemini AI works only when you authenticate yourself using an API key.
This API key tells Google servers:

“This user is verified. Allow access to AI model.”

📌 2. How I Generated Gemini AI API Key (Full Steps)
✔ Step 1: Gemini console open kiya

https://aistudio.google.com

✔ Step 2: Top right me Get API Key click kiya
✔ Step 3: Create API key for free select kiya
✔ Step 4: Project banaya / assign kiya
✔ Step 5: API key generate hui (Example format)
EXAMPLE OF API KEY:----AIzaSyAxxxxxxxxxxxxxxxxxxxx
✔ Step 6: API key ko .env file me store kiya


📌 3. Which Libraries I Installed?
Terminal me run kiya:
pip install google-generativeai
pip install python-dotenv
pip install requests
pip install streamlit


Libraries use:
google-generativeai → Gemini AI se connect
python-dotenv → .env file se API key load
requests → API calls
streamlit → Web UI


📌 4. Project Folder Structure (What files I created)
salesagentproject/
│
├── .env                       → GEMINI_API_KEY stored here
├── requirements.txt           → All library names
├── test_env.py                → API key load test

│
├── src/
│   ├── __init__.py            → Makes src a package
│   ├── api.py                 → Data loader
│   ├── llm.py                 → Gemini AI integration
│   ├── utils.py               → Date understanding (yesterday, last week)
│   ├── main.py                → CLI interface
│   ├── webpage.py             → Streamlit Web interface


📌 5. What Each File Does (Line-by-Line Purpose):-
🔐 .env
GEMINI_API_KEY=your_api_key_here


🧪 test_env.py
“It checks whether the API key has loaded correctly or not.”



│📁 src/__init__.py
“It tells Python that ‘src’ is a package. (This allows imports to work properly.)”

🔍 src/api.py
“It loads the sales data.”



🤖 src/llm.py
“It connects to the Google Gemini AI model ‘gemini-2.5-flash’.”
Important logic:
The API key gets loaded
The prompt is sent to the AI
The AI returns the text response



📅 src/utils.py
“It detects the dates mentioned in the user’s question, such as:
yesterday
today
last week”


💻 src/main.py
“CLI version — it takes the user’s question through the terminal.”
Flow:
1️⃣ User input
2️⃣ Sales data read
3️⃣ Date parse
4️⃣ AI se analysis
5️⃣ Answer print



🌐 src/webpage.py
“Streamlit Web UI — it opens in the browser.
Features:
Text input box
Analyze button
The AI’s answer is displayed on the web page.”




📌 6. How to Run the Project
✔ Step 1 — Install libraries

✔ Step 2 — Test API key
✔ Step 3 — Run CLI App
✔ Step 4 — Run Web App (Streamlit)
[To run the Streamlit Web UI, open the terminal in PyCharm and execute:

streamlit run src/webpage.py

This command starts the Streamlit server, and the web application automatically opens in the browser at:
http://localhost:8501]





📌 8. Why This Project is Useful?

✔ Human-like AI answers
✔ Owners ko instant business insights
✔ No manual calculation
✔ Works with natural language
✔ Easy to expand into full dashboard





