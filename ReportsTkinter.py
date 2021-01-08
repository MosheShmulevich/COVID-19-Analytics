import Database
from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime, date


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
        self.tab_control.add(self.Category, text="Report by Category")

        self.City = ttk.Frame(self.tab_control)
        self.tab_control.add(self.City, text="Report by City")

        self.Location = ttk.Frame(self.tab_control)
        self.tab_control.add(self.Location, text="Report by Quarantine Location")

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
        FilterList = []
        for Column in range(2, 14):
            FilterList += [Database.MainSheet.cell(row=1, column=Column).value]
        self.combobox = ttk.Combobox(self.Category, width=25, textvariable=self.option)
        self.combobox.set('Choose option')
        self.combobox['values'] = FilterList
        self.combobox.grid(row=2, column=0)

        self.button = ttk.Button(self.Category, text="Create report",
                                 command=self.create_CityAndOption_report_MessageBox)
        self.button.grid(row=2, column=1)
        #################################

        ############ City Tab ###########
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
        #################################

        ######### Location Tab ##########
        self.SelectCity = StringVar()
        self.SelectLocation = StringVar()

        self.Data = Text(self.Location, state=DISABLED, font=(12))
        self.Data.place(x=500, y=20, width=600, height=500)

        self.DataScroll = ttk.Scrollbar(self.Location, orient="vertical", command=self.Data.yview)
        self.DataScroll.place(x=1100, y=20, height=500)

        self.City_Message = Label(self.Location, text="Choose which city data you need")
        self.City_Message.place(x=5, y=2)
        self.City_Message.config(font=('Lato', 14,))

        self.CitySelect = ttk.Combobox(self.Location, width=25, textvariable=self.SelectCity)
        self.CitySelect.set('Choose city')
        self.CitySelect['values'] = Database.Covid19DB.sheetnames[1:99]
        self.CitySelect.place(x=5, y=35)

        self.button = ttk.Button(self.Location, text="Create report", command=self.ReportByLocation)
        self.button.place(x=190, y=33)

        self.ClearButton = Button(self.Location, text="Clear data", command=self.Clear)
        self.ClearButton.place(x=10, y=100, width=100)

        self.locationLabel = Label(self.Location, text="Location:")
        self.locationLabel.config(font=('Lato', 12,))
        self.locationLabel.place(x=2, y=66)

        self.HotelButton = Radiobutton(self.Location, text="Hotel", value="Hotel", variable=self.SelectLocation)
        self.HotelButton.place(x=100, y=66)
        self.HotelButton.configure(font=('Lato', 12))

        self.HomeButton = Radiobutton(self.Location, text="Home", value="Home", variable=self.SelectLocation)
        self.HomeButton.place(x=180, y=66)
        self.HomeButton.configure(font=('Lato', 12))

        self.HospitalButton = Radiobutton(self.Location, text="Hospital", value="Hospital",
                                          variable=self.SelectLocation)
        self.HospitalButton.place(x=260, y=66)
        self.HospitalButton.configure(font=('Lato', 12))

        #################################

        ############# ID Tab ############
        self.iD = IntVar()
        self.idCity = StringVar()
        CitySheets = list(Database.Covid19DB.sheetnames)

        self.cityMessage = Label(self.ID, text="Select city of the patient")
        self.cityMessage.grid(row=0, column=0)

        self.cityComboBox = ttk.Combobox(self.ID, width=7, textvariable=self.idCity)
        self.cityComboBox.grid(row=0, column=1)
        self.cityComboBox.set("City")
        self.cityComboBox['values'] = CitySheets[1:99]

        self.idMessage = Label(self.ID, text="Enter ID")
        self.idMessage.grid(row=1, column=0)
        self.idMessage.config(font=('Lato', 12))

        self.idEntry = Entry(self.ID, width=20, textvariable=self.iD).grid(row=2, column=0)

        self.idButton = ttk.Button(self.ID, text="Confirm", command=self.ReportByID)
        self.idButton.grid(row=2, column=1)
        #################################

        ############ Name Tab ###########
        self.FirstName = StringVar()
        self.LastName = StringVar()
        self.SelectedCity = StringVar()

        self.cityMessage = Label(self.Name, text="Select city of the patient")
        self.cityMessage.grid(row=0, column=0)

        self.cityComboBox = ttk.Combobox(self.Name, width=7, textvariable=self.SelectedCity)
        self.cityComboBox.grid(row=0, column=1)
        self.cityComboBox.set("City")
        self.cityComboBox['values'] = CitySheets[1:99]

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
        #################################

    def Clear(self):
        self.Data.configure(state=NORMAL)
        self.Data.delete(1.0, END)
        self.Data.configure(state=DISABLED)

    def create_CityAndOption_report_MessageBox(self):
        CitiesDict = {}
        Row = 2
        while Database.MainSheet.cell(row=Row, column=1).value is not None:
            for Column in range(2, 14):
                if Database.MainSheet.cell(row=1, column=Column).value == self.option.get():
                    City = Database.MainSheet.cell(row=Row, column=1).value
                    CitiesDict[City] = Database.MainSheet.cell(row=Row, column=Column).value
            Row += 1
        Text = ""
        for pair in CitiesDict:
            Text += "{0} : {1}\n".format(pair, CitiesDict[pair])
        messagebox.showinfo("Cities Report", Text)

    def create_city_report(self):
        CityDict = {}
        city_row = None
        City = self.city.get()
        Row = 2
        while Database.MainSheet.cell(row=Row, column=1).value is not None:
            if Database.MainSheet.cell(row=Row, column=1).value == City:
                city_row = Row
                for Column in range(2, 14):
                    if Column in (10, 11, 12):
                        CityDict[Database.MainSheet.cell(row=1, column=Column).value] = \
                            int(Database.MainSheet.cell(row=city_row, column=Column).value)
                    else:
                        CityDict[Database.MainSheet.cell(row=1, column=Column).value] = \
                            Database.MainSheet.cell(row=city_row, column=Column).value
            Row += 1

        Text = "{0}\n".format(Database.MainSheet.cell(row=city_row, column=1).value)
        for pair in CityDict:
            Text += "{0} : {1}\n".format(pair, CityDict[pair])
        messagebox.showinfo("City {0} Report".format(City), Text)

    def ReportByLocation(self):
        if len(self.Data.get("1.0", "end-1c")) != 0:
            self.Clear()
        self.Data.configure(state=NORMAL)
        citySheet = Database.Covid19DB[self.SelectCity.get()]
        Location = self.SelectLocation.get()
        def switch(option):
            switcher = {
                1: 'Firstname:',
                2: 'Lastname:',
                3: 'Sex:',
                4: 'ID:',
                5: 'Birth date:',
                6: 'Test date:',
                7: 'Patient Status:',
                8: 'Quarantined:'
            }
            return switcher[option]

        for ROW in range(1, 28):
            if citySheet.cell(row=ROW, column=9).value == Location:
                self.Data.insert(INSERT, "-------------------------------\n")  #seperator
                for Column in range(1, 9):
                    if Column in (5, 6):
                        self.Date = date
                        self.Date = datetime.strptime(str(citySheet.cell(row=ROW,
                                                                    column=Column).value), '%Y-%m-%d %H:%M:%S').date()
                        self.Data.insert(INSERT, "{0} {1}\n".format(switch(Column), self.Date))
                    else:
                        self.Data.insert(INSERT, "{0} {1}\n".format(switch(Column),
                                                                               citySheet.cell(row=ROW,
                                                                                              column=Column).value))
        self.DataScroll.config(command=self.Data.yview)
        self.Data.config(yscrollcommand = self.DataScroll.set)
        self.Data.configure(state=DISABLED)

    def ReportByID(self):
        citySheet = Database.Covid19DB[self.idCity.get()]
        id = self.iD.get()
        PatientRow = None
        for rw in range(2, 28):
            if citySheet.cell(row=rw, column=4).value == id:
                PatientRow = rw
        if PatientRow == None:
            self.NoPatient = Label(self.ID, text="Patient with such id do not exist in the system!").place(x=500, y=500)
            return 1

        self.firstname = Label(self.ID, text=("Firstname:", citySheet.cell(row=PatientRow,
                                                                           column=1).value), font=('Lato', 11))
        self.firstname.place(x=240, y=45)

        self.lastname = Label(self.ID, text=("Lastname:", citySheet.cell(row=PatientRow,
                                                                         column=2).value), font=('Lato', 11))
        self.lastname.place(x=240, y=90)

        self.sex = Label(self.ID, text=("Sex:", citySheet.cell(row=PatientRow, column=3).value), font=('Lato', 11))
        self.sex.place(x=240, y=135)

        self.id = Label(self.ID, text=("ID:", citySheet.cell(row=PatientRow, column=4).value), font=('Lato', 11))
        self.id.place(x=240, y=180)

        self.DateOfBirth = date
        self.DateOfBirth = datetime.strptime(str(citySheet.cell(row=PatientRow, column=5).value),
                                             '%Y-%m-%d %H:%M:%S').date()
        self.bDay = Label(self.ID, text=("Date of birth: {0}".format(self.DateOfBirth)), font=('Lato', 11))
        self.bDay.place(x=240, y=225)

        self.DateOfTest = date
        self.DateOfTest = datetime.strptime(str(citySheet.cell(row=PatientRow, column=6).value),
                                            '%Y-%m-%d %H:%M:%S').date()
        self.testDay = Label(self.ID, text=("Test Date: {0}".format(self.DateOfTest)), font=('Lato', 11))
        self.testDay.place(x=240, y=270)

        self.status = Label(self.ID, text=("Patient Status: {0}".format(citySheet.cell(row=PatientRow,
                                                                                column=7).value)), font=('Lato', 11))
        self.status.place(x=240, y=315)

        self.Quaran = Label(self.ID, text=("In Quarantine? : {0}".format(citySheet.cell(row=PatientRow,
                                                                                column=8).value)), font=('Lato', 11))
        self.Quaran.place(x=240, y=360)

        self.WhereQuaran = Label(self.ID, text=("Where In Quarantine? : {0}".format(citySheet.cell(row=PatientRow,
                                                                                column=9).value)), font=('Lato', 11))
        self.WhereQuaran.place(x=240, y=405)

    def ReportByName(self):
        citySheet = Database.Covid19DB[self.SelectedCity.get()]
        first_name = self.FirstName.get()
        last_name = self.LastName.get()
        PatientRow = None
        for rw in range(2, 28):
            if citySheet.cell(row=rw, column=1).value == first_name and citySheet.cell(row=rw,
                                                                                       column=2).value == last_name:
                PatientRow = rw
        if PatientRow == None:
            self.NoPatient = Label(self.Name, text="Patient with such id do not exist in the system!").place(x=500,
                                                                                                             y=500)
            return 1

        self.firstname = Label(self.Name, text=("Firstname:", citySheet.cell(row=PatientRow,
                                                                             column=1).value), font=('Lato', 11))
        self.firstname.place(x=240, y=45)

        self.lastname = Label(self.Name, text=("Lastname:", citySheet.cell(row=PatientRow,
                                                                           column=2).value), font=('Lato', 11))
        self.lastname.place(x=240, y=90)

        self.sex = Label(self.Name, text=("Sex:", citySheet.cell(row=PatientRow, column=3).value), font=('Lato', 11))
        self.sex.place(x=240, y=135)

        self.id = Label(self.Name, text=("ID:", citySheet.cell(row=PatientRow, column=4).value), font=('Lato', 11))
        self.id.place(x=240, y=180)

        self.DateOfBirth = date
        self.DateOfBirth = datetime.strptime(str(citySheet.cell(row=PatientRow,
                                                                column=5).value), '%Y-%m-%d %H:%M:%S').date()
        self.bDay = Label(self.Name, text=("Date of birth: {0}".format(self.DateOfBirth)), font=('Lato', 11))
        self.bDay.place(x=240, y=225)

        self.DateOfTest = date
        self.DateOfTest = datetime.strptime(str(citySheet.cell(row=PatientRow,
                                                               column=6).value), '%Y-%m-%d %H:%M:%S').date()
        self.testDay = Label(self.Name, text=("Test Date: {0}".format(self.DateOfTest)), font=('Lato', 11))
        self.testDay.place(x=240, y=270)

        self.status = Label(self.Name, text=("Patient Status: {0}".format(citySheet.cell(row=PatientRow,
                                                                                column=7).value)), font=('Lato', 11))
        self.status.place(x=240, y=315)

        self.Quaran = Label(self.Name, text=("In Quarantine? : {0}".format(citySheet.cell(row=PatientRow,
                                                                                column=8).value)), font=('Lato', 11))
        self.Quaran.place(x=240, y=360)

        self.WhereQuaran = Label(self.Name,
                                 text=("Where In Quarantine? : {0}".format(citySheet.cell(row=PatientRow,
                                                                                column=9).value)), font=('Lato', 11))
        self.WhereQuaran.place(x=240, y=405)


# Reports = ReportsPage()
# Reports.mainloop()
