import tkinter as tk
import os
import sys


def load_tasks():
    file_path = os.path.join(os.path.dirname(sys.executable), "tasks.txt")
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
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
            file.write(task + "\n")


def load_tasks_with_status():
    if os.path.exists("tasks_status.txt"):
        with open("tasks_status.txt", "r") as file:
            task_statuses = file.readlines()
            for idx, status in enumerate(task_statuses):
                task = listbox.get(idx)
                if task:
                    if status.strip() == "completed":
                        updated_task = task.replace("[ ]", "[✓]")
                        listbox.delete(idx)
                        listbox.insert(idx, updated_task)


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
        save_tasks_status()


def save_tasks_status():
    with open("tasks_status.txt", "w") as file:
        tasks = listbox.get(0, tk.END)
        for task in tasks:
            if "[✓]" in task:
                file.write("completed\n")
            else:
                file.write("incomplete\n")


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
load_tasks_with_status()

root.mainloop()
