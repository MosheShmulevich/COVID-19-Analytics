import unittest
import AddPatientToDB
from datetime import *


class TestAddPatientToDB(unittest.TestCase):
    def test_AddPatientToDB_function(self):
        self.assertIsNotNone(
            AddPatientToDB.addPatient(('Tom', 'Ska', 546879258, datetime.strptime("06/04/1992", "%d/%m/%Y"),
                                       datetime.strptime("15/09/2020", "%d/%m/%Y"), "Positive", "Yes",
                                       "Active"), "Beersheba"))


if __name__ == '__main__':
    unittest.main()