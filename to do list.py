import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    color = color_var.get()

    if task.strip() == '':
        messagebox.showwarning("Warning", "Please enter a task.")
    else:
        task_list.insert(tk.END, task)
        task_list.itemconfig(tk.END, {'bg': color})
        task_entry.delete(0, tk.END)

def remove_task():
    try:
        task_index = task_list.curselection()[0]
        task_list.delete(task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")


root = tk.Tk()
root.title("To-Do List")


task_entry = tk.Entry(root, width=40)
task_entry.grid(row=0, column=0, padx=10, pady=5)


colors = {
    "Red": "#FF9999",
    "Green": "#99FF99",
    "Blue": "#9999FF",
    "Yellow": "#FFFF99",
}

color_var = tk.StringVar()
color_var.set("#FFFFFF")

color_menu = tk.OptionMenu(root, color_var, *colors.values())
color_menu.grid(row=0, column=1, padx=10, pady=5)


add_button = tk.Button(root, text="Add Task", width=10, command=add_task)
add_button.grid(row=0, column=2, padx=10, pady=5)


task_list = tk.Listbox(root, width=50, height=10)
task_list.grid(row=1, columnspan=3, padx=10, pady=5)


remove_button = tk.Button(root, text="Remove Task", width=10, command=remove_task)
remove_button.grid(row=2, column=1, padx=10, pady=5)

root.mainloop()
