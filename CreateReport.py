from openpyxl import *
import Database


def create_report(city):
    for row in range(2, 100):
        if Database.city_sheet.cell(row=row, column=1).value == city:
            city_row = row
    print("Here are the data for the city:", city)
    for column in range(2, 13):
        print(Database.city_sheet.cell(row=1, column=column).value, "-", Database.city_sheet.cell(row=city_row, column=column).value)
