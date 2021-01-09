from tkinter import *
import AddPatientToDBTkinter
import NotesTkinter
import ReportsTkinter
import RegisterTkinter


class MainPage(Tk):
    def __init__(self):
        super(MainPage, self).__init__()
        self.title("Covid19 Analytics")
        self.geometry("640x480")
        self.resizable(width=False, height=False)
        self.makeButtons()

    def makeButtons(self):
        self.ReportsButton = Button(self, text="Reports", command=self.make_report)
        self.ReportsButton.place(x=120, y=10, width=370, height=60)

        self.AddPatientButton = Button(self, text="Add Patient", command=self.add_patient)
        self.AddPatientButton.place(x=120, y=80, width=370, height=70)

        self.ContactButton = Button(self, text="Contact Us", command=self.note)
        self.ContactButton.place(x=120, y=160, width=370, height=70)

        self.RegisterButton = Button(self, text="Register", command=self.Register)
        self.RegisterButton.place(x=120, y=240, width=370, height=70)

    def make_report(self):
        Report = ReportsTkinter.ReportsPage()
    def add_patient(self):
        Patient = AddPatientToDBTkinter.AddPage()
    def note(self):
        Note = NotesTkinter.NotesPage()
    def Register(self):
        register = RegisterTkinter.RegisterWindow()


Main_Page = MainPage()
Main_Page.mainloop()

