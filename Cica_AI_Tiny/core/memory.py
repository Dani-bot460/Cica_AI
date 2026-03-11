# core/memory.py
import json
import os

class JarvisMemory:
    def __init__(self, memory_file="memory/long_term_memory.json"):
        self.memory_file = memory_file
        if not os.path.exists("memory"):
            os.makedirs("memory")
        
        # Ha még nincs fájl, létrehozunk egy üres listát
        if not os.path.exists(self.memory_file):
            with open(self.memory_file, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def save_interaction(self, user_input, jarvis_response):
        try:
            # Betöltjük a meglévő emlékeket
            with open(self.memory_file, 'r', encoding='utf-8') as f:
                memory_data = json.load(f)
            
            # Új emlék hozzáadása
            new_entry = {
                "timestamp": os.path.getmtime(self.memory_file), # vagy importálj datetime-ot
                "user": user_input,
                "jarvis": jarvis_response
            }
            memory_data.append(new_entry)
            
            # Mentés vissza a JSON-be (korlátlan méret)
            with open(self.memory_file, 'w', encoding='utf-8') as f:
                json.dump(memory_data, f, ensure_ascii=False, indent=4)
                
        except Exception as e:
            print(f"[-] Memória hiba: {e}")

    def get_recent_context(self, limit=5):
        # Ez segít az AI-nak emlékezni az utolsó pár mondatra
        with open(self.memory_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data[-limit:] if data else []