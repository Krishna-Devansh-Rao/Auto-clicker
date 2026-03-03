🚀 Auto Macro Pro v2

A professional desktop-based Auto Clicker & Macro Automation Tool built using Python.

Auto Macro Pro allows users to record mouse clicks, keyboard inputs (including hotkeys like Ctrl+C / Ctrl+V), and replay them with custom loop counts. It is designed for repetitive task automation, testing workflows, and productivity enhancement.

✨ Features

🎯 Record mouse clicks (dynamic position capture)

⌨ Record keyboard typing

🔥 Record hotkeys (Ctrl+C, Ctrl+V, Ctrl+X, Ctrl+A, Shift combos, Alt combos)

🔁 Custom loop count execution

⏳ Adjustable delay between actions

💾 Save macro as JSON

📂 Load saved macro files

🛑 Emergency stop button

🖥 Simple and clean GUI (Tkinter based)

🔐 5-second safety delay before execution

🛠 Tech Stack

Python 3.10+

pyautogui

pynput

keyboard

tkinter

json

📦 Installation
pip install pyautogui pynput keyboard

Run the application:

python auto_macro_pro_v2.py
🧠 How It Works

Click Start Recording

Perform mouse clicks & keyboard actions

Click Stop Recording

Set loop count

Click Run Macro

Automation starts after 5 seconds

📁 Example JSON Macro File
[
    {
        "type": "click",
        "x": 450,
        "y": 300,
        "delay": 0.3
    },
    {
        "type": "hotkey",
        "keys": ["ctrl", "c"],
        "delay": 0.2
    }
]
⚠ Disclaimer

This tool is intended for:

Task automation

Workflow testing

Form filling

Personal productivity

Do not use this software for violating platform policies, cheating in games, or any illegal activities.

🚀 Future Upgrades (Planned)

Modern PyQt6 UI

Drag & Drop step editor

Clipboard content preview

Conditional automation

Image recognition click

Multi-profile system
