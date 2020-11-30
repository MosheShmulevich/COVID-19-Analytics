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

def CreateNewSheet(city):
    def SwitchTitle(column):
        switcher={
            1:'Firstname',
            2:'Lastname',
            3: 'ID',
            4: 'Birth date',
            5:'Test date',
            6:'Patient Status'}
        return switcher

    Database.Covid19DB.create_sheet(city)
    city_sheet = Database.Covid19DB[city]
    for colmn in range(1,7):
        city_sheet.cell(row=1, column=colmn).value =  SwitchTitle(colmn)[colmn]


def addPatient(New_Patient, city):

    if city not in Database.Covid19DB.sheetnames:
        CreateNewSheet(city)


    New_Patient.is_tested=None
    city_sheet = Database.Covid19DB[city]

    def switch_input(k):
        switcher = {
            1: New_Patient.firstname,
            2: New_Patient.lastname,
            3: New_Patient.ID,
            4: New_Patient.birth_date,
            5: New_Patient.test_date,
            6: New_Patient.status
        }
        return switcher

    for row in range(2, 28):
        for j in range(2, 3):
            if city_sheet.cell(row=row, column=j).value is None:
                for col in range(1, 7):
                    city_sheet.cell(row=row, column=col).value = switch_input(col)[col]
                Database.Covid19DB.save('Database.xlsx')
                break
            else:
                break
        if New_Patient.firstname == city_sheet.cell(row=row, column=1).value:
            break



