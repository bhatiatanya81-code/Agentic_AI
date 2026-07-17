import json
import os

MEMORY_FILE = "data/memory.json"

MAX_MESSAGES = 20     # Last 20 messages only

IGNORE = {
    "hi",
    "hello",
    "hey",
    "thanks",
    "thank you",
    "ok",
    "okay"
}

def should_save(text):
    return text.strip().lower() not in IGNORE


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []


MAX_HISTORY = 20

def save_memory(memory):
    memory = memory[-MAX_HISTORY:]

    os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)

    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(memory, file, indent=4, ensure_ascii=False)


def add_message(memory, role, content):
    memory.append({
        "role": role,
        "content": content
    })

    return memory[-MAX_MESSAGES:]