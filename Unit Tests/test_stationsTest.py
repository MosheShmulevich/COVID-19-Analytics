import unittest
import test_stations
from tkinter import *
from tkinter import ttk

class Test_test_stations(unittest.TestCase):
    def test_window(self):
        self.assertIsNotNone(test_stations.window, "should not be none")
        self.assertIsNot(test_stations.window, Tk, "should not be the same")
        self.assertIsNotNone(test_stations.window.title, "should not be none")
        self.assertIsNot(test_stations.photo_map, PhotoImage, "should not be photoimage")
        self.assertIsNotNone(test_stations.Button, "should not be none")
        self.assertIsNotNone(test_stations.clicked, "should be not none")
        self.assertNotEqual(test_stations.cities, test_stations.drop, "should not be the same")
        self.assertIsNotNone(test_stations.Label, "should not be none")

    def test_city_map(self):
        self.assertIsNot(test_stations.city_map, test_stations.window, "should not be the same")
        self.assertIsNotNone(test_stations.city_map, "should not be none")
        self.assertIsNotNone(test_stations.clicked.get(), "should not be none")

if __name__ == '__main__':
    unittest.main()