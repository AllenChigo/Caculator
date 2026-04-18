import tkinter as tk

def on_click(button_text):
    """Handles button presses and updates the display."""
    current = entry.get()
    
    if button_text == "=":
        try:
            # eval() calculates the string expression automatically
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# 1. Initialize the main window
root = tk.Tk()
root.title("Python Calculator")
root.geometry("300x400")
root.resizable(False, False)

# 2. Create the display entry at the top
entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=5, relief="flat", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# 3. Define the button labels and their grid positions
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0

# 4. Loop through the list to create and place buttons
for button in buttons:
    # Use lambda to pass the specific button text to the function
    tk.Button(root, text=button, width=5, height=2, font=("Arial", 14),
              command=lambda b=button: on_click(b)).grid(row=row_val, column=col_val, padx=5, pady=5)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Start the application loop
root.mainloop()
