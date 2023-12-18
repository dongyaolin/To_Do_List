import tkinter as tk

root = tk.Tk()
root.title("Widgets Example")

# 创建文本框
entry = tk.Entry(root)
entry.pack()

# 创建复选框
check_var = tk.IntVar()
check_button = tk.Checkbutton(root, text="Check me!", variable=check_var)
check_button.pack()

root.mainloop()
