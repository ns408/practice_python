#!/usr/bin/env python

class Employee:
    """Employee class"""

    def __init__(self, first_name, last_name, annual_salary):
        """
        Initialise
        """
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """Add 5k to the annual salary by default but also accept a different
        amount"""
        self.annual_salary += amount
