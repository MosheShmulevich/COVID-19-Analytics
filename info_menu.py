import docx2txt


def menu():
    print("Welcome to the information menu.")
    print("Choose the option you need:")
    print("Enter 1 for information about COVID 19")
    print("Enter 2 for information about the importance of COVID 19 guidelines")
    print("Enter 3 for information about the COVID 19 vaccination")
    print("Enter 4 for information about the effect of the COVID 19 on the mental health")
    print("Enter 5 for information blood donation for covid 19 patients")
    print("Enter 6 for information about professional help of any kind")
    print("Enter 7 for information about this system")
    print("Enter 8 for information about the developer company")
    print("Enter 9 to exit")
    choice = int(input())

    if choice == 1:
        my_text = docx2txt.process("COVID19info.docx")
        print(my_text)
        print("if you want to exit the menu enter 0,if not press 1")
        choice2 = int(input())
        if choice2 == 0:
            exit()
        else:
            menu()

    if choice == 2:
        my_text = docx2txt.process("COVID19guidelines.docx")
        print(my_text)
        print("if you want to exit the menu enter 0,if not press 1")
        choice2 = int(input())
        if choice2 == 0:
            exit()
        else:
            menu()

    if choice == 3:
        my_text = docx2txt.process("COVID19vaccine.docx")
        print(my_text)
        print("if you want to exit the menu enter 0,if not press 1")
        choice2 = int(input())
        if choice2 == 0:
            exit()
        else:
            menu()

    if choice == 4:
        my_text = docx2txt.process("COVID19MentalHealth.docx")
        print(my_text)
        print("if you want to exit the menu enter 0,if not press 1")
        choice2 = int(input())
        if choice2 == 0:
            exit()
        else:
            menu()

    if choice == 5:
        my_text = docx2txt.process("COVIDBloodDonation.docx")
        print(my_text)
        print("if you want to exit the menu enter 0,if not press 1")
        choice2 = int(input())
        if choice2 == 0:
            exit()
        else:
            menu()

    if choice == 6:
        my_text = docx2txt.process("Professional_help.docx")
        print(my_text)
        print("if you want to exit the menu enter 0,if not press 1")
        choice2 = int(input())
        if choice2 == 0:
            exit()
        else:
            menu()

    if choice == 7:
        my_text = docx2txt.process("system.docx")
        print(my_text)
        print("if you want to exit the menu enter 0,if not press 1")
        choice2 = int(input())
        if choice2 == 0:
            exit()
        else:
            menu()

    if choice == 8:
        my_text = docx2txt.process("Project35Company.docx")
        print(my_text)
        print("if you want to exit the menu enter 0,if not press 1")
        choice2 = int(input())
        if choice2 == 0:
            exit()
        else:
            menu()

    if choice == 9:
        exit()
    else:
        print("Wrong choice, try again!")
        menu()


menu()









