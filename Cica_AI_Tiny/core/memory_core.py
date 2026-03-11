import json
import os

DB_PATH = "memory/knowledge.json"

def load_knowledge():
    if not os.path.exists(DB_PATH):
        return {}
    with open(DB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_knowledge(db):
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2)
