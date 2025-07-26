# 🎲 DBD Random Killer + Perk Picker

A simple Python console app that randomly selects a **Killer** and a **Killer Perk** from *Dead by Daylight*. Each selection is unique per session — once a killer or perk is drawn, it won’t be used again until you reset the app.

---

## 📦 Requirements

This app requires:

- **Python 3.6 or higher**\
  You can [download Python here](https://www.python.org/downloads/)

---

## 📁 Files Included

Your project folder (`dbdapp/`) should look like this:

```
dbdapp/
├── dbd_picker.py      ← main app script
├── data.json          ← master list of all killers and perks
└── state.json         ← current session’s remaining killers/perks
```

---

## 💪 Setup

1. **Clone this repo** or download the folder.
2. Ensure you have Python installed. Run this in your terminal to check:
   ```bash
   python --version
   ```
3. Navigate to the folder where you saved the project:
   ```bash
   cd (where you put the folder with the files inside)
   ```

---

## ▶️ How to Run

Use your terminal or command prompt:

```bash
python dbd_picker.py
```

You’ll see a menu like this:

```
=== DBD Random Killer + Perk Picker ===
1. Draw
2. Reset
3. Exit
```

### ✨ Features:

- **Option 1**: Draws a random killer + perk (removes them from the pool).
- **Option 2**: Resets the list to full (`data.json` → `state.json`).
- **Option 3**: Exits the app.
- 💡 Shows how many killers remain.
- 🧼 Clears the screen between actions for clean visuals.

---

## 🔁 How It Works

- `data.json`: permanent full list of killers/perks.
- `state.json`: tracks what's left during your current session.
- When you reset, `state.json` is restored from `data.json`.

## 🔹 Made for DBD fans, by DBD fans.

