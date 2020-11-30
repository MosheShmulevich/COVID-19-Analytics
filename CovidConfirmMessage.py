import AddPatientToDB
from dataclasses import dataclass
from typing import NamedTuple
from datetime import *


@dataclass()
class New_Patient:
    firstname: str
    lastname: str
    ID: int
    birth_date: datetime
    test_date: datetime
    test_result: str
    is_tested: str
    status: str

def confirm_message(New_Patient):
    message = open('Message.txt', 'rt').read().splitlines()
    print(open('Message.txt', 'rt').read())
    patient_tested = str(input(message[4]))
    if patient_tested in ['n', 'N']:
        New_Patient.is_tested = 'no'
        exit("patient not tested!")
    elif patient_tested in ['y', 'Y']:
        New_Patient.is_tested = 'yes'
    else:
        if str(input("invalid input received, enter 1 to try again else 0 to exit")) == '1':
            confirm_message(New_Patient)
        else:
            exit(0)
    patient_result = str(input(message[5]))
    if patient_result in ['p', 'P']:
        New_Patient.test_result = 'Positive'
    elif patient_result in ['n', 'N']:
        New_Patient.status = 'Negative'
        exit("patient test result is negative")
    else:
        if str(input("invalid input received, enter 1 to try again else 0 to exit")) == '1':
            confirm_message(New_Patient)
        else:
            exit(0)

    if patient_result in ['P', 'p']:
        New_Patient.city = str(input("Which city the patient is from?"))
        AddPatientToDB.addPatient(New_Patient, New_Patient.city)


confirm_message(New_Patient("Mike", "lasto", 546827551, datetime.strptime("25/11/1995", "%d/%m/%Y"),
                            datetime.strptime("25/07/2020", "%d/%m/%Y"), "Positive", "Yes",  "Active"))
