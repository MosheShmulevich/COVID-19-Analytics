import Database


def FindRecovered():
    CitiesSheets = Database.Covid19DB.sheetnames[1:-1:1]

    def CreateNewSheet(city):  # function for creating a new 'city' sheet in xlsx database
        def FormatCells(CitySheet):  # function for formatting the date and id cells according to the data
            for row in range(2, 100):
                for column in range(4, 7):
                    cell = CitySheet.cell(row, column)
                    if column == 5 or column == 6:
                        cell.number_format = "DD-MM-YYYY"
                    elif column == 4:
                        cell.number_format = "0"
            Database.RecoveredDB.save('RecoveredDatabase.xlsx')

        def SwitchTitle(column):  # function for adding to the xlsx table columns, titles
            switcher = {
                1: 'Firstname',
                2: 'Lastname',
                3: 'Sex',
                4: 'ID',
                5: 'Birth date',
                6: 'Test date',
                7: 'Notes'
            }
            return switcher

        FormatCells(Database.RecoveredDB.create_sheet(city))  # creating a new sheet with 'city' name
        citySheet = Database.RecoveredDB[city]  # implementing the 'city' sheet into a variable "city_sheet"
        for colmn in range(1, 8):  # adding to the xlsx table columns, titles
            citySheet.cell(row=1, column=colmn).value = SwitchTitle(colmn)[colmn]
        Database.RecoveredDB.save('RecoveredDatabase.xlsx')

    for City in CitiesSheets:
        for PatientRow in range(2, 400):
            if City not in Database.RecoveredDB.sheetnames:
                CreateNewSheet(City)
            if Database.Covid19DB[City].cell(row=PatientRow, column=7).value == "Recovered":
                RecoveredIDList = []
                CheckRow = 2
                while Database.RecoveredDB[City].cell(row=CheckRow, column=4).value is not None:
                    RecoveredIDList += [Database.RecoveredDB[City].cell(row=CheckRow, column=4).value, ]
                    CheckRow += 1
                print(RecoveredIDList)
                if Database.Covid19DB[City].cell(row=PatientRow, column=4).value in RecoveredIDList:
                    print("Patient already in recovered database!")
                    continue

                NewRecoveredRow = 2
                while Database.RecoveredDB[City].cell(row=NewRecoveredRow, column=1).value is not None:
                    NewRecoveredRow += 1
                for COLUMN in range(1, 11):
                    if COLUMN in (7, 8, 9):
                        continue
                    Database.RecoveredDB[City].cell(row=NewRecoveredRow, column=COLUMN).value = \
                        Database.Covid19DB[City].cell(row=PatientRow, column=COLUMN).value
                print("Recovered patient added to the recovered database!")
                Database.RecoveredDB.save('RecoveredDatabase.xlsx')


FindRecovered()
