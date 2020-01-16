#!/usr/bin/env python3

from module2 import car

# If this was in the same directory, then it will just be `import car`

"""
module1 is the directory in which car.py is present

# Another technique is adding it to the path.
import sys
sys.path.insert(1, '/path/to/application/app/folder')
import file
"""

my_car = car.Car("Ford", "Endeavour", 2020)
print(f"My car on gas: {my_car.get_descriptive_name()}")

# Calling the attribute directly instead of updating it via the methods
my_car.odometer = 5
#my_car.read_odometer()
print()

my_car = car.ElectricCar("Tesla", "X", 2020)
print(f"My car on electricity: {my_car.get_descriptive_name()}")