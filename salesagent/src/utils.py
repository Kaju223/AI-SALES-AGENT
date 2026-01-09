from datetime import datetime, timedelta

def parse_date(text):
    today = datetime.today()
    text = text.lower()

    if "yesterday" in text:
        return today - timedelta(days=1)
    if "last week" in text:
        return today - timedelta(weeks=1)
    if "today" in text:
        return today
    return None
