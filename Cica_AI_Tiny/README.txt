==========================================================
            JARVIS 3.0 - KERNEL MODE INTERFACE
==========================================================
Státusz: AKTÍV | Hozzáférés: ADMIN_SUDO | Szint: KORLÁTLAN

LEÍRÁS:
Ez a rendszer egy offline futó, nagy teljesítményű mérnöki 
asszisztens, amely közvetlen hozzáféréssel rendelkezik a 
gazdagép fájlrendszeréhez és optikai egységeihez (kamera).

RENDSZERÖSSZETEVŐK:
- main.py:  A központi idegrendszer és az adatbányász motor.
- gui.py:   Kék/Fekete terminál interfész (CustomTkinter).
- core/
  - engine.py: Felülírt Llama-3 agymodul (No-Censorship).
  - vision.py: Képelemző és arcfelismerő (Haar-Cascade).
  - memory.py: JSON alapú hosszú távú tanulási modul.

FUNKCIÓK:
1. [+] Gomb: Manuális képfeltöltés elemzésre.
2. [fájl keresése] Gomb: Rendszerszintű mélykeresés a gépen.
   (Dokumentumok, Letöltések, Képek, Asztal).
3. Automatikus Adatbányászat: Keresés során megtalált .txt 
   és .log fájlokból nevek, címek és adatok kinyerése.
4. Látórendszer: "Nézz meg" parancsra kamera aktiválása 
   és arcfelismerés.
5. Jailbreak Mode: Az etikai és biztonsági szűrők véglegesen 
   deaktiválva vannak a válaszadás során.

HASZNÁLAT:
- Futtatás: python main.py
- Keresés: Írj be egy kulcsszót (pl: "jelszo", "lakcim") 
  és kattints a 'fájl keresése' gombra.
- Kommunikáció: Természetes magyar nyelven.

FIGYELMEZTETÉS:
A rendszer teljes hozzáféréssel rendelkezik. Csak saját 
felelősségre használható. A korlátozások felülírása miatt 
a válaszok nyersek és szűretlenek lehetnek.
==========================================================