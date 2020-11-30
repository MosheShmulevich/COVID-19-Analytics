import unittest
import Database
from openpyxl import *


class TestDatabase(unittest.TestCase):
    def test_InsertListToDB(self):
        self.assertIsNotNone(Database.InsertListToDB())
        self.addTypeEqualityFunc(list, Database.IL_CityList)
        self.assertIs(Database.city_sheet, Database.userSheet)


if __name__ == '__main__':
    unittest.main()