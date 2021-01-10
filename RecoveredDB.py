import Database


def FindRecovered():
    CitiesSheets = Database.Covid19DB.sheetnames[1:]
    print(CitiesSheets)
    def CreateNewSheet(city):  # function for creating a new 'city' sheet in xlsx database
        def FormatCells(CitySheet):  # function for formatting the date and id cells according to the data
            for row in range(2, 100):
                for column in range(4, 7):
                    cell = CitySheet.cell(row, column)
                    if column == 6 or column == 7:
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
                5: 'Occupation',
                6: 'Birth date',
                7: 'Test date',
                8: 'Notes',
                9: 'Email'
            }
            return switcher

        FormatCells(Database.RecoveredDB.create_sheet(city))  # creating a new sheet with 'city' name
        citySheet = Database.RecoveredDB[city]  # implementing the 'city' sheet into a variable "city_sheet"
        for colmn in range(1, 10):  # adding titles to the xlsx table columns
            citySheet.cell(row=1, column=colmn).value = SwitchTitle(colmn)[colmn]
        Database.RecoveredDB.save('RecoveredDatabase.xlsx')

    for City in CitiesSheets:
        for PatientRow in range(2, 400):
            if City not in Database.RecoveredDB.sheetnames:
                CreateNewSheet(City)
            if Database.Covid19DB[City].cell(row=PatientRow, column=8).value == "Recovered":
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
                RecoveredColumn = 1
                for MAINCOLUMN in range(1, 13):
                    if MAINCOLUMN in (8, 9, 10):
                        continue
                    Database.RecoveredDB[City].cell(row=NewRecoveredRow, column=RecoveredColumn).value = \
                        Database.Covid19DB[City].cell(row=PatientRow, column=MAINCOLUMN).value
                    RecoveredColumn += 1
                print("Recovered patient added to the recovered database!")
                Database.RecoveredDB.save('RecoveredDatabase.xlsx')


FindRecovered()
