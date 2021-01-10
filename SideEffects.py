from tkinter import ttk
from tkinter import *

class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()
        self.title("Side Effects")
        self.minsize(400, 320)
        self.add_tabs()

    def add_tabs(self):
        self.message1 = StringVar()
        self.message2 = StringVar()

        self.tab_control = ttk.Notebook(self)

        self.Tab1 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.Tab1, text="Check Health Status")

        self.Tab2 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.Tab2, text="Recovering Questionnaire")

        self.tab_control.pack(expan=1, fill="both")

        self.labelTab1 = Label(self.Tab1, text="Enter Corona Test's answer:").grid(row=0, column=0)
        self.labelTab2 = Label(self.Tab2, text="Do you have any breathing problems? ").grid(row=0, column=0)
        self.labelTab2 = Label(self.Tab2, text="Do you feel tiredness? ").grid(row=6, column=0)
        self.labelTab2 = Label(self.Tab2, text="Do you have dry cough? ").grid(row=12, column=0)

        self.ComboBoxVar1 = StringVar()
        self.ComboBoxVar2 = StringVar()
        self.ComboBoxVar3 = StringVar()
        self.ComboBoxVar4 = StringVar()

        self.combos1 = ttk.Combobox(self.Tab1, width=6, textvariable=self.ComboBoxVar1)
        self.combos1.grid(row=1, column=0)
        self.combos1['values'] = ['Recovered', 'Negative', 'Positive']

        self.combos = ttk.Combobox(self.Tab2, width=6, textvariable=self.ComboBoxVar2)
        self.combos.grid(row=1, column=0)
        self.combos['values'] = ['No', 'Yes']

        self.combos = ttk.Combobox(self.Tab2, width=6, textvariable=self.ComboBoxVar3)
        self.combos.grid(row=7, column=0)
        self.combos['values'] = ['No', 'Yes']

        self.combos = ttk.Combobox(self.Tab2, width=6, textvariable=self.ComboBoxVar4)
        self.combos.grid(row=13, column=0)
        self.combos['values'] = ['No', 'Yes']

        self.MessageButton = Button(self.Tab1, text="Submit", command=self.PrintMessage1)
        self.MessageButton.grid(row=2, column=0)

        self.MessageButton = Button(self.Tab2, text="Submit", command=self.PrintMessage2)
        self.MessageButton.grid(row=15, column=0)

    def PrintMessage1(self):
        if self.ComboBoxVar1.get() == 'Negative':
                self.LabelMessage1 = Label(self.Tab1, text=self.combos1['values'][0]).place(x=60, y=80)
        else:
                self.LabelMessage1 = Label(self.Tab1, text=self.ComboBoxVar1.get()).place(x=60, y=80)

    def PrintMessage2(self):
        if self.ComboBoxVar2.get() == 'Negative':
                self.LabelMessage2 = Label(self.Tab2, text=self.combos['values'][0]).place(x=250, y=0)
        else:
                self.LabelMessage2 = Label(self.Tab2, text=self.ComboBoxVar2.get()).place(x=250, y=0)

        if self.ComboBoxVar3.get() == 'Negative':
                self.LabelMessage2 = Label(self.Tab2, text=self.combos['values'][0]).place(x=250, y=50)
        else:
                self.LabelMessage2 = Label(self.Tab2, text=self.ComboBoxVar3.get()).place(x=250, y=50)

        if self.ComboBoxVar4.get() == 'Negative':
                self.LabelMessage2 = Label(self.Tab2, text=self.combos['values'][0]).place(x=250, y=100)
        else:
                self.LabelMessage2 = Label(self.Tab2, text=self.ComboBoxVar4.get()).place(x=250, y=100)


window = Window()
window.mainloop()
