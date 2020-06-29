#!/usr/bin/env python

from employee import Employee
import unittest

class TestEmployee(unittest.TestCase):
    """Class to test methods within Employee Class"""

    def setUp(self):
        """Define objects once for the test methods"""
        self.an_employee = Employee('Jane', 'Doe', 5000)

    def test_give_default(self):
        self.an_employee.give_raise()
        self.assertEqual(self.an_employee.annual_salary, 10000)

    def test_give_custom_raise(self):
        self.an_employee.give_raise(15000)
        self.assertEqual(self.an_employee.annual_salary, 20000)

if __name__ == "__main__":
    unittest.main()