import unittest
import CreateReport


class TestCreateReport(unittest.TestCase):
    def test_create_report_function(self):
        self.assertIsNone(CreateReport.create_report('Acre'))
        self.addTypeEqualityFunc(str, CreateReport.create_report('Arad'))
        self.assertIs(CreateReport.create_report('Acre'), CreateReport.create_report('Arad'))
        self.assertEqual(CreateReport.create_report('Acre'), CreateReport.create_report('Arad'))


if __name__ == '__main__':
    unittest.main()
