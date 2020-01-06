#!/usr/bin/env python3

"""
real world things/situations -> classes -> objects
"""

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
