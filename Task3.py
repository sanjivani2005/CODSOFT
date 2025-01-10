from tkinter import *
from tkinter.ttk import Combobox
import random
import string

def generate_password():
    length = solidboss.get()
    if length == 0:
        password_display.config(text="Please select a length")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    
    password_display.config(text=password)


root = Tk()
root.geometry("500x350")
root.title("Sanjivani Password Generator")
root.config(bg="pink")

Title = Label(root, text="Sanjivani Password Generator", bg="pink", fg="black", font=("futura", 15, "bold"))
Title.pack(anchor="center", pady=20)

length_label = Label(root, text="Select the length of your password:", fg="black", bg="beige", font=("ubuntu", 12,"bold"))
length_label.place(x=50, y=100)

solidboss = IntVar(value=0)
Selector = Combobox(root, textvariable=solidboss, state="readonly", values=list(range(6, 21)))
Selector.place(x=350, y=100)

generate_btn = Button(root, text="Generate Password", command=generate_password, font=("ubuntu", 14,"bold"), bg="red", fg="white")
generate_btn.place(x=175, y=150)

password_label = Label(root, text="Generated Password:", fg="Black", bg="pink", font=("ubuntu", 14,"bold"))
password_label.place(x=50, y=200)

password_display = Label(root, text="", fg="red", bg="pink", font=("futura", 15, "bold"))
password_display.place(x=50, y=230)

root.mainloop()
