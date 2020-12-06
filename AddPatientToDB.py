from pip._vendor.distlib.compat import raw_input
import Database
from dataclasses import dataclass
from datetime import *


@dataclass()
class New_Patient:
    firstname: str
    lastname: str
    ID: int
    birth_date: datetime
    test_date: datetime
    test_result: str
    is_tested: str
    status: str
    is_quarantined: str
    where_quarantined: str


def CreateNewSheet(city):  # function for creating a new 'city' sheet in xlsx database
    def FormatCells(city_sheet):  # function for formatting the date and id cells according to the data
        for row in range(2, 28):
            for column in range(3, 6):
                cell = city_sheet.cell(row, column)
                if column == 4 or column == 5:
                    cell.number_format = "DD-MM-YYYY"
                elif column == 3:
                    cell.number_format = "0"
        Database.Covid19DB.save('Database.xlsx')

    def SwitchTitle(column):  # function for adding to the xlsx table columns, titles
        switcher = {
            1: 'Firstname',
            2: 'Lastname',
            3: 'ID',
            4: 'Birth date',
            5: 'Test date',
            6: 'Patient Status',
            7: 'Quarantined',
            8: 'Where quarantined'
        }
        return switcher

    FormatCells(Database.Covid19DB.create_sheet(city) ) # creating a new sheet with 'city' name
    city_sheet = Database.Covid19DB[city]  # implementing the 'city' sheet into a variable "city_sheet"
    for colmn in range(1, 9):  # adding to the xlsx table columns, titles
        city_sheet.cell(row=1, column=colmn).value = SwitchTitle(colmn)[colmn]


def addPatient(New_Patient, city):  # function for adding a patient to the 'city' sheet
    if city not in Database.Covid19DB.sheetnames:  # if there is no 'city' sheet , calls a function to create one
        CreateNewSheet(city)

    New_Patient.is_tested = None
    city_sheet = Database.Covid19DB[city]

    def switch_input(k):  # function to choose patient's parameters
        switcher = {
            1: New_Patient.firstname,
            2: New_Patient.lastname,
            3: New_Patient.ID,
            4: datetime.strptime(str(New_Patient.birth_date), "%d/%m/%Y"),
            5: datetime.strptime(str(New_Patient.test_date), "%d/%m/%Y"),
            6: New_Patient.status,
            7: New_Patient.is_quarantined,
            8: New_Patient.where_quarantined
        }
        return switcher

    for row in range(2, 28):  # starts from row#2 because #1 is titles and end in #27(temporarily)
        for j in range(1, 2):  # start in column#1 to check if its empty
            if city_sheet.cell(row=row, column=j).value is None:
                for col in range(1, 9):  # adding patient parameters into the empty row by columns
                    city_sheet.cell(row=row, column=col).value = switch_input(col)[col]
                Database.Covid19DB.save('Database.xlsx')  # after adding parameters,the system "autosaves" the xlsx file
                print("Patient added!")
                return 0
            else:
                continue


def DateCheck(option):
    if option == 0:
        year = int(input("Year of birth: "))
        if year < 1900 or year > 2021:
            exit("Invalid Value!")
        month = int(input("Month of birth: "))
        if month < 1 or month > 12:
            exit("Invalid Value!")
        day = int(input("Day of birth: "))
        if month == 2:
            if day < 1 or day > 29:
                exit("Invalid Value!")
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            if day < 1 or day > 31:
                exit("Invalid Value!")
        if month == 4 or month == 6 or month == 9 or month == 11:
            if day < 1 or day > 30:
                exit("Invalid Value!")
        return datetime.strptime((str(day), "/", str(month), "/", str(year)), "%d/%m/%Y")
    else:
        year = int(input("year tested in: "))
        if year < 2019 or year > 2022:
            exit("Invalid Value!")
        month = int(input("Test month: "))
        if month < 1 or month > 12:
            exit("Invalid Value!")
        day = int(input("Test day: "))
        if month == 2:
            if day < 1 or day > 29:
                exit("Invalid Value!")
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            if day < 1 or day > 31:
                exit("Invalid Value!")
        if month == 4 or month == 6 or month == 9 or month == 11:
            if day < 1 or day > 30:
                exit("Invalid Value!")
        return datetime.strptime((str(day), "/", str(month), "/", str(year)), "%d/%m/%Y")


def InputNewPatient():
    firstname = input("Patient's firstname: ")
    lastname = input("Patient's lastname: ")
    id = int(input("Patient's id: "))
    birthday = DateCheck(0)
    TestDate = DateCheck(1)
    Status = input("What's the patient's status? (Active/Recovered)")
    TestResult = "Positive"
    IsTested = "Yes"
    IsQuarantined = str(input("Is the patient is in quarantine: "))
    WhereQuar = str(input("Where the patient is in quarantine: "))
    city = str(input("Where is the patient live?"))
    addPatient(New_Patient(firstname, lastname, id, birthday, TestDate, TestResult, IsTested, Status,
                           IsQuarantined, WhereQuar), city)
