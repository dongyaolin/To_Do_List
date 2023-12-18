import tkinter as tk
from tkinter import messagebox

def check_inputs():
    if entry.get() and check_var.get() == 1:
        messagebox.showinfo("Success", "Inputs are valid! Performing action.")
        # 这里可以添加你希望执行的操作
    else:
        messagebox.showwarning("Warning", "Please enter text and check the box.")

root = tk.Tk()
root.title("Widgets Example")

# 获取屏幕的宽度和高度
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 设置窗口的大小为屏幕的大小
root.geometry(f"{screen_width}x{screen_height}")

# 创建文本框
entry = tk.Entry(root)
entry.pack()

# 创建复选框
check_var = tk.IntVar()
check_button = tk.Checkbutton(root, text="Check me!", variable=check_var)
check_button.pack()

# 创建按钮来执行检查操作
check_button = tk.Button(root, text="Check Inputs", command=check_inputs)
check_button.pack()

root.mainloop()
