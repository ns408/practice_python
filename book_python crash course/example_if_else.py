#!/usr/bin/env python3

"""
Working with conditionals, i.e. if-else
"""

cars = ["audi", "bmw", "toyota", "mercedes"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

print("Keep in mind equality(==) operator is different to assignment(=) \
operator")

print("\nIgnore case while testing:\n")
car = "TeSla"
if car.lower() == "tesla":
    print("That's cool! But Model S, right?")

print("\nCheck for not equal(!=)")
if car.lower() != "tesla":
    print("okay...")
else:
    print("say what now..")

print("""
Examples of mathematical comparisons:
fingers = 5
fingers < 10 # True
fingers > 5  # False
fingers >= 2 # True
fingers <=5  # True
""")

print("""
Check multiple conditions:
bones = 206
bones >= 200 and bones < 400 # True
bones > 200 or bones < 20 # True
""")

print("""
Test if an item in the list:
maze = ["blue", "green", "black", "white"]
if "black" in maze:
    print("black in maze")
""")
maze = ["blue", "green", "black", "white"]
if "black" in maze:
    print("black in maze")

print("""
# Example of test if an item is not in the list:
if "black" not in maze:
    print("black not in maze")
""")

print("""
Shorthand version for above:
maze = ["blue", "green", "black", "white"]
print(f"Black in maze: {'black' not in maze}")
print("Black in maze: " + str('black' not in maze))
""")

print("""
today = "Monday"
if today == "Friday":
    print("whateve")
else:
    print("Oh yeah!")
""")
today = "Monday"
if today == "Friday":
    print("whateve")
else:
    print("Oh yeah!")

print("""
today = "Monday"
if today == "Friday":
    print("whateve")
elif today == "Someday":
    print("yeah, nah")
else:
    print("Oh yeah!")
""")
today = "Someday"
if today == "Friday":
    print("whatever")
elif today == "Someday":
    print("yeah, nah")
else:
    print("Oh yeah!")

print("""

# Empty list is False when tested
alist = []
if alist:
    print("list got an item")
else:
    print("list got no item")
""")
alist = []
if alist:
    print("list got an item")
else:
    print("list got no item")

print("""
# Test if items from list1 are available in list2
list1 = [1, 2, 3, 4, 5]
list2 = [4, 2, 3, 1]
for item in list1:
    if item in list2:
        print(f"exists in both lists: {item}")
    else:
        print(f"doesn't exist in list2: {item}")
""")
list1 = [1, 2, 3, 4, 5]
list2 = [4, 2, 3, 1]
for item in list1:
    if item in list2:
        print(f"exists in both lists: {item}")
    else:
        print(f"doesn't exist in list2: {item}")

# Exercise
# Ordinal numbers indicate their position in a list, such as 1st or 2nd.

# Ordinal numbers
alist = list(range(1, 6))

for item in alist:
    if item == 1:
        print("1st")
    elif item == 2:
        print("2nd")
    elif item == 3:
        print("3rd")
    else:
        print(f"{item}th")

print("""
Note:
This happened when I decided to define a list as "list".
Do not use keywords as variables.

Traceback (most recent call last):
  File "./example_if_else.py", line 135, in <module>
    alist = list(range(1, 6))
TypeError: 'list' object is not callable
""")
