import Database
from openpyxl import *


def Register():
    userName = input("Username: ")  # Asking the User for Username input
    for row in range(2, 35):
        if userName == Database.userSheet.cell(row=row, column=1):
            print("Already exists, Try something else.")
            Register()
        else:
            continue
    password = input("Password: ")  # Asking the user for their password
