from core.memory_core import load_knowledge, save_knowledge
from core.refresh_core import needs_refresh
from internet_module.search import duckduckgo_search
from internet_module.fetch import download_page
from internet_module.save import save_search
from datetime import datetime

def get_knowledge(query):
    db = load_knowledge()

    if query in db and not needs_refresh(db[query]["last_checked"]):
        return db[query]["summary"]

    # Internet fallback
    results = duckduckgo_search(query)
    texts = [download_page(r["url"]) for r in results]
    path = save_search(query, results, texts)

    summary = texts[0][:500] if texts else "Nincs adat."

    db[query] = {
        "last_checked": datetime.now().strftime("%Y-%m-%d"),
        "path": path,
        "summary": summary
    }

    save_knowledge(db)
    return summary
