import Database
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image



class RegisterWindow(Tk):
    def __init__(self):
        super(RegisterWindow, self).__init__()
        self.title("User Registration Page")
        self.geometry("450x300")
        self.wm_iconbitmap("Logo.ico")
        self.configure(bg='goldenrod')
        self.create_UsertextBox()

    def create_UsertextBox(self):
        self.username = StringVar()
        self.password = StringVar()
        self.email = StringVar()

        self.IMG = ImageTk.PhotoImage(Image.open("Logo.jpg"))
        self.Label = Label(image=self.IMG, bg="goldenrod")
        self.Label.pack()



        self.label_user = ttk.Label(self, text="Username: ")
        self.label_user.pack()
        self.label_user.configure(background='goldenrod')

        self.user = ttk.Entry(self, width=20, textvariable=self.username)
        self.user.pack()
        self.user.focus()

        self.label_pswrd = ttk.Label(self, text="Password: ")
        self.label_pswrd.pack()
        self.label_pswrd.configure(background='goldenrod')

        self.pswrd = ttk.Entry(self, width=20, textvariable=self.password)
        self.pswrd.pack()

        self.label_email = ttk.Label(self, text="Email: ")
        self.label_email.pack()
        self.label_email.configure(background='goldenrod')

        self.Email = ttk.Entry(self, width=20, textvariable=self.email)
        self.Email.pack()

        self.button = ttk.Button(self, text="Sign up", command=self.Register)
        self.button.pack()

        self.Message = Label(self, text='')
        self.Message.pack()
        self.Message.configure(background='goldenrod')


    def Register(self):
        TryCounter = 0
        for row in range(2, 35):
            if self.username.get() == Database.userSheet.cell(row=row, column=1).value:
                TryCounter += 1
                self.Message.configure(text="This user name already exist\nlog-in or choose a different "
                                            "username")
            else:
                continue
        for row in range(2, 35):
            if self.email.get() == Database.userSheet.cell(row=row, column=3).value:
                TryCounter += 1
                self.Message.configure(text="This email already exist\nlog-in or choose a different "
                                            "email")
            else:
                continue
        if TryCounter >=2:
            self.Message.configure(text="Too many tries,closing the registration page")
            exit(-1)
        else:
            for row in range(2, 35):
                for column in range(1, 2):
                    if Database.userSheet.cell(row=row, column=column).value is None:
                        Database.userSheet.cell(row=row, column=1).value = self.username.get()
                        Database.userSheet.cell(row=row, column=2).value = self.password.get()
                        Database.userSheet.cell(row=row, column=3).value = self.email.get()
                        Database.userDb.save('UserDatabase.xlsx')
                        self.Message = ttk.Label(self, text="Thank you for your registration!")
                        self.Message.pack()
                        return 1
                    else:
                        continue


# Register_Window = RegisterWindow()
# Register_Window.mainloop()
