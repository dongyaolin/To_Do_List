import tkinter as tk

root = tk.Tk()
root.title("Pack Layout Example")

# 创建三个不同颜色的标签
label1 = tk.Label(root, text="Label 1", bg="red")
label2 = tk.Label(root, text="Label 2", bg="green")
label3 = tk.Label(root, text="Label 3", bg="blue")

# 使用 pack 将标签放置到窗口中，并指定排列顺序和方向
label1.pack(fill="both")  # 默认从上往下排列
label2.pack(fill="both")  # 默认从上往下排列
label3.pack(fill="both")  # 默认从上往下排列

root.mainloop()
