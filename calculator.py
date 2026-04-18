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
    elif button_text == "√":
        try:
            result = math.sqrt(float(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.insert(tk.END, " Error")
    elif button_text == "π":
        entry.insert(tk.END, str(math.pi))
    elif button_text == "^":
        entry.insert(tk.END, "**")
    else:
        entry.insert(tk.END, button_text)

def update_display():
    """Refresh button layout based on mode."""
    for widget in root.grid_slaves():
        if widget not in [entry, mode_button]:
            widget.destroy()
    
    create_buttons()

def create_buttons():
    """Create buttons based on current mode."""
    if mode == "basic":
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
    else:
        buttons = [
            'sin', 'cos', 'tan', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '√', '0', '=', '+',
            'π', '^', 'C', '.'
        ]
    
    row_val = 1
    col_val = 0
    
    for button in buttons:
        tk.Button(root, text=button, width=5, height=2, font=("Arial", 12),
                  command=lambda b=button: on_click(b)).grid(row=row_val, column=col_val, padx=5, pady=5)
        
        col_val += 1
        if col_val > 3:
            col_val = 0
            row_val += 1

# Initialize the main window
root = tk.Tk()
root.title("Python Calculator")
root.geometry("400x550")
root.resizable(False, False)

# Mode toggle button
mode_button = tk.Button(root, text="Mode: Basic", command=toggle_mode, font=("Arial", 10), bg="lightblue")
mode_button.grid(row=0, column=0, columnspan=4, padx=10, pady=5, sticky="ew")

# Create the display entry
entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=5, relief="flat", justify="right")
entry.grid(row=1, column=0, columnspan=4, padx=10, pady=20)

# Create buttons
create_buttons()

# Start the application loop
root.mainloop()