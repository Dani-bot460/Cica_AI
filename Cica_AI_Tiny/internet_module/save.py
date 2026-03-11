import os
import re
from datetime import datetime

def save_search(query, results, texts):
    # Windows által tiltott karakterek eltávolítása a fájlnévből
    # < > : " / \ | ? *
    clean_query = re.sub(r'[<>:"/\\|?*]', '', query).replace(' ', '_')[:50]
    
    timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    folder_name = f"{clean_query}_{timestamp}"
    base = f"internet/searches/{folder_name}"
    
    try:
        os.makedirs(base + "/pages", exist_ok=True)
        
        # Elmentjük a nyers szövegeket is, hogy meglegyen
        with open(f"{base}/content.txt", "w", encoding="utf-8") as f:
            f.write("\n\n--- NEXT PAGE ---\n\n".join(texts))
            
        return base
    except Exception as e:
        print(f"Mentési hiba: {e}")
        return None