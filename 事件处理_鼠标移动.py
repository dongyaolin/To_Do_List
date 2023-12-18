import tkinter as tk

def on_mouse_move(event):
    label.config(text=f"Mouse coordinates: x={event.x}, y={event.y}")

root = tk.Tk()
root.title("Mouse Event Handling Example")

label = tk.Label(root, text="Move your mouse")
label.pack()

label.bind("<Motion>", on_mouse_move)  # 绑定鼠标移动事件

root.mainloop()
