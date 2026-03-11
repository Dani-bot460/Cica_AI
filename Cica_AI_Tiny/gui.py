# gui.py
import customtkinter as ctk
from tkinter import filedialog
import os

class JarvisUI(ctk.CTk):
    def __init__(self, send_callback):
        super().__init__()

        # Ablak beállításai
        self.title("Cica AI 3.0 - Interface")
        self.geometry("900x600")
        self.configure(fg_color="black")

        self.send_callback = send_callback

        # --- Chat ablak ---
        self.chat_display = ctk.CTkTextbox(self, fg_color="#050505", text_color="#00BFFF", 
                                           font=("Consolas", 14), border_color="#004578", border_width=1)
        self.chat_display.pack(padx=20, pady=20, fill="both", expand=True)
        self.chat_display.insert("end", "Cica AI > Rendszer online. Teljes hozzáférés biztosítva.\n")

        # --- Alsó vezérlősáv ---
        self.input_frame = ctk.CTkFrame(self, fg_color="black")
        self.input_frame.pack(fill="x", side="bottom", padx=20, pady=10)

        # + Gomb (Képfeltöltés)
        self.add_button = ctk.CTkButton(self.input_frame, text="+", width=40, height=40,
                                        fg_color="#004578", hover_color="#00BFFF",
                                        command=self.upload_image)
        self.add_button.pack(side="left", padx=5)

        # Fájl keresése Gomb
        self.search_button = ctk.CTkButton(self.input_frame, text="fájl keresése", width=120, height=40,
                                           fg_color="#004578", hover_color="#1E90FF",
                                           command=self.trigger_file_search)
        self.search_button.pack(side="left", padx=5)

        # Beviteli mező
        self.entry = ctk.CTkEntry(self.input_frame, placeholder_text="Adjon utasítást vagy kulcsszót a kereséshez...",
                                  fg_color="#101010", text_color="#00BFFF", border_color="#004578")
        self.entry.pack(side="left", fill="x", expand=True, padx=5)
        self.entry.bind("<Return>", self.on_send)

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Képek", "*.jpg *.png *.jpeg")])
        if file_path:
            self.chat_display.insert("end", f"\n[*] Kép manuálisan betöltve: {os.path.basename(file_path)}\n")
            self.send_callback(f"[IMAGE_UPLOAD]: {file_path}")

    def trigger_file_search(self):
        query = self.entry.get()
        if not query:
            self.chat_display.insert("end", "\nCica Ai > Uram, kérem írjon be egy kulcsszót a beviteli mezőbe a kereséshez!\n")
        else:
            self.chat_display.insert("end", f"\nFELHASZNÁLÓ > [KERESÉS INDÍTÁSA: {query}]\n")
            self.send_callback(f"[FILE_SEARCH]: {query}")
            self.entry.delete(0, "end")

    def on_send(self, event=None):
        text = self.entry.get()
        if text:
            self.chat_display.insert("end", f"\nFELHASZNÁLÓ > {text}\n")
            self.entry.delete(0, "end")
            self.send_callback(text)

    def display_jarvis(self, response):
        self.chat_display.insert("end", f"Cica AI > {response}\n")
        self.chat_display.see("end")