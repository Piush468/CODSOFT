import tkinter as tk
from tkinter import messagebox


def click(event):
    global expression
    expression += str(event)
    input_text.set(expression)


def clear():
    global expression
    expression = ""
    input_text.set("")


def evaluate():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        expression = ""
        input_text.set("")


root = tk.Tk()
root.title("Calculator")
root.geometry("400x550")
root.resizable(0, 0)
root.configure(bg="#2c3e50")

expression = ""
input_text = tk.StringVar()


entry_frame = tk.Frame(root, bg="#2c3e50")
entry_frame.pack(pady=20)

entry = tk.Entry(entry_frame, font=('arial', 24, 'bold'), textvariable=input_text, width=17, bd=5,
                 bg="#34495e", fg="white", justify='right')
entry.grid(row=0, column=0, padx=10)


btns_frame = tk.Frame(root, bg="#2c3e50")
btns_frame.pack()


buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
    ['C']
]


for i, row in enumerate(buttons):
    for j, btn in enumerate(row):
        if btn == "=":
            b = tk.Button(btns_frame, text=btn, fg="white", bg="#e67e22", font=('arial', 20, 'bold'), bd=0,
                          width=5, height=2, command=evaluate)
        elif btn == "C":
            b = tk.Button(btns_frame, text=btn, fg="white", bg="#e74c3c", font=('arial', 20, 'bold'), bd=0,
                          width=23, height=2, command=clear)
            b.grid(row=i, column=0, columnspan=4, pady=10)
            continue
        else:
            b = tk.Button(btns_frame, text=btn, fg="white", bg="#34495e", font=('arial', 20, 'bold'), bd=0,
                          width=5, height=2, command=lambda x=btn: click(x))
        b.grid(row=i, column=j, padx=5, pady=5)


root.mainloop()
