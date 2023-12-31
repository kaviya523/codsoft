import tkinter as tk

# Function to perform calculations
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to add characters to the entry widget
def add_to_entry(character):
    entry.insert(tk.END, character)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to display and input numbers/operators
entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Add buttons to the calculator
for (text, row, col) in buttons:
    if text != '=':
        button = tk.Button(root, text=text, padx=20, pady=10, command=lambda t=text: add_to_entry(t))
        button.grid(row=row, column=col, padx=5, pady=5)
    else:
        button = tk.Button(root, text=text, padx=20, pady=10, command=calculate)
        button.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
