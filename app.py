"""
这个简单的待办事项应用程序具有以下功能：

有一个输入框用于添加新任务。
有一个 "Add" 按钮，用于将任务添加到列表中。
有一个列表框显示当前的任务列表。
有一个 "Delete" 按钮，用于删除选定的任务。
这个项目基于 Tkinter 创建了一个简单的用户界面，可以实现添加和删除待办事项的基本功能。你可以进一步扩展它，比如增加保存功能、标记已完成的任务等，以加强其功能性和用户体验。
"""
import tkinter as tk


def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)


def delete_task():
    selected_indices = listbox.curselection()
    if selected_indices:
        listbox.delete(selected_indices)


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

root.mainloop()
