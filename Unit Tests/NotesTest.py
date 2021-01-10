import unittest
import NotesTkinter
from tkinter import ttk
from tkinter import *
from NotesTkinter import NewWindow



class TestNotesTkinter(unittest.TestCase):
    def test_NotesPage(self):
        self.assertIsNot(NotesTkinter.Page, Tk(), "Should not be Tk")
        self.assertIsNot(NotesTkinter.Page, NotesTkinter.NotesPage, "should not be the same")

    def test_add_widgets(self):
        self.assertIsNotNone(NotesTkinter.Page.Name, "should be not None")
        self.assertIsNotNone(NotesTkinter.Page.Subject, "should be not None")
        self.assertIsNotNone(NotesTkinter.Page.Message, "should be not None")
        self.assertIsNotNone(NotesTkinter.Page.Tab1, "should be not None")
        self.assertIsNotNone(NotesTkinter.Page.tab_control, "should be not None")
        self.assertIsNone(NotesTkinter.Page.SubmitButton, "should be None")
        self.assertIsNone(NotesTkinter.Page.SubmitButton, "should be not none")

    def test_create_tabs(self):
        self.assertIsNotNone(NotesTkinter.Page.tab_control, "should be not None")
        self.assertIsNotNone(NotesTkinter.Page.Tab1, "should be not None")
        self.assertIsNot(NotesTkinter.Page.tab_control, ttk.Notebook, "should not be ttk.Notebook")
        self.assertIsNot(NotesTkinter.Page.Tab1, ttk.Frame, "should not be ttk.Frame")

class TestNewWindow(unittest.TestCase):
    def test_NewWindow(self):
        self.assertIsNot(NewWindow, Tk, "Should not be Tk")

    def test_Confirm(self):
        self.assertIsNotNone(NewWindow.Confirm, "should be not none")
        self.assertIsNot(NewWindow.ReturnYes, NotesTkinter.Page, "should not be the same")
        self.assertIsNot(NewWindow, NewWindow.Confirm, "should not be the same")

    def test_ReturnYes(self):
        self.assertIsNot(NotesTkinter.Page, NewWindow.ReturnYes, "should not be the same")
        self.assertIsNotNone(NewWindow.ReturnYes, "should return not None")

    def test_ReturnNo(self):
        self.assertIsNot(NotesTkinter.Page, NewWindow.ReturnNo, "should not be the same")
        self.assertIsNotNone(NewWindow.ReturnNo, "should return not None")
        self.assertIsNot(NotesTkinter.Page.ThanksMessage, ttk.Label, "should not be the same")


if __name__ == '__main__':
    unittest.main()
