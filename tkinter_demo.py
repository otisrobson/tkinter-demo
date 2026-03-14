import tkinter as tk

root = tk.Tk()
root.title("My First GUI")
root.geometry("400x300")

label = tk.Label(root, text="Hello, World!", font=("Arial", 24))
label.pack(pady=40)

count = tk.IntVar(value=0)

def on_click():
    count.set(count.get() + 1)

counter_label = tk.Label(root, textvariable=count, font=("Arial", 18))
counter_label.pack(pady=10)

button = tk.Button(root, text="Click me!", command=on_click, font=("Arial", 14))
button.pack(pady=10)

root.mainloop()
