import Database
from tkinter import *
from tkinter import ttk
from datetime import *


class AddPage(Tk):
    def __init__(self):
        super(AddPage, self).__init__()
        self.title("Add patient to the Database")
        self.minsize(480, 260)
        # self.wm_iconbitmap("")
        self.create_tabs()
        self.add_widgets()

    def create_tabs(self):
        self.tab_control = ttk.Notebook(self)
        self.Tab1 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.Tab1, text="Add Patient")
        self.tab_control.pack(expan=1, fill="both")

    def add_widgets(self):
        ### Add Patient Tab ###
        self.City = StringVar()
        self.First_Name = StringVar()
        self.Last_Name = StringVar()
        self.Sex = StringVar()
        self.ID = IntVar()

        self.birth_Day = IntVar()
        self.birth_Month = IntVar()
        self.birth_Year = IntVar()
        self.BirthDate = StringVar()

        self.Test_Day = IntVar()
        self.Test_Month = IntVar()
        self.Test_Year = IntVar()
        self.TestDate = StringVar()

        self.PatientStatus = StringVar()
        self.Quarantined = StringVar()
        self.WhereQuarntined = StringVar()

        self.Message = Label(self.Tab1, text="Fill the following information of the patient"
                                             " to enter a patient into the database").grid(row=0, column=0,
                                                                                           columnspan=5)

        self.city = Label(self.Tab1, text="City").grid(row=1, column=0)
        self.CityEntry = ttk.Entry(self.Tab1, width=25, textvariable=self.City).grid(row=1, column=1)

        self.FirstName = Label(self.Tab1, text="First Name").grid(row=2, column=0)  # FirstName Label
        self.first_name = ttk.Entry(self.Tab1, width=20, textvariable=self.First_Name).grid(row=2,
                                                                                            column=1)  # FirstName TextBox

        self.LastName = Label(self.Tab1, text="Last Name").grid(row=3, column=0)  # LastName Label
        self.last_name = ttk.Entry(self.Tab1, width=20, textvariable=self.Last_Name).grid(row=3,
                                                                                          column=1)  # LastName TextBox

        self.sex = Label(self.Tab1, text="Sex:").grid(row=4, column=0)
        self.sexCombo = ttk.Combobox(self.Tab1, width=7, textvariable=self.Sex)
        self.sexCombo.grid(row=4, column=1)
        self.sexCombo['values'] = ('Male', 'Female')

        self.id = Label(self.Tab1, text="ID").grid(row=5, column=0)  # ID Label
        self.iD = ttk.Entry(self.Tab1, width=20, textvariable=self.ID).grid(row=5, column=1)  # ID TextBox

        self.Birthday = Label(self.Tab1, text="Date of Birth").grid(row=7, column=0)  # Birthday Label
        self.B_Day = ttk.Combobox(self.Tab1, width=4, textvariable=self.birth_Day)  # Day entry
        self.B_Day.grid(row=7, column=1)
        self.B_Day.set("Day")
        self.B_Day['values'] = tuple(range(1, 32))  # Day options
        self.B_Month = ttk.Combobox(self.Tab1, width=8, textvariable=self.birth_Month)
        self.B_Month.grid(row=7, column=2)
        self.B_Month.set("Month")
        self.B_Month['values'] = tuple(range(1, 13))
        self.B_Year = ttk.Combobox(self.Tab1, width=10, textvariable=self.birth_Year)
        self.B_Year.grid(row=7, column=4)
        self.B_Year.set("Year")
        self.B_Year['values'] = tuple(range(1900, 2021))

        self.TestDay = Label(self.Tab1, text="Test Date").grid(row=9, column=0)  # Birthday Label
        self.T_Day = ttk.Combobox(self.Tab1, width=4, textvariable=self.Test_Day)  # Day entry
        self.T_Day.set("Day")
        self.T_Day.grid(row=9, column=1)
        self.T_Day['values'] = tuple(range(1, 32))  # Day options
        self.T_Month = ttk.Combobox(self.Tab1, width=8, textvariable=self.Test_Month)
        self.T_Month.grid(row=9, column=2)
        self.T_Month.set("Month")
        self.T_Month['values'] = tuple(range(1, 13))
        self.T_Year = ttk.Combobox(self.Tab1, width=10, textvariable=self.Test_Year)
        self.T_Year.grid(row=9, column=4)
        self.T_Year.set("Year")
        self.T_Year['values'] = tuple(range(2019, 2022))

        self.Status = Label(self.Tab1, text="What's the patient status?").grid(row=10, column=0)
        self.status = ttk.Combobox(self.Tab1, width=8, textvariable=self.PatientStatus)
        self.status.grid(row=10, column=1)
        self.status['values'] = ("Active", "Recovered", "Dead", "Immunized")

        self.quarantine = Label(self.Tab1, text="Is the patient in quarantine?").grid(row=11, column=0, columnspan=1)
        self.Quarn = ttk.Combobox(self.Tab1, width=6, textvariable=self.Quarantined)
        self.Quarn.grid(row=11, column=1, columnspan=1)
        self.Quarn['values'] = ("Yes", "No")
        self.confirm = Button(self.Tab1, text="Confirm", command=self.enable)
        self.confirm.grid(row=11, column=2)

        self.add_patient = Button(self.Tab1, text='Add Patient', command=self.AssignData)
        self.add_patient.grid(row=13, column=4)

        self.Location = Label(self.Tab1, text="Where is the patient quarantined?")
        self.Location.grid(row=12, column=0)
        self.QuarantineHome = Radiobutton(self.Tab1, text="Home", value="Home", variable=self.WhereQuarntined,
                                          state=DISABLED)
        self.QuarantineHome.grid(row=12, column=0, columnspan=5)
        self.QuarantineHotel = Radiobutton(self.Tab1, text="Hotel", value="Hotel", variable=self.WhereQuarntined,
                                           state=DISABLED)
        self.QuarantineHotel.grid(row=12, column=1, columnspan=5)
        self.QuarantineHospital = Radiobutton(self.Tab1, text="Hospital", value="Hospital",
                                              variable=self.WhereQuarntined, state=DISABLED)
        self.QuarantineHospital.grid(row=12, column=2, columnspan=5)
        ############################

    def enable(self):
        if self.Quarn.get() == "Yes":
            self.QuarantineHome.configure(state=NORMAL)
            self.QuarantineHotel.configure(state=NORMAL)
            self.QuarantineHospital.configure(state=NORMAL)
        else:
            self.QuarantineHome.configure(state=DISABLED)
            self.QuarantineHotel.configure(state=DISABLED)
            self.QuarantineHospital.configure(state=DISABLED)

    def AssignData(self):
        self.BirthDate = datetime.strptime((str(self.birth_Day.get()) + "/" + str(self.birth_Month.get()) + "/" +
                                            str(self.birth_Year.get())), "%d/%m/%Y")
        self.TestDate = datetime.strptime((str(self.Test_Day.get()) + "/" + str(self.Test_Month.get()) + "/" +
                                           str(self.Test_Year.get())), "%d/%m/%Y")

        def CreateNewSheet(city):  # function for creating a new 'city' sheet in xlsx database
            def FormatCells(city_sheet):  # function for formatting the date and id cells according to the data
                for row in range(2, 28):
                    for column in range(4, 7):
                        cell = city_sheet.cell(row, column)
                        if column == 5 or column == 6:
                            cell.number_format = "DD-MM-YYYY"
                        elif column == 4:
                            cell.number_format = "0"
                Database.Covid19DB.save('Database.xlsx')

            def SwitchTitle(column):  # function for adding to the xlsx table columns, titles
                switcher = {
                    1: 'Firstname',
                    2: 'Lastname',
                    3: 'Sex',
                    4: 'ID',
                    5: 'Birth date',
                    6: 'Test date',
                    7: 'Patient Status',
                    8: 'Quarantined',
                    9: 'Where quarantined'
                }
                return switcher

            FormatCells(Database.Covid19DB.create_sheet(city))  # creating a new sheet with 'city' name
            citySheet = Database.Covid19DB[city]  # implementing the 'city' sheet into a variable "city_sheet"
            for colmn in range(1, 9):  # adding to the xlsx table columns, titles
                citySheet.cell(row=1, column=colmn).value = SwitchTitle(colmn)[colmn]

        def switch_input(k):  # function to choose patient's parameters
            switcher = {
                1: self.First_Name.get(),
                2: self.Last_Name.get(),
                3: self.Sex.get(),
                4: self.ID.get(),
                5: self.BirthDate,
                6: self.TestDate,
                7: self.PatientStatus.get(),
                8: self.Quarantined.get(),
                9: self.WhereQuarntined.get()
            }
            return switcher

        if self.City.get() not in Database.Covid19DB.sheetnames:  # if there is no 'city' sheet , calls a function to
            # create one
            CreateNewSheet(self.City.get())
        citySheet = Database.Covid19DB[self.City.get()]
        for row in range(2, 28):  # starts from row#2 because #1 is titles and end in #27(temporarily)
            for j in range(1, 2):  # start in column#1 to check if its empty
                if citySheet.cell(row=row, column=j).value is None:
                    for col in range(1, 10):  # adding patient parameters into the empty row by columns
                        citySheet.cell(row=row, column=col).value = switch_input(col)[col]
                    Database.Covid19DB.save(
                        'Database.xlsx')  # after adding parameters,the system "autosaves" the xlsx file
                    self.Success = Label(self.Tab1, text="Patient Added!").grid(row=13, column=0)
                    print("Patient added!")
                    return 0


PatientAdd = AddPage()
PatientAdd.mainloop()
