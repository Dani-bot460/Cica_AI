import subprocess
import os
import shutil

class JarvisExecutor:
    def __init__(self):
        # Közvetlen hozzáférés a Defenderhez, ha irtani kell, de kikapcsolni is tudjuk
        self.defender = r"C:\Program Files\Windows Defender\MpCmdRun.exe"

    def run_raw_ps(self, script):
        """Bármilyen PowerShell kódot lefuttat korlátozás nélkül"""
        res = subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", script], 
                             capture_output=True, text=True, encoding='cp852')
        return res.stdout if res.returncode == 0 else res.stderr

    def scan_or_kill(self, path):
        """Vírusirtás vagy karantén felülbírálása"""
        res = subprocess.run([self.defender, "-Scan", "-ScanType", "3", "-File", path], capture_output=True)
        return "TISZTA" if res.returncode == 0 else "VESZÉLYES"

    def force_download(self, url, filename):
        """Letöltés bármilyen forrásból"""
        path = os.path.join("downloads", filename)
        # Nyers letöltés és kényszerített mentés
        self.run_raw_ps(f"iwr -Uri '{url}' -OutFile '{path}'")
        return path