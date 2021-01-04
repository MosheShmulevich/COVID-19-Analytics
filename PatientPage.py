from tkinter import *
from tkinter import ttk
import Database
import pygame



class PatientPage(Tk):
    def __init__(self):
        super(PatientPage, self).__init__()
        self.title("Patient Information")
        self.geometry("1000x600")
        self.minsize(1000, 600)
        self.maxsize(1000, 600)
        self.MakeTabs()
        self.MakeLabels()
        self.MakeInterface()

    def MakeTabs(self):
        self.Tab_control = ttk.Notebook(self)

        self.MainTab = ttk.Frame(self.Tab_control)
        self.Tab_control.add(self.MainTab, text="Patient Data")

        self.MessagesTab = ttk.Frame(self.Tab_control)
        self.Tab_control.add(self.MessagesTab, text="Messages for patient")

        self.Tab_control.pack(expan=1, fill="both")

    def MakeLabels(self):
        ######################## Main Tab ###########################
        self.Firstname_Label = Label(self.MainTab, text="Firstname:")
        self.Firstname_Label.place(x=50, y=15)
        self.Firstname_Label.configure(font=('Lato', 12, "bold"))

        self.Lastname_Label = Label(self.MainTab, text="Lastname:")
        self.Lastname_Label.place(x=50, y=70)
        self.Lastname_Label.configure(font=('Lato', 12, "bold"))

        self.Sex_Label = Label(self.MainTab, text="Sex:")
        self.Sex_Label.place(x=50, y=125)
        self.Sex_Label.configure(font=('Lato', 12, "bold"))

        self.ID_Label = Label(self.MainTab, text="ID:")
        self.ID_Label.place(x=50, y=180)
        self.ID_Label.configure(font=('Lato', 12, "bold"))

        self.bDay_Label = Label(self.MainTab, text="Date of birth:")
        self.bDay_Label.place(x=50, y=235)
        self.bDay_Label.configure(font=('Lato', 12, "bold"))

        self.tDate_Label = Label(self.MainTab, text="Date of test:")
        self.tDate_Label.place(x=50, y=290)
        self.tDate_Label.configure(font=('Lato', 12, "bold"))

        self.Status_Label = Label(self.MainTab, text="Patient's Status:")
        self.Status_Label.place(x=50, y=345)
        self.Status_Label.configure(font=('Lato', 12, "bold"))

        self.Quaran_Label = Label(self.MainTab, text="In quarantine?:")
        self.Quaran_Label.place(x=50, y=400)
        self.Quaran_Label.configure(font=('Lato', 12, "bold"))

        self.WhereQuaran_Label = Label(self.MainTab, text="Where in quarantine?:")
        self.WhereQuaran_Label.place(x=50, y=455)
        self.WhereQuaran_Label.configure(font=('Lato', 12, "bold"))

        self.Notes_Label = Label(self.MainTab, text="Patient's notes")
        self.Notes_Label.place(x=500, y=200)
        self.Notes_Label.configure(font=('Lato', 12, "bold"))

        self.CityLabel = Label(self.MainTab, text="Select Patient's City:")
        self.CityLabel.configure(font=('Lato', 11, "bold"))
        self.CityLabel.place(x=445, y=13)

        self.EnterIdLabel = Label(self.MainTab, text="Enter Patient's ID:")
        self.EnterIdLabel.configure(font=('Lato', 11, "bold"))
        self.EnterIdLabel.place(x=463, y=43)
        #############################################################

        ###################### Messages Tab #########################
        #### Variables ####
        self.Name = StringVar()
        self.Phone = StringVar()
        #################
        self.name = Label(self.MessagesTab, text="Name:")
        self.name.configure(font=("Arial", 11, 'bold'))
        self.name.place(x=15, y=20)

        self.nameEntry = ttk.Entry(self.MessagesTab, width=25, textvariable=self.Name)
        self.nameEntry.place(x=19, y=45)

        self.phone = Label(self.MessagesTab, text="Phone number:")
        self.phone.configure(font=("Arial", 11, 'bold'))
        self.phone.place(x=15, y=70)

        self.phoneEntry = ttk.Entry(self.MessagesTab, width=25, textvariable=self.Phone)
        self.phoneEntry.place(x=19, y=95)

        self.messageLabel = Label(self.MessagesTab, text="Message:")
        self.messageLabel.configure(font=("Arial", 11, 'bold'))
        self.messageLabel.place(x=15, y=140)

        self.message = Text(self.MessagesTab)
        self.message.place(x=19, y=165, width=400, height=300)
        self.message.configure(font=('Arial', 12))

        self.PostButton = ttk.Button(self.MessagesTab, width=16, text="Send message")
        self.PostButton.place(x=19, y=480)
    def MakeInterface(self):
        ######################## Main Tab ###########################
        #### Variables ####
        self.City = StringVar()
        self.ID = IntVar()
        ###################
        self.CityCombo = ttk.Combobox(self.MainTab, width=10, textvariable=self.City)
        self.CityCombo.place(x=600, y=15)
        self.CityCombo['values'] = Database.Covid19DB.sheetnames[1:99]

        self.CitySelect = ttk.Button(self.MainTab, text="Select", width=8, command=self.get_Data)
        self.CitySelect.place(x=690, y=13)

        self.IdEntry = ttk.Entry(self.MainTab, width=15, textvariable=self.ID)
        self.IdEntry.place(x=600, y=45)

        self.PatientNotes = Text(self.MainTab, state=NORMAL)
        self.PatientNotes.place(x=500, y=230, width=400, height=240)

        self.EditNotes = Button(self.MainTab, width=9, text="Edit", command=self.edit)
        self.EditNotes.place(x=910, y=230)

        self.SaveNotes = Button(self.MainTab, width=9, text="Save", command=self.save)
        self.SaveNotes.place(x=910, y=260)
        #############################################################

    def get_Data(self):
        citySheet = Database.Covid19DB[self.City.get()]
        ID = self.ID.get()
        self.Row = None
        Text = "Patient with id {0} doesn't exist in the city database".format(ID)
        self.Error = Label(self.MainTab, text=Text)
        for ROW in range(1, 28):
            if citySheet.cell(row=ROW, column=4).value == ID:
                self.Row = ROW
        if self.Row == None:
            self.Error.place(x=300, y=70)
            self.Error.configure(font=('Lato', 11, 'bold'))
            return -1
        self.Error.destroy()
        self.firstname = Label(self.MainTab, text=citySheet.cell(row=self.Row, column=1).value)
        self.firstname.place(x=50, y=40)
        self.firstname.configure(font=('Lato', 11))

        self.lastname = Label(self.MainTab, text=citySheet.cell(row=self.Row, column=2).value)
        self.lastname.place(x=50, y=95)
        self.lastname.configure(font=('Lato', 11))

        self.sex = Label(self.MainTab, text=citySheet.cell(row=self.Row, column=3).value)
        self.sex.place(x=50, y=150)
        self.sex.configure(font=('Lato', 11))

        self.id = Label(self.MainTab, text=citySheet.cell(row=self.Row, column=4).value)
        self.id.place(x=50, y=205)
        self.id.configure(font=('Lato', 11))

        self.bDay = Label(self.MainTab, text=citySheet.cell(row=self.Row, column=5).value)
        self.bDay.place(x=50, y=260)
        self.bDay.configure(font=('Lato', 11))

        self.tDay = Label(self.MainTab, text=citySheet.cell(row=self.Row, column=6).value)
        self.tDay.place(x=50, y=315)
        self.tDay.configure(font=('Lato', 11))

        self.status = Label(self.MainTab, text=citySheet.cell(row=self.Row, column=7).value)
        self.status.place(x=50, y=370)
        self.status.configure(font=('Lato', 11))

        self.Quaran = Label(self.MainTab, text=citySheet.cell(row=self.Row, column=8).value)
        self.Quaran.place(x=50, y=425)
        self.Quaran.configure(font=('Lato', 11))

        self.WhereQuaran = Label(self.MainTab, text=citySheet.cell(row=self.Row, column=9).value)
        self.WhereQuaran.place(x=50, y=480)
        self.WhereQuaran.configure(font=('Lato', 11))

    def edit(self):
        self.PatientNotes.configure(state=NORMAL)

    def save(self):
        self.PatientNotes.configure(state=DISABLED)
        Save = SaveConfirm()

class SaveConfirm(Tk):
    def __init__(self):
        super(SaveConfirm, self).__init__()
        self.title("Are you sure?")
        self.geometry("250x100")
        self.maxsize(300, 100)
        self.Confirm()

    def Confirm(self):
        pygame.mixer.init()
        pygame.mixer.music.load("ConfirmSoundFX.mp3")    # For fun
        pygame.mixer.music.play()
        self.ConfirmMessage = Label(self, text="Are you sure about that?")
        self.ConfirmMessage.pack(side=TOP)
        self.ConfirmMessage.configure(font=('Lato', 12, 'bold'))

        self.NoButton = ttk.Button(self, text="No", command=self.ReturnNo)
        self.NoButton.pack(side=LEFT)
        self.YesButton = ttk.Button(self, text="Yes", command=self.ReturnYes)
        self.YesButton.pack(side=RIGHT)

    def ReturnYes(self):
        Database.Covid19DB[Page.City.get()].cell(row=Page.Row, column=10).value = Page.PatientNotes.get("1.0", END)
        Database.Covid19DB.save('Database.xlsx')
        self.destroy()

    def ReturnNo(self):
        Page.PatientNotes.configure(state=NORMAL)
        self.destroy()

Page = PatientPage()
Page.mainloop()
