import tkinter as tk

root = tk.Tk()
root.title("Place Layout Example")

# 创建三个不同颜色的标签
label1 = tk.Label(root, text="Label 1", bg="red")
label2 = tk.Label(root, text="Label 2", bg="green")
label3 = tk.Label(root, text="Label 3", bg="blue")

# 使用 place 将标签放置到窗口中，并指定坐标位置
label1.place(x=10, y=10)
label2.place(x=50, y=50)
label3.place(x=100, y=100)

root.mainloop()
