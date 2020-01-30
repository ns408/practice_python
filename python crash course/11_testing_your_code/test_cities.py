#!/usr/bin/env python

"""
Test function from city_functions.py
"""
import unittest
from city_functions import get_city_country

class CitiesTestCase(unittest.TestCase):
    """
    Class to test the get_city_country function
    """

    def test_get_city_country(self):
        """test the function"""
        city_country = get_city_country('santiago', 'chile')
        self.assertEqual(city_country, 'Santiago, Chile')

if __name__ == "__main__":
    unittest.main()