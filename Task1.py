from tkinter import * 
from tkinter import ttk

class Todo:
    def __init__(self, root):
        self.root = root 
        self.root.title("To-Do List")
        self.root.geometry('650x410+300+150')
        self.root.configure(bg='lightgrey')

        self.label = Label(self.root, text='To-Do List APP', font='arial 25 bold', width=24, bd=5, bg='Red', fg='white')
        self.label.grid(row=0, column=0, columnspan=3, pady=10)

        self.label2 = Label(self.root, text='Add task', font='arial 18 bold', width=10, bd=5, bg='Red', fg='white')
        self.label2.grid(row=1, column=0, padx=20, pady=10)

        self.label3 = Label(self.root, text='Tasks', font='arial 18 bold', width=10, bd=5, bg='Red', fg='white')
        self.label3.grid(row=1, column=1, padx=20, pady=10)

        self.text = Text(self.root, bd=5, height=2, width=30, font='arial 10 bold')
        self.text.grid(row=2, column=0, padx=20, pady=10)

        self.main_text = Listbox(self.root, height=10, bd=5, width=40, font="arial 12 italic bold")
        self.main_text.grid(row=2, column=1, padx=20, pady=10, rowspan=4)

        self.add_btn = Button(self.root, text="Add Task", command=self.add, font='arial 10 bold', bd=5, bg='Red', fg='white')
        self.add_btn.grid(row=3, column=0, pady=10)

        self.del_btn = Button(self.root, text="Delete Task", command=self.delete, font='arial 10 bold', bd=5, bg='Red', fg='white')
        self.del_btn.grid(row=4, column=0, pady=10)

    def add(self):
        content = self.text.get(1.0, END).strip()
        if content:
            self.main_text.insert(END, content)
            with open('data.txt', 'a') as file:
                file.write(content + '\n')
            self.text.delete(1.0, END)

    def delete(self):
        try:
            selected_index = self.main_text.curselection()[0]
            selected_task = self.main_text.get(selected_index)
            self.main_text.delete(selected_index)
            with open('data.txt', 'r') as f:
                lines = f.readlines()
            with open('data.txt', 'w') as f:
                for line in lines:
                    if line.strip("\n") != selected_task:
                        f.write(line)
        except IndexError:
            pass

def main():
    root = Tk()
    ui = Todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
