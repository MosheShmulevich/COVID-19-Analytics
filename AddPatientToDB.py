import CovidConfirmMessage
import Database
import mysql.connector
import pyodbc


def add_patient_to_db(patient):
    Database.cursor.excute('''
                            INSERT INTO covid19.dbo.patient (id,first_name,last_name,birth_date,is_tested,
                            test_result,city)
                            VALUES
                            (258741369,'Mike','Lasto',2012-12-13,'yes',positive','ramat-gan)
                            ''')
    Database.conn.commit()
