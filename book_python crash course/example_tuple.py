#!/usr/bin/env python3

"""
Working with Python Tuples (like lists but Immutable)
"""

a_tuple = ("item1", "item2", "item3", "item4")

# Let's try assigning a value to an item in a tuple and see what happens
# Using try:except so that the script doesn't break here
try:
    a_tuple[0] = "item0"
except TypeError as e:
    print("Error: " + str(e))

a_tuple = ("what",)
print("A tuple with a single item: " + str(a_tuple))

print("\nOne can assign a new value to a tuple variable:")
a_tuple = ("when",)
print(a_tuple)
print()