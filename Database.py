from openpyxl import *

Covid19DB = load_workbook(filename='Database.xlsx', data_only=True)  # Covid19 database
MainSheet = Covid19DB['Cities Data']
CityDB = ((load_workbook(filename="Israel city list.xlsx"))['Israel Cities'])['A']  # Israel cities sheet column A
IL_CityList = [CityDB[x].value for x in range(len(CityDB))]

userDb = load_workbook(filename='UserDatabase.xlsx')  # System users database
userSheet = userDb['users']  # UserDatabase users sheet


def InsertListToDB():  # Adding cities from Israel city list.xlsx file as a list
    row = 2
    for city in IL_CityList:
        city_sheet.cell(row=row, column=1).value = city
        row += 1
    Covid19DB.save('Database.xlsx')
