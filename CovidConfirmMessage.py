from dataclasses import dataclass
from collections import namedtuple
import datetime
import Database
import Status
import AddPatientToDB


class new_patient:
    name: str
    tested: str
    status: str
    date: datetime


def confirm_message(database, self):
    patient_test = namedtuple('Patient Tested', ['yes', 'no'])
    patient_status = namedtuple('Patient Status ', ['denied', 'confirmed'])
    message = open('Message.txt', 'rt').read()
    print(message)
    if input("1.") == ('yes' or 'Yes'):
        self.tested = 'yes'
    else:
        self.tested = 'no'
        exit(0)
    if input("2.") == ('p' or 'P'):
        self.status = 'Confirmed'
    else:
        self.status = 'Denied'
        exit(0)
    self.date.day = input("day:")
    self.date.month = input("month: (number)")
    self.date.year = input("year:")
    if patient_status == 'Confirmed':
        AddPatientToDB.add_patient_to_db(self)
