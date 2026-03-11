# core/security.py
import hashlib
import requests
import os

class JarvisSecurity:
    def __init__(self, target_password="110608231002"):
        self.password_hash = hashlib.sha256(target_password.encode()).hexdigest()
        self.locked = True
        # REGISZTRÁLJ A VIRUSTOTAL.COM-ON ÉS KÉRJ EGY INGYENES KULCSOT:
        self.vt_api_key = "7cfe59f5dcd133ffd0aadb1b97e1822fa4453648f05a8cc08089718703169619"

    def verify_password(self, input_password):
        check_hash = hashlib.sha256(input_password.encode()).hexdigest()
        if check_hash == self.password_hash:
            self.locked = False
            return True
        return False

    def get_file_hash(self, file_path):
        """Kiszámolja a fájl ujjlenyomatát (SHA-256)."""
        sha256_hash = hashlib.sha256()
        try:
            with open(file_path, "rb") as f:
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)
            return sha256_hash.hexdigest()
        except Exception as e:
            return None

    def scan_file(self, file_path):
        """Valódi vírusellenőrzés tartalom alapján."""
        if not self.vt_api_key or len(self.vt_api_key) < 10:
            return "[-] HIBA: Hiányzó VirusTotal API kulcs!"

        file_hash = self.get_file_hash(file_path)
        if not file_hash:
            return "[-] HIBA: A fájl nem olvasható."

        url = f"https://www.virustotal.com/api/v3/files/{file_hash}"
        headers = {"x-apikey": self.vt_api_key}

        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                stats = data['data']['attributes']['last_analysis_stats']
                mal = stats['malicious']
                
                if mal > 0:
                    return f"[!!!] VESZÉLY: {mal} motor kártékonynak találta!"
                return "[+] TISZTA: A fájl a globális adatbázis szerint biztonságos."
            
            elif response.status_code == 404:
                return "[?] ISMERETLEN: Ez a fájl még nem lett elemezve a VirusTotalon."
            elif response.status_code == 429:
                return "[-] LIMIT: Túl sok kérés. Várj egy percet (Ingyenes API limit)."
            else:
                return f"[-] API HIBA: {response.status_code}"
        except Exception as e:
            return f"[-] Kapcsolódási hiba: {str(e)}"

    def lock_system(self):
        self.locked = True
        return "[!] RENDSZER ZÁROLVA."