from tkinter import *
from tkinter import ttk

class Page(Tk):
    def __init__(self):
        super(Page, self).__init__()
        self.title("This is Page")
        self.minsize(480, 250)
        self.add_tabs()
        self.CreateComboBox()
        self.RadioButton()
        self.MakeText()

    def add_tabs(self):
        self.message1 = StringVar()
        self.message2 = StringVar()

        self.tab_control = ttk.Notebook(self)

        self.Tab1 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.Tab1, text="Tab 1 is this")

        self.Tab2 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.Tab2, text="Tab2 is this")

        self.tab_control.pack(expan=1, fill="both")

        self.labelTab1 = Label(self.Tab1, text="Hello world").grid(row=0, column=0)
        self.labelTab2 = Label(self.Tab2, text="Hello mishu").grid(row=0, column=0)

        self.MessageBox = Entry(self.Tab1, width=10, textvariable=self.message1).grid(row=1, column=0)
        self.MessageBox2 = ttk.Entry(self.Tab1, width=12, textvariable=self.message2)
        self.MessageBox2.grid(row=1, column=1)
        self.MessageBox2.focus()


        self.MessageButton = Button(self.Tab1, text="This is Button", command=self.PrintMessage1)
        self.MessageButton.grid(row=2, column=0)
        self.MessageButton = ttk.Button(self.Tab1, text="This is Button", command=self.PrintMessage2)
        self.MessageButton.grid(row=2, column=1)

    def CreateComboBox(self):
        self.ComboBoxVar = IntVar()
        self.combos = ttk.Combobox(self.Tab2, width=6, textvariable=self.ComboBoxVar)
        self.combos.grid(row=1, column=0)
        self.combos['values'] = tuple(range(1, 80))
        self.combos.set("Number")
        self.ComboButton = Button(self.Tab2, text="Confirm", command=self.ComboBoxEvent)
        self.ComboButton.grid(row=1, column=1)

    def RadioButton(self):
        self.radioVar = StringVar()
        self.radio1 = Radiobutton(self.Tab2, text="First", value="One", textvariable=self.radioVar)
        self.radio1.grid(row=3, column=0, columnspan=3)
        self.radio2 = Radiobutton(self.Tab2, text="Second", value="Two", textvariable=self.radioVar, state=DISABLED)
        self.radio2.grid(row=3, column=1)
        self.radioButton = Button(self.Tab2, text="Select", command=self.RadioEvent)
        self.radioButton.grid(row=4, column=0)
        self.radioButton = Button(self.Tab2, text="disable", command=self.disable)
        self.radioButton.grid(row=4, column=1)

    def MakeText(self):
        self.Text = Text(self.Tab1).grid(row=5, column=0)
    def PrintMessage1(self):
        self.LabelMessage1 = Label(self.Tab1, text=self.message1.get()).place(x=150, y=120)

    def PrintMessage2(self):
        self.LabelMessage2 = Label(self.Tab1, text=self.message2.get()).place(x=200, y=120)

    def ComboBoxEvent(self):
        self.label = Label(self.Tab2, text=self.ComboBoxVar.get()).grid(row=2, column=0)

    def RadioEvent(self):
        self.LabelRadio = Label(self.Tab2, text="Hello world").grid(row=5, column=0)
        self.radio2.configure(state=NORMAL)
    def disable(self):
        self.radio2.configure(state=DISABLED)

page = Page()
page.mainloop()