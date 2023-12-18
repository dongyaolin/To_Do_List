import tkinter as tk


def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    new_window.geometry("800x800+100+100")  # 设置新窗口的大小和位置偏移量
    label = tk.Label(new_window, text="This is a new window")
    label.pack()


root = tk.Tk()
root.title("Main Window")
root.geometry("800x800+100+100")  # 设置新窗口的大小和位置偏移量
button = tk.Button(root, text="Open New Window", command=open_new_window)
button.pack()

root.mainloop()
