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
        self.resizable(width=False, height=False)
        self.MakeTabs()
        self.MakeInterface()

    def MakeTabs(self):
        self.Tab_control = ttk.Notebook(self)

        self.AgeGraph = ttk.Frame(self.Tab_control)
        self.Tab_control.add(self.AgeGraph, text="Graph by age")

        self.CitiesGraph = ttk.Frame(self.Tab_control)
        self.Tab_control.add(self.CitiesGraph, text="City Graph")

        self.QuaranGraph = ttk.Frame(self.Tab_control)
        self.Tab_control.add(self.QuaranGraph, text="Graph by quarantine location")

        self.Tab_control.pack(expan=1, fill="both")

    def MakeInterface(self):
        ############# Graph by age #############
        self.CityAge = StringVar()
        self.Cities = ttk.Combobox(self.AgeGraph,  textvariable=self.CityAge)
        self.Cities.place(x=130, y=50, width=130, height=27)
        self.Cities['values'] = Database.Covid19DB.sheetnames[1:99]
        self.Cities.set("Choose City...")

        self.AgeGraphButton = Button(self.AgeGraph, text="Create Graph", width=16, relief=GROOVE, command=self.MakeAgeGraph)
        self.AgeGraphButton.place(x=136, y=80, width=120, height=27)
        ########################################

        ############# Graph by City ############
        self.SelectedFilter = StringVar()

        FilterList = []
        for Column in range(2, 14):
            FilterList += [Database.MainSheet.cell(row=1, column=Column).value]
        self.SelectFilter = ttk.Combobox(self.CitiesGraph, textvariable=self.SelectedFilter)
        self.SelectFilter.place(x=10, y=15, width=210, height=24)
        self.SelectFilter['values'] = FilterList
        self.SelectFilter.set("Choose filter...")


        self.ConfirmSelect = Button(self.CitiesGraph, text="Generate Graph", relief=RIDGE, command=self.CityGraph)
        self.ConfirmSelect.place(x=10, y=50, width=120, height=27)
        ########################################

        ############# Graph by quarantine location #############
        self.CityQuaran = StringVar()
        self.Cities = ttk.Combobox(self.QuaranGraph, width=28, textvariable=self.CityQuaran)
        self.Cities.place(x=130, y=50, width=130, height=27)
        self.Cities['values'] = Database.Covid19DB.sheetnames[1:99]
        self.Cities.set("Choose City...")

        self.LocationGraphButton = Button(self.QuaranGraph, text="Create Graph", width=16, relief=GROOVE, command=self.quarantineGraph)
        self.LocationGraphButton.place(x=136, y=80, width=120, height=27)
        ########################################################


    def CalcAge(self):
        self.AgeDict = {}
        CitySheet = Database.Covid19DB[self.CityAge.get()]
        today = date.today()
        Row = 2
        while CitySheet.cell(row=Row, column=5).value is not None:
            Born = datetime.strptime(str(CitySheet.cell(row=Row, column=5).value), '%Y-%m-%d %H:%M:%S').date()
            Age = today.year - Born.year - (
                    (today.month, today.day) < (Born.month, Born.day))
            Row += 1
            if Age in self.AgeDict:
                self.AgeDict[Age] += 1
            else:
                self.AgeDict[Age] = 1
        print(self.AgeDict)

    def MakeAgeGraph(self):
        self.CalcAge()
        plt.bar(self.AgeDict.keys(), self.AgeDict.values(), width=1, tick_label=list(self.AgeDict.keys()))
        plt.show()

    def CalcLocation(self):
        self.LocationDict = {}
        CitySheet = Database.Covid19DB[self.CityQuaran.get()]
        Row = 2
        while CitySheet.cell(row=Row, column=9).value is not None:
            Location = CitySheet.cell(row=Row, column=9).value
            if Location in self.LocationDict:
                self.LocationDict[Location] += 1
            else:
                self.LocationDict[Location] = 1
            Row += 1
        print(self.LocationDict)

    def quarantineGraph(self):
        self.CalcLocation()
        Locations = self.LocationDict.keys()
        Quantity = self.LocationDict.values()
        plt.pie(Quantity, labels=Locations, autopct='%1.1f%%', shadow=True, startangle=90)
        plt.axis('equal')
        plt.show()

    def CalcCityGraph(self):
        self.FilterDict = {}
        Sheet = Database.MainSheet
        Row = 2
        for Column in range(2, 14):
            if self.SelectedFilter.get() == Sheet.cell(row=1, column=Column).value:
                while Sheet.cell(row=Row, column=2).value is not None:
                    City = Sheet.cell(row=Row, column=1).value
                    self.FilterDict[City] = Sheet.cell(row=Row, column=Column).value
                    Row += 1
        print(self.FilterDict)

    def CityGraph(self):
        self.CalcCityGraph()
        plt.bar(self.FilterDict.keys(), self.FilterDict.values(), width=0.35)
        plt.show()



Test = GraphGenerator()
Test.mainloop()
