import unittest
import Updates
from tkinter import *
from tkinter import ttk


class TestUpdates(unittest.TestCase):
    def test_UpdatingPage(self):
        self.assertIsNotNone(Updates.UpdatingPage, "should not be none")
        self.assertIsNot(Updates.UpdatingPage, Updates.updates, "should not be the same")
        self.assertIsNotNone(Updates.UpdatingPage.AddTabs, "should not be none")
        self.assertIsNotNone(Updates.UpdatingPage.CreateLabel, "should not be none")
        self.assertIsNotNone(Updates.UpdatingPage.CreateButton, "should not be none")
        self.assertIsNotNone(Updates.UpdatingPage.PrintMessage, "should not be none")
        self.assertIsNotNone(Updates.updates.CreateLabel, "should not be none")

    def test_AddTabs(self):
        self.assertIsNot(Updates.updates.tab_control, ttk.Notebook, "should not be the same")
        self.assertIsNotNone(Updates.updates.tab_control, "should not be None")
        self.assertIsNot(Updates.updates.UpdatingPage, "should not be None")
        self.assertIsNotNone(Updates.updates.ContactInformation, "should not be None")
        self.assertIsNot(Updates.updates.ContactInformation, ttk.Frame, "should not be the same")

    def test_CreateLabel(self):
        self.assertIsNot(Updates.updates.Updating, str, "should be string")
        self.assertIsNone(Updates.updates.labelUpdatingPage, "should be none")
        self.assertIsNone(Updates.updates.labelContactInformation, "should be none")
        self.assertEqual(Updates.updates.labelContactInformation, Updates.updates.labelUpdatingPage, "should be  equal")
        self.assertIsNot(Updates.updates.Updating, Updates.updates.labelUpdatingPage, "should not be the same")

    def test_CreateButton(self):
        self.assertIsNotNone(Updates.updates.MessageButton, "should be not none")
        self.assertIsNone(Updates.updates.MessageBox, "should be none")
        self.assertIsNot(Updates.updates.MessageButton, Updates.updates.MessageBox, "should not be the same")
        self.assertIsNot(Updates.updates.MessageButton, ttk.Button, "should not be the same")

    def test_PrintMessage(self):
        self.assertIsNone(Updates.updates.LabelMessage, "should be none")
        self.assertIsNot(Updates.updates.LabelMessage, Label, "should not be the same")

if __name__ == '__main__':
    unittest.main()
