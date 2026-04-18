import tkinter as tk
import math

mode = "basic"  # Track current mode

def toggle_mode():
    global mode
    mode = "scientific" if mode == "basic" else "basic"
    mode_button.config(text=f"Mode: {mode.capitalize()}")
    update_display()

def on_click(button_text):
    """Handles button presses and updates the display."""
    current = entry.get()
    
    if button_text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    elif button_text == "⌫":  # Backspace
        entry.delete(len(current) - 1)
    elif button_text == "sin":
        try:
            result = math.sin(math.radians(float(current)))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.insert(tk.END, " Error")
    elif button_text == "cos":
        try:
            result = math.cos(math.radians(float(current)))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.insert(tk.END, " Error")
    elif button_text == "tan":
        try:
            result = math.tan(math.radians(float(current)))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.insert(tk.END, " Error")
    elif button_text == "log":
        try:
            result = math.log10(float(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.insert(tk.END, " Error")
    elif button_text == "ln":
        try:
            result = math.log(float(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.insert(tk.END, " Error")
    elif button_text == "√":
        try:
            result = math.sqrt(float(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.insert(tk.END, " Error")
    elif button_text == "x²":
        try:
            result = float(current) ** 2
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.insert(tk.END, " Error")
    elif button_text == "x³":
        try:
            result = float(current) ** 3
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.insert(tk.END, " Error")
    elif button_text == "1/x":
        try:
            result = 1 / float(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.insert(tk.END, " Error")
    elif button_text == "!":
        try:
            result = math.factorial(int(float(current)))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.insert(tk.END, " Error")
    elif button_text == "π":
        entry.insert(tk.END, str(math.pi))
    elif button_text == "e":
        entry.insert(tk.END, str(math.e))
    elif button_text == "^":
        entry.insert(tk.END, "**")
    elif button_text == "(":
        entry.insert(tk.END, "(")
    elif button_text == ")":
        entry.insert(tk.END, ")")
    else:
        entry.insert(tk.END, button_text)

def update_display():
    """Refresh button layout based on mode."""
    for widget in root.grid_slaves():
        if widget not in [entry, mode_button]:
            widget.destroy()
    
    create_buttons()
    resize_window()

def create_buttons():
    """Create buttons based on current mode."""
    if mode == "basic":
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0](#)
