from tkinter import *
from openpyxl import *

Patients_Details=load_workbook(filename='Patients_Details.xlsx',data_only=True)

class Statistic_Window(Tk):
    def __init__(self):
        super(Statistic_Window,self).__init__()
        self.title("Statistic Analysis")
        self.geometry("1000x500")
        self.minsize(1000,500)
        self.maxsize(1000,500)
        self.ComboBox_Statistic()
        self.configure(background="spring green")

################### create text box where the patient's details will be written.

    def text_box(self):
        text_=Text(self,width=100,height=400,)
        Text.pack(pady=20)
        button_frame=Frame(self)
        button_frame.pack()

        clear_button=Button(button_frame,text='Clear')
        clear_button.grid(row=0,column=0)
    ##############
    def close_text(self):
        if len(self.data.get("1.0","end-1c"))!=0:
            self.ClearLocation()

################### create options window to choose from.

    def switch(event, clicked):
        First_name = []
        Last_name= []
        ID= []
        Birth_Date= []
        Test_Date= []
        Patient_Status= []


        N=Patients_Details.nrows

        ################### printing the patient's details in the textbox window.

        if clicked.get()=='Firstname':

            for N in range (1,Patients_Details.cell_value(N,0)):
                print(First_name)

        elif clicked.get()=='Last name':
            for N in range (1,Patients_Details.cell_value(N,1)):
                print(Last_name)

        elif clicked.get() == 'ID':
            for N in range (1,Patients_Details.cell_value(N,2)):
                print(ID)

        elif clicked.get() == 'Birth Date':
            for N in range(1,Patients_Details.cell_value(N, 3)):
                print(Birth_Date)

        elif clicked.get() == 'Test Date':
            for N in range (1,Patients_Details.cell_value(N,4)):
                print(Test_Date)

        elif clicked.get() == 'Patient Status':
            for N in range (1,Patients_Details.cell_value(N,5)):
                print(Patient_Status)

    ################### visual integrity,what the consumer will meet when the program runs.

    def ComboBox_Statistic(self):
        options = [
               "First name",
                "Last name",
                "ID",
                "Birth Date",
                "Test Date",
                "Patient Status",
        ]
        clicked=StringVar()
        clicked.set(options[0])

        drop=OptionMenu(Tk.self,clicked,*options,command=Tk.selected)
        drop.pack(pady=20)

        myButton= Button(Tk.self,text="Enter a statistical analysis:\n",command=Tk.selected)
        myButton.pack()

K=Statistic_Window()
K.mainloop()