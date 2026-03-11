import requests
from bs4 import BeautifulSoup

class DuckSearch:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    def search(self, query):
        # HTML verziót használunk, mert nem kell hozzá API kulcs
        url = f"https://html.duckduckgo.com/html/?q={query}"
        try:
            response = requests.get(url, headers=self.headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            results = []
            for link in soup.find_all('a', class_='result__a', limit=5):
                results.append({'title': link.text, 'url': link.get('href')})
            return results
        except Exception as e:
            return []