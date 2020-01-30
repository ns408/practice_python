#!/usr/bin/env python

"""
Function that accepts two parameters: a city name and a country name.
Returns a single string of the form 'City, Country'. Eg: 'Santiago, Chile'
"""

def get_city_country(city, country, population=""):
    """Return formatted string 'City, Country -  population xxx'."""
    city_country = f"{city}, {country}"
    city_country = city_country.title()
    if population:
        city_country = f"{city_country} - population {population}"
    return city_country

"""
 11-2. Population: Modify your function so it requires a third parameter, population. It should now return a single string of the form City, Country – population xxx, such as Santiago, Chile – population 5000000. Run test _cities.py again. Make sure test_city_country() fails this time.
Modify the function so the population parameter is optional. Run test _cities.py again, and make sure test_city_country() passes again.
Write a second test called test_city_country_population() that veri- fies you can call your function with the values 'santiago', 'chile', and 'population=5000000'. Run test_cities.py again, and make sure this new test passes.
"""