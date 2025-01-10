import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("570x600+100+200")
root.resizable(False, False)
root.configure(bg="#17161b")

equation = ""

def show(value):
    global equation
    equation += value
    label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = str(eval(equation))
            equation = result  # Update equation with the result
        except:
            result = "error"
            equation = ""
    label_result.config(text=result)

label_result = tk.Label(root, width=25, height=2, text=" ", font=("arial", 30))
label_result.pack()

# Create buttons
buttons = [
    ('C', 10, 100, clear, "#3697f5"),
    ('/', 150, 100, lambda: show("/"), "#2a2d36"),
    ('%', 290, 100, lambda: show("%"), "#2a2d36"),
    ('*', 430, 100, lambda: show("*"), "#2a2d36"),
    ('7', 10, 200, lambda: show("7"), "#2a2d36"),
    ('8', 150, 200, lambda: show("8"), "#2a2d36"),
    ('9', 290, 200, lambda: show("9"), "#2a2d36"),
    ('-', 430, 200, lambda: show("-"), "#2a2d36"),
    ('4', 10, 300, lambda: show("4"), "#2a2d36"),
    ('5', 150, 300, lambda: show("5"), "#2a2d36"),
    ('6', 290, 300, lambda: show("6"), "#2a2d36"),
    ('+', 430, 300, lambda: show("+"), "#2a2d36"),
    ('1', 10, 400, lambda: show("1"), "#2a2d36"),
    ('2', 150, 400, lambda: show("2"), "#2a2d36"),
    ('3', 290, 400, lambda: show("3"), "#2a2d36"),
    ('0', 10, 500, lambda: show("0"), "#2a2d36", 11, 1),
    ('.', 290, 500, lambda: show("."), "#2a2d36"),
    ('=', 430, 400, calculate, "#fe9037", 5, 3)
]

for button in buttons:
    if len(button) == 7:
        text, x, y, command, color, width, height = button
    else:
        text, x, y, command, color = button
        width, height = 5, 1

    tk.Button(root, text=text, width=width, height=height, font=("arial", 30, "bold"), bd=1, fg="#fff", bg=color, command=command).place(x=x, y=y)

root.mainloop()
