import tkinter as tk

root = tk.Tk()
root.title("Grid Layout Example")

# 创建三个不同颜色的标签
label1 = tk.Label(root, text="Label 1", bg="red")
label2 = tk.Label(root, text="Label 2", bg="green")
label3 = tk.Label(root, text="Label 3", bg="blue")

# 使用 grid 将标签放置到窗口中，并指定行列位置
label1.grid(row=0, column=0)
label2.grid(row=0, column=2)
label3.grid(row=1, column=0, columnspan=2)  # 占据两列

root.mainloop()
