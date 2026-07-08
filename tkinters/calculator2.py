import tkinter as tk
import math

root = tk.Tk()
root.title("Scientific Calculator")

entry = tk.Entry(root, font=("Arial", 20), width=25, justify="right")
entry.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

# ---------------- Functions ---------------- #

def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get().replace("^", "**")
        result = eval(expression, {
            "__builtins__": None,
            "sqrt": math.sqrt,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "log": math.log10,
            "ln": math.log,
            "pi": math.pi,
            "e": math.e
        })

        entry.delete(0, tk.END)
        entry.insert(tk.END, result)

    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# ---------------- Buttons ---------------- #

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3), ('sqrt(',1,4),

    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3), ('^',2,4),

    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3), ('(',3,4),

    ('0',4,0), ('.',4,1), ('+',4,2), (')',4,3), ('C',4,4),

    ('sin(',5,0), ('cos(',5,1), ('tan(',5,2), ('log(',5,3), ('ln(',5,4),

    ('pi',6,0), ('e',6,1), ('=',6,2,3)
]

# ---------------- Create Buttons ---------------- #

for button in buttons:

    if len(button) == 3:

        text = button[0]

        if text == "C":
            command = clear
        else:
            command = lambda value=text: click(value)

        tk.Button(
            root,
            text=text,
            width=6,
            height=2,
            font=("Arial",14),
            command=command
        ).grid(row=button[1], column=button[2], padx=3, pady=3)

    else:

        tk.Button(
            root,
            text=button[0],
            width=20,
            height=2,
            font=("Arial",14),
            command=calculate
        ).grid(
            row=button[1],
            column=button[2],
            columnspan=button[3],
            padx=3,
            pady=3
        )

root.mainloop()