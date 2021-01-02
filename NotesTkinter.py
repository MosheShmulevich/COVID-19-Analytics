from tkinter import *
from tkinter import ttk


class NotesPage(Tk):
    def __init__(self):
        super(NotesPage, self).__init__()
        self.title("Notes to system")
        self.minsize(480, 260)
        self.create_tabs()
        self.add_widgets()

    def create_tabs(self):
        self.tab_control = ttk.Notebook(self)
        self.Tab1 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.Tab1, text="Contact us")
        self.tab_control.pack(expan=1, fill="both")

    def add_widgets(self):
        self.Name = StringVar()
        self.Subject = StringVar()
        self.Message = StringVar()

        self.NameLabel = Label(self.Tab1, text="Name").grid(row=0, column=0)
        self.NameBox = Entry(self.Tab1, width=20, textvariable=self.Name)
        self.NameBox.grid(row=1, column=0)

        self.SubjectLabel = Label(self.Tab1, text="Subject").grid(row=3, column=0)
        self.SubjectBox = Entry(self.Tab1, width=30, textvariable=self.Subject)
        self.SubjectBox.grid(row=4, column=0, columnspan=20)

        self.MessageLabel = Label(self.Tab1, text="Message").grid(row=5, column=0)
        self.MessageBox = Entry(self.Tab1, textvariable=self.Message)
        self.MessageBox.place(x=2, y=110, width=400, height=100)

        self.SubmitButton = Button(self.Tab1, text="Submit", command=self.SubmitCommand)
        self.SubmitButton.place(x=420, y=184)

    def SubmitCommand(self):
        self.ThanksMessage = Label(self.Tab1, text="Thank you  for your note").place(x=200, y=10)
        self.NameBox.delete(0, END)
        self.SubjectBox.delete(0, END)
        self.MessageBox.delete(0, END)


Page = NotesPage()
Page.mainloop()
