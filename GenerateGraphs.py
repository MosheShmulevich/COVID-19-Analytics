from tkinter import *
from tkinter import ttk
import Database
from datetime import datetime, date
import matplotlib.pyplot as plt


class GraphGenerator(Tk):
    def __init__(self):
        super(GraphGenerator, self).__init__()
        self.title("Graph Generator")
        self.geometry("400x200")
        self.maxsize(400, 200)
        self.CalcAge()
        self.AgeDict = {}
        self.MakeInterface()

    def MakeInterface(self):
        self.City = StringVar()
        self.Cities = ttk.Combobox(self, width=12, textvariable=self.City)
        self.Cities.pack(anchor=CENTER)
        self.Cities['values'] = Database.Covid19DB.sheetnames

    def CalcAge(self):
        CitySheet = Database.Covid19DB['Lod']
        today = date.today()
        Born = datetime.strptime(str(CitySheet.cell(row=3, column=5).value.date()), "%Y-%m-%d")
        print(Born.date())
        print(today)
        Age = today.year - CitySheet.cell(row=3, column=5).value.date().year - (
                (today.month, today.day) < (Born.date().month, Born.date().day))
        print(Age)





Test = GraphGenerator()
Test.mainloop()
