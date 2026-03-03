import pyautogui
import time
import json
import threading
import tkinter as tk
from tkinter import filedialog, messagebox
from pynput import mouse, keyboard

actions = []
recording = False
current_modifiers = set()

# ------------------ RECORDING ------------------ #

def on_click(x, y, button, pressed):
    global actions, recording
    if recording and pressed:
        actions.append({
            "type": "click",
            "x": x,
            "y": y,
            "delay": 0.3
        })

def on_press(key):
    global actions, recording, current_modifiers

    if not recording:
        return

    # Modifier Keys Track
    if key in [keyboard.Key.ctrl_l, keyboard.Key.ctrl_r]:
        current_modifiers.add("ctrl")
        return
    if key in [keyboard.Key.shift]:
        current_modifiers.add("shift")
        return
    if key in [keyboard.Key.alt_l, keyboard.Key.alt_r]:
        current_modifiers.add("alt")
        return

    try:
        key_char = key.char
        if current_modifiers:
            actions.append({
                "type": "hotkey",
                "keys": list(current_modifiers) + [key_char],
                "delay": 0.2
            })
        else:
            actions.append({
                "type": "key",
                "key": key_char,
                "delay": 0.1
            })
    except:
        actions.append({
            "type": "special",
            "key": str(key).replace("Key.", ""),
            "delay": 0.2
        })

def on_release(key):
    global current_modifiers
    if key in [keyboard.Key.ctrl_l, keyboard.Key.ctrl_r]:
        current_modifiers.discard("ctrl")
    if key in [keyboard.Key.shift]:
        current_modifiers.discard("shift")
    if key in [keyboard.Key.alt_l, keyboard.Key.alt_r]:
        current_modifiers.discard("alt")

mouse_listener = mouse.Listener(on_click=on_click)
keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)

mouse_listener.start()
keyboard_listener.start()

# ------------------ EXECUTION ------------------ #

def execute(loop_count):
    time.sleep(5)  # Safety delay
    for _ in range(loop_count):
        for action in actions:

            if action["type"] == "click":
                pyautogui.click(action["x"], action["y"])

            elif action["type"] == "key":
                pyautogui.write(action["key"])

            elif action["type"] == "special":
                pyautogui.press(action["key"])

            elif action["type"] == "hotkey":
                pyautogui.hotkey(*action["keys"])

            time.sleep(action["delay"])

# ------------------ BUTTON FUNCTIONS ------------------ #

def start_recording():
    global recording, actions
    actions = []
    recording = True
    status_label.config(text="Recording Started...", fg="green")

def stop_recording():
    global recording
    recording = False
    status_label.config(text="Recording Stopped", fg="red")

def run_macro():
    if not actions:
        messagebox.showerror("Error", "No actions recorded!")
        return

    try:
        loops = int(loop_entry.get())
    except:
        messagebox.showerror("Error", "Enter valid loop number")
        return

    thread = threading.Thread(target=execute, args=(loops,))
    thread.start()

def save_macro():
    file = filedialog.asksaveasfilename(defaultextension=".json")
    if file:
        with open(file, "w") as f:
            json.dump(actions, f, indent=4)
        messagebox.showinfo("Saved", "Macro Saved Successfully")

def load_macro():
    global actions
    file = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    if file:
        with open(file, "r") as f:
            actions = json.load(f)
        messagebox.showinfo("Loaded", "Macro Loaded Successfully")

def emergency_stop():
    messagebox.showwarning("Stopped", "Emergency Stop Activated!")
    exit()

# ------------------ GUI ------------------ #

root = tk.Tk()
root.title("Auto Macro Pro v2")
root.geometry("400x370")
root.resizable(False, False)

title = tk.Label(root, text="Auto Macro Pro v2", font=("Arial", 18, "bold"))
title.pack(pady=10)

status_label = tk.Label(root, text="Idle", font=("Arial", 12))
status_label.pack(pady=5)

tk.Button(root, text="Start Recording", width=20, command=start_recording).pack(pady=5)
tk.Button(root, text="Stop Recording", width=20, command=stop_recording).pack(pady=5)

tk.Label(root, text="Loop Count:").pack(pady=5)
loop_entry = tk.Entry(root)
loop_entry.pack(pady=5)
loop_entry.insert(0, "1")

tk.Button(root, text="Run Macro", width=20, command=run_macro).pack(pady=5)
tk.Button(root, text="Save Macro", width=20, command=save_macro).pack(pady=5)
tk.Button(root, text="Load Macro", width=20, command=load_macro).pack(pady=5)

tk.Button(root, text="Emergency Stop", width=20, command=emergency_stop, fg="white", bg="red").pack(pady=10)

root.mainloop()
