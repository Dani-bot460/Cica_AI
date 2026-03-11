from datetime import datetime

def needs_refresh(date_str, days=30):
    last = datetime.strptime(date_str, "%Y-%m-%d")
    # Ez a sor legyen beljebb!
    return (datetime.now() - last).days > days