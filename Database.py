import mysql.connector
import pyodbc

PatientsDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=Local instance MySQL80;'
                      'Database=covid19;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM covid19.dbo.patient')


