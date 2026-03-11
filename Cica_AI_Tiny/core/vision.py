# core/vision.py
import os
import cv2

class JarvisVision:
    def __init__(self):
        # Betöltjük az alapértelmezett arc-adatbázist
        cascade_path = "core/haarcascade_frontalface_default.xml"
        if os.path.exists(cascade_path):
            self.face_cascade = cv2.CascadeClassifier(cascade_path)
            self.vision_active = True
        else:
            print(f"[-] HIBA: {cascade_path} nem található!")
            self.vision_active = False

    def analyze_image(self, file_path):
        if not self.vision_active: return "Látórendszer offline."
        
        img = cv2.imread(file_path)
        if img is None: return "Fájl nem olvasható."
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)
        
        if len(faces) > 0:
            return f"A képen {len(faces)} arcot azonosítottam."
        return "Nem látok senkit a képen."

    def get_camera_frame(self):
        if not self.vision_active: return "Kamera hiba."
        
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()
        
        if not ret: return "Nincs kamera jel."
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)
        
        if not os.path.exists("downloads"): os.makedirs("downloads")
        cv2.imwrite("downloads/last_seen.jpg", frame)
        
        if len(faces) > 0:
            return f"Látom önt, uram. {len(faces)} arc van előttem."
        return "A kamera aktív, de üres a kép."