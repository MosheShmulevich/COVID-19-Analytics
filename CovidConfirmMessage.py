from dataclasses import dataclass
from collections import namedtuple
import datetime
import Database


class new_patient:
    name: str
    tested: str
    status: str
    date: datetime


def confirm_message(database, new_patient):
    patient_test = namedtuple('Patient Tested', ['yes', 'no'])
    patient_status = namedtuple('Patient Status ', ['denied', 'confirmed'])
    message = open('Message.txt', 'rt').read()
    print(message)
    if input("1.") == ('yes' or 'Yes'):
        new_patient.tested = 'yes'
    else:
        new_patient.tested = 'no'
        exit(0)
    if input("2.") == ('p' or 'P'):
        new_patient.status = 'Confirmed'
    else:
        new_patient = 'Denied'
        exit(0)
    new_patient.date.day = input("day:")
    new_patient.date.month = input("month: (number)")
    new_patient.date.year = input("year:")
