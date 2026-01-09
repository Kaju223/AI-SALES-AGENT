from src.api import get_recent_orders
from src.llm import ask_llm
from src.utils import parse_date

def handle_question(question):
    data = get_recent_orders()
    if "error" in data:
        return f"API Error: {data['error']}"

    date_parsed = parse_date(question)
    prompt = f"""
Sales Data: {data}
User question: {question}
Date parsed: {date_parsed}
Answer in clear bullet points.
"""
    return ask_llm(prompt)

if __name__ == "__main__":
    print("Sales Agent CLI Ready! Type 'exit' to quit\n")
    while True:
        query = input("Ask a sales question: ")
        if query.lower() == "exit":
            break
        print("\n🔍 Answer:", handle_question(query))
        print("-" * 50)
