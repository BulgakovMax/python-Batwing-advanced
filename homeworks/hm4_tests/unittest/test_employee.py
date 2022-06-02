import unittest
from employee import Employee
from unittest.mock import patch


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("nick", "clinton", 1000)

    def test_email(self):
        self.assertEqual(self.employee.email, 'nick.clinton@email.com')

    def test_fullname(self):
        self.assertEqual(self.employee.fullname, 'nick clinton')

    def test_apply_raise(self):
        self.assertEqual(self.employee.pay*self.employee.raise_amt, 1050)

    @patch("employee.requests.get")
    def test_monthly_schedule(self, mock_response):
        mock_response.return_value.text = "TEST"
        self.assertEqual(self.employee.monthly_schedule("june"), 'TEST')


