from tkinter import *
from tkinter import ttk


class UpdatingPage(Tk):
    def __init__(self):
        super(UpdatingPage, self).__init__()
        self.title("Application")
        self.minsize(500, 500)
        self.AddTabs()
        self.CreateLabel()
        self.CreateButton()

    def AddTabs(self):
        self.tab_control = ttk.Notebook(self)
        self.UpdatingPage = ttk.Frame(self.tab_control)
        self.tab_control.add(self.UpdatingPage, text="Updating Page")

        self.ContactInformation = ttk.Frame(self.tab_control)
        self.tab_control.add(self.ContactInformation, text="Contact Us")
        self.tab_control.pack(expan=1, fill="both")

    def CreateLabel(self):
        self.Updating = StringVar()
        self.labelUpdatingPage = Label(self.UpdatingPage, text="Enter the updates here:").grid(row=0, column=0)
        self.labelContactInformation = Label(self.ContactInformation,
        text="Phone:00-0000000\nFax:00-0000000\nEmail:WorkerName@company.il").grid(row=0, column=0)

    def CreateButton(self):
        self.MessageButton = Button(self.UpdatingPage, text="Submit", command=self.PrintMessage)
        self.MessageButton.grid(row=2, column=0)
        self.MessageBox = Entry(self.UpdatingPage, width=40, textvariable=self.Updating).grid(row=1, column=0)

    def PrintMessage(self):
        self.LabelMessage = Label(self.UpdatingPage, text=self.Updating.get()).place(x=0, y=80)

updates = UpdatingPage()
updates.mainloop()
