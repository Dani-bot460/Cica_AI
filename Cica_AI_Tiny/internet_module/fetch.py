import requests
from bs4 import BeautifulSoup

def download_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Felesleges HTML elemek törlése
        for tag in soup(["script", "style", "noscript", "header", "footer", "nav", "aside", "button", "svg"]):
            tag.decompose()
            
        text = soup.get_text(separator="\n")
        
        # Csak a 40 karakternél hosszabb sorok maradnak (kiszűri a gombokat)
        lines = [line.strip() for line in text.splitlines() if len(line.strip()) > 40]
        
        return "\n".join(lines) if lines else "Nem található érdemi tartalom."
    except Exception as e:
        return f"Hiba: {e}"