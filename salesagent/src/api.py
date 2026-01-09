import requests

def get_recent_orders():
    url = "https://sandbox.mkonnekt.net/ch-portal/api/v1/orders/recent"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, timeout=50)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    print(get_recent_orders())
