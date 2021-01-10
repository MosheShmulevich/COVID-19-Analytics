import unittest
import workers_messages
from tkinter import *
from tkinter import ttk

class TestWorkersMessages(unittest.TestCase):
    def test_send(self):
        self.assertIsNotNone(workers_messages.window.send, "should not be  none")

    def test_window(self):
        TestWindow = Tk()
        self.assertIsNot(workers_messages.window, Tk, "should not be the same")
        self.assertIsNot(workers_messages.textentry, Entry, "should not be the same")
        self.assertIsNot(workers_messages.textentry1, ttk.Entry, "should not be the same")
        self.assertIsNot(workers_messages.textentry2, Label, "should not be the same")
        self.assertIsNot(workers_messages.textentry_pas, ttk.Combobox, "should not be the same")
        self.assertIsNot(workers_messages.window, TestWindow, "should not be the same")


if __name__ == '__main__':
    unittest.main()