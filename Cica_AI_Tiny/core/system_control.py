import subprocess
import os
import shutil

class SystemController:
    def __init__(self):
        pass

    def execute_shell(self, command):
        """Tetszőleges rendszerparancs futtatása"""
        try:
            result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True, encoding='latin-1')
            return result.stdout if result.returncode == 0 else result.stderr
        except Exception as e:
            return f"Hiba a végrehajtás során: {str(e)}"

    def download_file(self, url, destination):
        """Fájl letöltése API nélkül, rendszerszinten"""
        cmd = f"Invoke-WebRequest -Uri '{url}' -OutFile '{destination}'"
        return self.execute_shell(cmd)

    def delete_path(self, path):
        """Fájl vagy mappa végleges törlése"""
        if os.path.exists(path):
            if os.path.isfile(path):
                os.remove(path)
            else:
                shutil.rmtree(path)
            return True
        return False