#!/usr/bin/env python

"""
Function that accepts two parameters: a city name and a country name.
Returns a single string of the form 'City, Country'. Eg: 'Santiago, Chile'
"""

def get_city_country(city, country):
    """Return formatted string 'City, Country'."""
    city_country = f"{city}, {country}"
    return city_country.title()
