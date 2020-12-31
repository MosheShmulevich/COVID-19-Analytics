import Database
from tkinter import *
from tkinter import ttk



class ReportsPage(Tk):
    def __init__(self):
        super(ReportsPage, self).__init__()
        self.title("Reports Creating Page")
        self.minsize(1280, 620)
        self.wm_iconbitmap("Logo.ico")
        self.create_tabs()
        self.add_widgets()

    def create_tabs(self):
        self.tab_control = ttk.Notebook(self)
        self.Tab1 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.Tab1, text="Find By Category")
        self.Tab2 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.Tab2, text="Find By City")
        self.tab_control.pack(expan=1, fill="both")

    def add_widgets(self):
        ########## Tab1 #########
        self.Message = Label(self.Tab1, text="Choose by which category you would like to get a Report")
        self.Message.grid(row=0, column=0, columnspan=20)
        self.Message.config(font=('Lato', 14,))

        self.option = StringVar()
        self.combobox = ttk.Combobox(self.Tab1, width=25, textvariable=self.option)
        self.combobox.set('Choose option')
        self.combobox['values'] = ("Total Cases", "New Cases", "Active Cases", "Total Deaths", "New Deaths", "Total "
                                                                                                             "Recovered",
                                   "New Recovered", "Total Tests", "Cases to 1M Population", "Tests to 1M Population",
                                   "Deaths to 1M Population", "Population")
        self.combobox.grid(row=2, column=0)

        self.button = ttk.Button(self.Tab1, text="Create report", command=self.create_CityAndOption_report)
        self.button.grid(row=2, column=1)
        ##########################

        ########## Tab 2 #########
        self.CityMessage = Label(self.Tab2, text="Choose which city data you need")
        self.CityMessage.grid(row=0, column=0, columnspan=20)
        self.CityMessage.config(font=('Lato', 14,))

        self.city = StringVar()
        self.combobox_city = ttk.Combobox(self.Tab2, width=25, textvariable=self.city)
        self.combobox_city.set('Choose city')
        self.combobox_city['values'] = Database.IL_CityList
        self.combobox_city.grid(row=2, column=0)

        self.button = ttk.Button(self.Tab2, text="Create report", command=self.create_city_report)
        self.button.grid(row=2, column=1)
        ##########################

    def create_CityAndOption_report(self):
        r = 0
        c = 0
        for row in range(2, 100):
            for column in range(2, 14):
                if Database.city_sheet.cell(row=1, column=column).value == self.option.get():
                    self.Result = Label(self, text=(Database.city_sheet.cell(row=row, column=1).value, ':',
                                                    Database.city_sheet.cell(row=row, column=column).value)).pack()
                    c += 1
                r += 1

    def create_city_report(self):
        city_row = 0
        for row in range(2, 100):
            if Database.city_sheet.cell(row=row, column=1).value == self.city.get():
                city_row = row
        self.City = Label(self, text=Database.city_sheet.cell(row=city_row, column=1).value).pack()
        for column in range(2, 14):
            self.CityResult = Label(self, text=(Database.city_sheet.cell(row=1, column=column).value, ':',
                                                Database.city_sheet.cell(row=city_row, column=column).value)).pack()


Reports = ReportsPage()
Reports.mainloop()
