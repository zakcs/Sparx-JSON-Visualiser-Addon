import tkinter as tk
import json

root = tk.Tk()
root.title("bookwork code visual thing")

data = json.loads(open("data.json").read())

title = tk.Label(root, text="bookwork codez", font=("Helvetica", 16), foreground="red")
title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

code_label = tk.Label(root, text="code", font=("Helvetica", 14))
answer_label = tk.Label(root, text="answer", font=("Helvetica", 14))
code_label.grid(row=1, column=0, padx=10, pady=10)
answer_label.grid(row=1, column=1, padx=10, pady=10)

for i, (code, answer) in enumerate(data.items()):
    code_label = tk.Label(root, text=code, font=("Courier", 10))
    answer_label = tk.Label(root, text=answer, font=("Courier", 10))
    code_label.grid(row=i+2, column=0, padx=10, pady=10)
    answer_label.grid(row=i+2, column=1, padx=10, pady=10)

root.mainloop()