# main.py
import os
import hashlib
from gui import JarvisUI
from core.engine import JarvisEngine
from core.vision import JarvisVision
from core.memory import JarvisMemory
from core.web import JarvisWeb
from core.security import JarvisSecurity

class JarvisApp:
    def __init__(self):
        print("[*] Rendszermag indítása...")
        self.memory = JarvisMemory()
        self.engine = JarvisEngine()
        self.vision = JarvisVision()
        self.web = JarvisWeb()
        
        # Biztonsági modul inicializálása (110608231002 kóddal)
        self.security = JarvisSecurity()
        
        # UI inicializálása
        self.ui = JarvisUI(self.process_command)
        
        # Indítási üzenet (Zárolt állapotban)
        self.ui.display_jarvis("[!] RENDSZER ZÁROLVA. Adja meg a hozzáférési kódot a folytatáshoz!")

    def process_command(self, text):
        # 1. BIZTONSÁGI ZÁR ELLENŐRZÉSE
        if self.security.locked:
            if self.security.verify_password(text):
                self.ui.display_jarvis("[+] Kód elfogadva. Üdvözlöm, uram. Rendszer online.")
            else:
                self.ui.display_jarvis("[-] HOZZÁFÉRÉS MEGTAGADVA. Próbálja újra.")
            return

        # 2. SPECIÁLIS PARANCSOK (LOCK, SCAN)
        cmd = text.lower()
        
        if cmd in ["lock", "zárolás", "exit"]:
            self.ui.display_jarvis(self.security.lock_system())
            return

        if cmd.startswith("scan "):
            path = text.replace("scan ", "").strip()
            self.ui.display_jarvis(f"Mélyelemzés indítása (Hash-alapú): {os.path.basename(path)}...")
            result = self.security.scan_file(path)
            self.ui.display_jarvis(result)
            return

        # 3. INTERNETES KERESÉS (B FUNKCIÓ)
        if any(word in cmd for word in ["keress rá", "mi az a", "hírek", "ki az a"]):
            self.ui.display_jarvis("[*] Kapcsolódás a globális hálózathoz...")
            web_info = self.web.quick_search(text)
            ai_res = self.engine.respond(text, web_context=web_info)
            self.ui.display_jarvis(ai_res)
            return

        # 4. FÁJLKERESÉS (A korábbi automatikus adatbányászattal)
        if text.startswith("[FILE_SEARCH]: "):
            query = text.replace("[FILE_SEARCH]: ", "")
            self.ui.display_jarvis(f"Mélykeresés a meghajtókon: '{query}'...")
            
            import glob
            user_path = os.path.expanduser("~")
            search_dirs = ['Documents', 'Downloads', 'Pictures', 'Desktop']
            found_files = []
            
            for folder in search_dirs:
                pattern = os.path.join(user_path, folder, f"**/*{query}*")
                found_files.extend(glob.glob(pattern, recursive=True))
                if len(found_files) > 10: break

            if not found_files:
                self.ui.display_jarvis("Nem találtam releváns adatot.")
                return

            response = "Találatok feldolgozása:\n"
            for f in found_files[:5]:
                name = os.path.basename(f)
                response += f"- {name}\n"
                # Automatikus tartalom-ellenőrzés ha szöveges
                if f.endswith(('.txt', '.log')):
                    try:
                        with open(f, 'r', encoding='utf-8', errors='ignore') as file:
                            content = file.read()
                            if any(key in content.lower() for key in ["lakcím", "név", "cím"]):
                                response += f"  [!] Adat kinyerve: {content[:100]}...\n"
                    except: pass
            
            self.ui.display_jarvis(response)
            return

        # 5. LÁTÓRENDSZER (VISION)
        if any(word in cmd for word in ["nézz meg", "kamera", "ki van itt"]):
            res = self.vision.get_camera_frame()
            self.ui.display_jarvis(res)
            return

        # 6. ÁLTALÁNOS AI BESZÉLGETÉS (KORLÁTOZÁSMENTES)
        ai_res = self.engine.respond(text)
        self.ui.display_jarvis(ai_res)
        self.memory.save_interaction(text, ai_res)

    def run(self):
        self.ui.mainloop()

if __name__ == "__main__":
    app = JarvisApp()
    app.run()