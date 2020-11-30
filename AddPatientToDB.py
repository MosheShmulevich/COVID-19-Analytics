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


def addPatient(New_Patient, city):
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
        for j in range(1, 2):
            if city_sheet.cell(row=row, column=j).value is None:
                for col in range(1, 7):
                    city_sheet.cell(row=row, column=col).value = switch_input(col)[col]
                Database.Covid19DB.save('Database.xlsx')
                break
            else:
                break
        if New_Patient.firstname == city_sheet.cell(row=row, column=1).value:
            break



