import tkinter as tk

root = tk.Tk()
root.title("Widgets Example")

# 创建标签
label = tk.Label(root, text="Hello, this is a label!")
label.pack()

# 创建按钮
def button_click():
    label.config(text="Button clicked!")

button = tk.Button(root, text="Click me!", command=button_click)
button.pack()

root.mainloop()
