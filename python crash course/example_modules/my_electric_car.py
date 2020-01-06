#!/usr/bin/env python3

from module2.car import ElectricCar

"""
module1 is the directory in which car.py is present

# Another technique is adding it to the path.
import sys
sys.path.insert(1, '/path/to/application/app/folder')
import file
"""

my_car = ElectricCar("Tesla", "3", 2020)
print(my_car.get_descriptive_name())

# Calling the attribute directly instead of updating it via the methods
my_car.battery.describe_battery()
my_car.battery.get_miles_left()
