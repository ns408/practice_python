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
        city_country = f"{city_country} - population={population}"
    return city_country