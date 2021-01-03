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

        self.Category = ttk.Frame(self.tab_control)
        self.tab_control.add(self.Category, text="Find by Category")

        self.City = ttk.Frame(self.tab_control)
        self.tab_control.add(self.City, text="Find by City")

        self.ID = ttk.Frame(self.tab_control)
        self.tab_control.add(self.ID, text="Find by ID")

        self.Name = ttk.Frame(self.tab_control)

        self.tab_control.add(self.Name, text="Find by Name")
        self.tab_control.pack(expan=1, fill="both")

    def add_widgets(self):
        ########## Category Tab #########
        self.Message = Label(self.Category, text="Choose by which category you would like to get a Report")
        self.Message.grid(row=0, column=0, columnspan=20)
        self.Message.config(font=('Lato', 14,))

        self.option = StringVar()
        self.combobox = ttk.Combobox(self.Category, width=25, textvariable=self.option)
        self.combobox.set('Choose option')
        self.combobox['values'] = ("Total Cases", "New Cases", "Active Cases", "Total Deaths", "New Deaths", "Total "
                                                                                                             "Recovered",
                                   "New Recovered", "Total Tests", "Cases to 1M Population", "Tests to 1M Population",
                                   "Deaths to 1M Population", "Population")
        self.combobox.grid(row=2, column=0)

        self.button = ttk.Button(self.Category, text="Create report", command=self.create_CityAndOption_report)
        self.button.grid(row=2, column=1)
        ##########################

        ########## City Tab #########
        self.CityMessage = Label(self.City, text="Choose which city data you need")
        self.CityMessage.grid(row=0, column=0, columnspan=20)
        self.CityMessage.config(font=('Lato', 14,))

        self.city = StringVar()
        self.combobox_city = ttk.Combobox(self.City, width=25, textvariable=self.city)
        self.combobox_city.set('Choose city')
        self.combobox_city['values'] = Database.IL_CityList
        self.combobox_city.grid(row=2, column=0)

        self.button = ttk.Button(self.City, text="Create report", command=self.create_city_report)
        self.button.grid(row=2, column=1)
        ###########################

        ########## ID Tab #########
        self.iD = IntVar()
        self.idCity = StringVar()
        CitySheets = list(Database.Covid19DB.sheetnames)

        self.cityMessage = Label(self.ID, text="Select city of the patient")
        self.cityMessage.grid(row=0, column=0)

        self.cityComboBox = ttk.Combobox(self.ID, width=7, textvariable=self.idCity)
        self.cityComboBox.grid(row=0, column=1)
        self.cityComboBox.set("City")
        self.cityComboBox['values'] = CitySheets

        self.idMessage = Label(self.ID, text="Enter ID")
        self.idMessage.grid(row=1, column=0)
        self.idMessage.config(font=('Lato', 12))

        self.idEntry = Entry(self.ID, width=20, textvariable=self.iD).grid(row=2, column=0)

        self.idButton = ttk.Button(self.ID, text="Confirm", command=self.ReportByID)
        self.idButton.grid(row=2, column=1)
        ###########################

        ########## Name Tab #########
        self.FirstName = StringVar()
        self.LastName = StringVar()
        self.SelectedCity = StringVar()

        self.cityMessage = Label(self.Name, text="Select city of the patient")
        self.cityMessage.grid(row=0, column=0)

        self.cityComboBox = ttk.Combobox(self.Name, width=7, textvariable=self.SelectedCity)
        self.cityComboBox.grid(row=0, column=1)
        self.cityComboBox.set("City")
        self.cityComboBox['values'] = CitySheets

        self.Firstname_Message = Label(self.Name, text="Enter Firstname")
        self.Firstname_Message.grid(row=1, column=0)
        self.Firstname_Message.config(font=('Lato', 12))
        self.Firstname_Entry = Entry(self.Name, width=20, textvariable=self.FirstName).grid(row=2, column=0)

        self.Lastname_Message = Label(self.Name, text="Enter Lastname")
        self.Lastname_Message.grid(row=3, column=0)
        self.Lastname_Message.config(font=('Lato', 12))
        self.Lastname_Entry = Entry(self.Name, width=20, textvariable=self.LastName).grid(row=4, column=0)

        self.PatientButton = ttk.Button(self.Name, text="Confirm", command=self.ReportByName)
        self.PatientButton.grid(row=5, column=0)

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
        city_row = 1
        for row in range(2, 100):
            if Database.city_sheet.cell(row=row, column=1).value == self.city.get():
                city_row = row
        self.City = Label(self, text=Database.city_sheet.cell(row=city_row, column=1).value).pack()
        for column in range(2, 14):
            self.CityResult = Label(self, text=(Database.city_sheet.cell(row=1, column=column).value, ':',
                                                Database.city_sheet.cell(row=city_row, column=column).value)).pack()
    def ReportByID(self):
        citySheet = Database.Covid19DB[self.idCity.get()]
        id = self.iD.get()
        PatientRow = None
        for rw in range(2, 28):
            if citySheet.cell(row=rw, column=3).value == id:
                PatientRow = rw
        if PatientRow == None:
            self.NoPatient = Label(self.ID, text="Patient with such id do not exist in the system!").place(x=500, y=500)
            return 1

        self.firstname = Label(self.ID, text=("Firstname:", citySheet.cell(row=PatientRow, column=1).value))
        self.firstname.config(font=('Lato', 11))
        self.firstname.place(x=240, y=45)

        self.lastname = Label(self.ID, text=("Lastname:", citySheet.cell(row=PatientRow, column=2).value))
        self.lastname.config(font=('Lato', 11))
        self.lastname.place(x=240, y=90)

        self.id = Label(self.ID, text=("ID:", citySheet.cell(row=PatientRow, column=3).value))
        self.id.config(font=('Lato', 11))
        self.id.place(x=240, y=135)

        self.bDay = Label(self.ID, text=("Date of birth:", citySheet.cell(row=PatientRow, column=4).value))
        self.bDay.config(font=('Lato', 11))
        self.bDay.place(x=240, y=180)

        self.testDay = Label(self.ID, text=("Test Date:", citySheet.cell(row=PatientRow, column=5).value))
        self.testDay.config(font=('Lato', 11))
        self.testDay.place(x=240, y=225)

        self.status = Label(self.ID, text=("Patient Status:", citySheet.cell(row=PatientRow, column=6).value))
        self.status.config(font=('Lato', 11))
        self.status.place(x=240, y=275)

        self.Quaran = Label(self.ID, text=("In Quarantine?:", citySheet.cell(row=PatientRow, column=7).value))
        self.Quaran.config(font=('Lato', 11))
        self.Quaran.place(x=240, y=320)

        self.WhereQuaran = Label(self.ID, text=("Where In Quarantine?", citySheet.cell(row=PatientRow, column=8).value))
        self.WhereQuaran.config(font=('Lato', 11))
        self.WhereQuaran.place(x=240, y=365)

    def ReportByName(self):
        citySheet = Database.Covid19DB[self.SelectedCity.get()]
        first_name = self.FirstName.get()
        last_name = self.LastName.get()
        PatientRow = None
        for rw in range(2, 28):
            if citySheet.cell(row=rw, column=1).value == first_name and citySheet.cell(row=rw, column=2).value == last_name:
                PatientRow = rw
        if PatientRow == None:
            self.NoPatient = Label(self.Name, text="Patient with such id do not exist in the system!").place(x=500, y=500)
            return 1

        self.firstname = Label(self.Name, text=("Firstname:", citySheet.cell(row=PatientRow, column=1).value))
        self.firstname.config(font=('Lato', 11))
        self.firstname.place(x=240, y=45)

        self.lastname = Label(self.Name, text=("Lastname:", citySheet.cell(row=PatientRow, column=2).value))
        self.lastname.config(font=('Lato', 11))
        self.lastname.place(x=240, y=90)

        self.id = Label(self.Name, text=("ID:", citySheet.cell(row=PatientRow, column=3).value))
        self.id.config(font=('Lato', 11))
        self.id.place(x=240, y=135)

        self.bDay = Label(self.Name, text=("Date of birth:", citySheet.cell(row=PatientRow, column=4).value))
        self.bDay.config(font=('Lato', 11))
        self.bDay.place(x=240, y=180)

        self.testDay = Label(self.Name, text=("Test Date:", citySheet.cell(row=PatientRow, column=5).value))
        self.testDay.config(font=('Lato', 11))
        self.testDay.place(x=240, y=225)

        self.status = Label(self.Name, text=("Patient Status:", citySheet.cell(row=PatientRow, column=6).value))
        self.status.config(font=('Lato', 11))
        self.status.place(x=240, y=275)

        self.Quaran = Label(self.Name, text=("In Quarantine?:", citySheet.cell(row=PatientRow, column=7).value))
        self.Quaran.config(font=('Lato', 11))
        self.Quaran.place(x=240, y=320)

        self.WhereQuaran = Label(self.Name, text=("Where In Quarantine?", citySheet.cell(row=PatientRow, column=8).value))
        self.WhereQuaran.config(font=('Lato', 11))
        self.WhereQuaran.place(x=240, y=365)



Reports = ReportsPage()
Reports.mainloop()
