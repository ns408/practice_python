#!/usr/bin/env python3

"""
real world things/situations -> classes -> objects
"""

from car import Car


# Creating the Dog Class
class Dog:
    """ Model a dog.
    Convention: capitalised names for classes
    docstring to describe what this class does.
    """

    def __init__(self, name, age):
        """
        Special method that gets run on creation of a new instance of class.
        Initialise attributes.
        """
        self.name = name
        self.age = age

    def sit(self):
        """dog sitting."""
        print(f"{self.name} is sitting.")

    def bark(self):
        """dog barking."""
        print(f"{self.name} is barking.")


adog = Dog('buddy', 4)
bdog = Dog('milo', 2)

print(f"Dog's name is {adog.name} and age is {adog.age}")
adog.bark()
print()

print(f"Dog's name is {bdog.name} and age is {bdog.age}\n")

# Exercise


class Restaurant:
    """
    Class modelling restaurants.
    """

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")


restaurant = Restaurant("Waterfront", "Seafood")
print(f"Name of the Restaurant: {restaurant.restaurant_name}")
restaurant.open_restaurant()
restaurant.describe_restaurant()
print("\n#### 3 restaurants ####\n")

restaurant1 = Restaurant("Coco", "Islander")
restaurant2 = Restaurant("Copacabana", "Brazilian")
restaurant3 = Restaurant("Sicily", "Italian")
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
print()


class User():
    """
    Users class.
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old.")

    def greet_user(self):
        print(f"Welcome {self.first_name} {self.last_name}.")


print("""
# way-1
user_list = []
for num in range(1, 3):
    user_list.append(User(f"firstname{num}", f"lastname{num}", 100 + num))

# way-2
user_list = []
for num in range(1, 3):
    user_list += [User(f"firstname{num}", f"lastname{num}", 100 + num)]

# way-3 (list comprehension)
user_list = [
    User(f"firstname{num}", f"lastname{num}", 100 + num)
    for num in range(1, 3)
]
""")


# Using list comprehension
user_list = [
    User(f"firstname{num}", f"lastname{num}", 100 + num)
    for num in range(1, 3)
]

for item in user_list:
    item.greet_user()
    item.describe_user()
print()


# Because we started adding too many attributes and methods to the ElectricCar class,
# now we are deciding to move the battery related attributes/methods to a separate one
# to keep the class from getting too complex.

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

# Inheritance - Line 7
# mucking around with import cause too lazy to define the class here again.


class ElectricCar(Car):
    """Electric vehicle specific aspects."""

    def __init__(self, make, model, year):
        """
        Initialise attributes for the parent class.
        Initialise electric car specific attributes.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
        # Create new instance of the Battery class replacing the
        # previous self.battery = 75

# Moved the function to Battery
#   def describe_battery(self):
#       """
#       Print a statement describing the battery size.
#       """
#       print(f"Battery size: {self.battery}")

    def fill_gas_tank(self):
        """
        Overriding the method from the parent/super Car class
        Electric don't need no gas tank.
        """
        print(f"{self.model} gonna need a supercharger station.")


my_car = ElectricCar('tesla', 'cybertruck', 2020)
print(my_car.get_descriptive_name())
# my_car.describe_battery() - replaced with
my_car.battery.describe_battery()
my_car.fill_gas_tank()
my_car.battery.get_miles_left()
print()

######### Exercise Begin #########


class IceCreamStand(Restaurant):
    """
    Inherits from Restaurant class as it's a specific kind of restaurant.
    Contains
    - attribute: flavours
    - method: display_flavours
    """

    def __init__(self, restaurant_name, cuisine_type):
        """
        Define how this class will be initialised.
        Also include attributes and methods of the super/parent class.
        Also, supply the flavour attribute.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ["vanilla", "chocolate",
                         "tiramissu", "blackcurrent", "black-seasame"]

    def display_flavours(self):
        """
        Display all the flavours
        """
        print(f"Flavours: {self.flavours}")


my_icecream = IceCreamStand("Coco's", "IceCream Joint")
my_icecream.open_restaurant()
my_icecream.display_flavours()
print()



my_car1 = ElectricCar("Ford", "Falcon", 2019)
print(my_car1.get_descriptive_name())
my_car1.battery.get_miles_left()
my_car1.battery.upgrade_battery()
my_car1.battery.get_miles_left()

######### Exercise END #########