import Database
from dataclasses import dataclass
from datetime import *
import openpyxl

@dataclass()
class Searching_Patient:
    firstname: str
    lastname: str
    ID: int
    birth_date: datetime
    test_date: datetime
    test_result: str
    is_tested: str
    status: str

    print("through which function would you like to sort?"
          "1: 'Firstname'"
          "2: 'Lastname'"
          "3: 'ID'"
          "4: 'Birth date'"
          "5: 'Test date'"
          "6: 'Patient Status'")

Sorting_option =input ("choose your searching option")
if(Sorting_option>=1 and Sorting_option<=6):
    def SwitchTitle(Sorting_option):  # function to help sorting out information.
        switcher = {
            1: 'Firstname',
            2: 'Lastname',
            3: 'ID',
            4: 'Birth date',
            5: 'Test date',
            6: 'Patient Status'}
        return switcher

    def switch_input(k):  # function to choose patient's parameters
        switcher = {
            1: Searching_Patient.firstname,
            2: Searching_Patient.lastname,
            3: Searching_Patient.ID,
            4: Searching_Patient.birth_date,
            5: Searching_Patient.test_date,
            6: Searching_Patient.status
        }
        return switcher

    print("through which function would you like to sort?"
          "1: 'Firstname'"
          "2: 'Lastname'"
          "3: 'ID'"
          "4: 'Birth date'"
          "5: 'Test date'"
          "6: 'Patient Status'")

Sheet.cell(row='Row_Name', column='Column_Name').value
Sorting_option =input ("choose your searching option")
if(Sorting_option>=1 and Sorting_option<=6):
   x=SwitchTitle(Sorting_option)
   x2=switch_input(Sorting_option)
    while (Sheet.cell(row='Row_Name', column='Column_Name').value)!=None:
        Row=Row+1
        print(x2)
else:
 print("Wrong answer!")
