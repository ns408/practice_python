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

    def test_city_country_population(self):
        """test the function"""
        city_country = get_city_country('santiago', 'chile', 5000000)
        self.assertEqual(city_country, 'Santiago, Chile - population=5000000')

if __name__ == "__main__":
    unittest.main()