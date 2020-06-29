#!/usr/bin/env python3


class Car:
    """Represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        """return a formatted name."""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name

    def read_odometer(self):
        """Show the mileage."""
        print(f"{self.odometer} miles")

    def update_odometer(self, mileage):
        """Update the value through a method rather than directly."""
        if mileage > self.odometer:
            self.odometer = mileage
            return True
        else:
            print("can't roll back")

    def increment_odometer(self, mileage):
        """Increment the value through a method."""
        if mileage >= 0:
            self.odometer += mileage
            return True
        else:
            print("can't roll back")

    def fill_gas_tank(self):
        """Someone doesn't have an electric car"""
        print("Filling gas...")

if __name__ == "__main__":
    mycar = Car("Toyota", "Hilux", 2019)
    print(mycar.get_descriptive_name())
    print(f"\nReading before changing: ")
    mycar.read_odometer()
    print()

    print("\nUpdate the mileage")
    if mycar.update_odometer(2):
        mycar.read_odometer()

    print("\nIncrement the mileage")
    if mycar.increment_odometer(100):
        mycar.read_odometer()