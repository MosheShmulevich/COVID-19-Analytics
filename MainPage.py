from tkinter import *

import AddPatientToDBTkinter
import NotesTkinter
import ReportsTkinter
import RegisterTkinter


class MainPage(Tk):
    def __init__(self):
        super(MainPage, self).__init__()
        self.title("Covid19 Analytics")
        self.minsize(640, 480)
        self.makeButtons()

    def makeButtons(self):
        self.ReportsButton = Button(self, text="Reports", command=ReportsTkinter.ReportsPage)
        self.ReportsButton.place(x=120, y=10, width=370, height=60)

        self.AddPatientButton = Button(self, text="Add Patient", command=AddPatientToDBTkinter.AddPage)
        self.AddPatientButton.place(x=120, y=80, width=370, height=70)

        self.ContactButton = Button(self, text="Contact Us", command=NotesTkinter.NotesPage)
        self.ContactButton.place(x=120, y=160, width=370, height=70)

        self.RegisterButton = Button(self, text="Register", command=RegisterTkinter.RegisterWindow)
        self.RegisterButton.place(x=120, y=240, width=370, height=70)


Page = MainPage()
Page.mainloop()

