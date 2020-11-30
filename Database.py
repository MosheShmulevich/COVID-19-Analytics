from openpyxl import *

Covid19DB = load_workbook(filename='Database.xlsx')
CityDB = ((load_workbook(filename="Israel city list.xlsx"))['Israel Cities'])['A']
IL_CityList = [CityDB[x].value for x in range(len(CityDB))]
