import json
import random
import os
import platform

DATA_FILE = "data.json"
STATE_FILE = "state.json"

def clear_console():
    # Works on Windows, macOS, Linux
    os.system("cls" if platform.system() == "Windows" else "clear")

def load_json(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def reset_state():
    print("🔁 Resetting state from data.json...")
    data = load_json(DATA_FILE)
    save_json(STATE_FILE, data)

def draw_random():
    if not os.path.exists(STATE_FILE):
        print("📁 No state file found. Creating a fresh one.")
        reset_state()

    state = load_json(STATE_FILE)

    if not state["killers"]:
        print("❌ No killers left. Resetting.")
        reset_state()
        state = load_json(STATE_FILE)

    if not state["perks"]:
        print("❌ No perks left. Resetting.")
        reset_state()
        state = load_json(STATE_FILE)

    killer = random.choice(state["killers"])
    perk = random.choice(state["perks"])

    print(f"🎯 Your Random Killer: {killer}")
    print(f"🧩 Your Random Perk: {perk}")
    print(f"📊 Killers remaining after this draw: {len(state['killers']) - 1}")

    # Remove them from state
    state["killers"].remove(killer)
    state["perks"].remove(perk)
    save_json(STATE_FILE, state)

if __name__ == "__main__":
    while True:
        clear_console()
        print("=== DBD Random Killer + Perk Picker ===")
        print("1. Draw")
        print("2. Reset")
        print("3. Exit")

        try:
            state = load_json(STATE_FILE)
            killer_count = len(state.get("killers", []))
        except Exception:
            killer_count = 0

        print(f"\n📌 Killers remaining: {killer_count}")
        choice = input("\nChoose an option (1/2/3): ").strip()

        clear_console()

        if choice == "1":
            draw_random()
        elif choice == "2":
            reset_state()
            print("✅ State reset.")
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid option. Try again.")

        input("\nPress Enter to continue...")
