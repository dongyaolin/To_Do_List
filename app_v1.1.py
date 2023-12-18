import tkinter as tk
import os

def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            for line in file:
                task = line.strip()
                listbox.insert(tk.END, task)

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, f"{task} [ ]")
        entry.delete(0, tk.END)
        save_tasks()

def delete_task():
    selected_indices = listbox.curselection()
    if selected_indices:
        listbox.delete(selected_indices)
        save_tasks()

def save_tasks():
    with open("tasks.txt", "w") as file:
        tasks = listbox.get(0, tk.END)
        for task in tasks:
            file.write(task.split("[")[0].strip() + "\n")

def toggle_task(event):
    selected_indices = listbox.curselection()
    if selected_indices:
        current_task = listbox.get(selected_indices[0])
        if "[ ]" in current_task:
            updated_task = current_task.replace("[ ]", "[✓]")
        else:
            updated_task = current_task.replace("[✓]", "[ ]")
        listbox.delete(selected_indices)
        listbox.insert(selected_indices[0], updated_task)
        save_tasks()

root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

entry = tk.Entry(frame, width=25)
entry.grid(row=0, column=0, padx=5)

add_button = tk.Button(frame, text="Add", command=add_task)
add_button.grid(row=0, column=1, padx=5)

delete_button = tk.Button(frame, text="Delete", command=delete_task)
delete_button.grid(row=0, column=2, padx=5)

listbox = tk.Listbox(root, width=30, height=10)
listbox.pack(pady=10)

listbox.bind("<Double-Button-1>", toggle_task)

load_tasks()

root.mainloop()
