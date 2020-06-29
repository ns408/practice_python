""" A set of classes that can be used to represent electric cars."""

from car import Car

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