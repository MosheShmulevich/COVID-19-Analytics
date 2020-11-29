import mysql.connector

PatientsDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)