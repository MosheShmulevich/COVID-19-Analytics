import unittest
import Register


class TestRegister(unittest.TestCase):
    def test_register_function(self):
        self.assertIsNotNone(Register.Register())
        self.assertTrue(Register.Register())
        self.addTypeEqualityFunc(int, Register.Register())

    def test_CleanUserData_function(self):
        self.assertIsNotNone(Register.CleanUserData("Amei"))
        self.assertFalse(Register.CleanUserData("Mike"))
        self.assertTrue("MosheShmul")
        self.assertIs(Register.CleanUserData("Gila"),Register.CleanUserData("Haim"))


if __name__ == '__main__':
    unittest.main()
