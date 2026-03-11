from ddgs import DDGS

def duckduckgo_search(query, max_results=5):
    results = []
    try:
        with DDGS() as ddgs:
            # Az új ddgs.text metódust használjuk
            search_results = ddgs.text(query, max_results=max_results)
            for r in search_results:
                results.append({
                    "title": r.get('title', ''),
                    "url": r.get('href', ''),
                    "snippet": r.get('body', '')
                })
    except Exception as e:
        print(f"Keresési hiba: {e}")
    return results