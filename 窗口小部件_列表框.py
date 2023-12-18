import tkinter as tk

def get_selected_item():
    # 获取所选中的项目
    selected_indices = listbox.curselection()
    if selected_indices:
        selected_item = listbox.get(selected_indices[0])
        label.config(text=f"Selected item: {selected_item}")
    else:
        label.config(text="No item selected")

root = tk.Tk()
root.title("Listbox Example")

# 创建列表框
listbox = tk.Listbox(root)
listbox.pack()

# 向列表框中添加项目
for i in range(1, 11):
    listbox.insert(tk.END, f"Item {i}")

# 创建一个标签来显示所选中的项目
label = tk.Label(root, text="No item selected")
label.pack()

# 创建按钮来获取所选中的项目
button = tk.Button(root, text="Get Selected Item", command=get_selected_item)
button.pack()

root.mainloop()
