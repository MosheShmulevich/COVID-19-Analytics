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


def addPatient(New_Patient, city):
    city_sheet = Database.db[city]

    def switch_input(k):
        switcher = {
            1: New_Patient.firstname,
            2: New_Patient.lastname,
            3: New_Patient.ID,
            4: New_Patient.birth_date,
            5: New_Patient.test_date,
            6: New_Patient.test_result
        }
        return switcher

    for row in range(2, 28):
        for j in range(1, 2):
            if city_sheet.cell(row=row, column=j).value is None:
                for col in range(1, 7):
                    city_sheet.cell(row=row, column=col).value = switch_input(col)[col]
                break
            else:
                break
        if New_Patient.firstname == city_sheet.cell(row=row, column=1).value:
            break

addPatient(New_Patient("Mike", "lasto", 546827551, datetime.strptime("1995/11/25", "%Y/%m/%d"),
                       datetime.strptime("2020/07/25", "%Y/%m/%d"), "Positive"), "Beer Sheva")
addPatient(New_Patient("Moshe", "Shmulevich", 315541367, datetime.strptime("12/02/1996", "%d/%m/%Y"),
                       datetime.strptime("30/10/2020", "%d/%m/%Y"), "Negative"), "Beer Sheva")
Database.db.save('Database.xlsx')
