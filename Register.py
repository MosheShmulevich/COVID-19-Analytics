import Database


def Register():
    userName = input("Username: ")  # Asking the User for Username input
    for row in range(2, 35):
        if userName == Database.userSheet.cell(row=row, column=1):
            print("Username already exists, Try something else")
            Register()
        else:
            continue
    password = input("Password: ")  # Asking the user for their password
    email = input("Email: ")  # Asking the user for their email
    for row in range(2, 35):
        if email == Database.userSheet.cell(row=row, column=3):
            print("Email already exists, Try something else")
            Register()
        else:
            continue
    for row in range(2, 35):
        for column in range(1, 2):
            if Database.userSheet.cell(row=row, column=column).value is None:
                Database.userSheet.cell(row=row, column=1).value = userName
                Database.userSheet.cell(row=row, column=2).value = password
                Database.userSheet.cell(row=row, column=3).value = email
                Database.userDb.save('UserDatabase.xlsx')
                print("Thank you for your registration!")
                return 1
            else:
                continue


def CleanUserData(username):
    userRow = 0
    for row in range(2, 35):
        if username == Database.userSheet.cell(row=row, column=1).value:
            userRow = row
            break
        else:
            print("username doesn't exist!")
            return 0
    for column in range(1, 4):
        Database.userSheet.cell(row=userRow, column=column).value = None
    Database.userDb.save('UserDatabase.xlsx')
    return 1


CleanUserData("MaxShap")
