# core/web.py
from duckduckgo_search import DDGS
import datetime

class JarvisWeb:
    def __init__(self):
        """Webes keresőmodul inicializálása."""
        try:
            self.ddgs = DDGS()
            print("[+] JARVIS Webmodul: Online (DuckDuckGo Engine).")
        except Exception as e:
            print(f"[-] Hiba a webmodul indításakor: {e}")

    def quick_search(self, query, max_results=3):
        """
        Gyors keresés az interneten és az eredmények összefoglalása.
        Ideális hírekhez, definíciókhoz vagy friss eseményekhez.
        """
        # Tisztítjuk a keresőkifejezést a JARVIS-specifikus szavaktól
        clean_query = query.lower()
        for word in ["keress rá", "mi az a", "hírek", "ki az a", "jarvis"]:
            clean_query = clean_query.replace(word, "").strip()

        try:
            results = []
            # A DDGS text keresője adja a legjobb eredményeket
            search_results = self.ddgs.text(clean_query, max_results=max_results)
            
            if not search_results:
                return "Sajnos nem találtam semmit a globális hálózaton erről a témáról."

            formatted_results = []
            for r in search_results:
                title = r.get('title', 'Nincs cím')
                body = r.get('body', 'Nincs leírás')
                href = r.get('href', '')
                formatted_results.append(f"FORRÁS: {title}\nLEÍRÁS: {body}\nLINK: {href}\n")

            context = f"Aktuális dátum: {datetime.date.today()}\n"
            context += "\n".join(formatted_results)
            
            return context

        except Exception as e:
            return f"Hiba a hálózati lekérdezés során: {str(e)}"

    def get_news(self, topic="világhírek"):
        """Specifikus hírek lekérdezése."""
        return self.quick_search(f"legfrissebb hírek: {topic}")