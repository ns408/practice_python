"""
Module-level docstring to describe what this is about.
Store set of classes to represent gas and electric cars.
"""

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

class Battery:
    """model electric car's battery"""

    def __init__(self, battery=75):
        """Initialise the attributes."""
        self.battery = battery

    def describe_battery(self):
        """
        Print a statement describing the battery size.
        """
        print(f"Battery size: {self.battery}")

    def get_miles_left(self):
        """Show me if I'm gonna get home today or not."""
        if self.battery == 75:
            miles_left = 300
        elif self.battery == 100:
            miles_left = 500

        print(f"You'll get {miles_left} miles.")

    def upgrade_battery(self):
        if self.battery < 100:
            self.battery = 100
        print("Battery upgraded.")

class ElectricCar(Car):
    """Electric vehicle specific aspects."""

    def __init__(self, make, model, year):
        """
        Initialise attributes for the parent class.
        Initialise electric car specific attributes.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """
        Overriding the method from the parent/super Car class
        Electric don't need no gas tank.
        """
        print(f"{self.model} gonna need a supercharger station.")