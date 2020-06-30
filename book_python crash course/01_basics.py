#!/usr/bin/env python3

message = "sup!"
print(message)

message = "sup yo!"
print(message)


"""
name.py
Change each word to begin with capital letters.
title() is a method.
"""
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

"""
Concatenate strings
"""
first_name = "batman"
last_name = "nunya"
full_name = first_name + " " + last_name
print("\nSup " + full_name.title())

"""
tabs
newlines
"""
print("This is a \ttabbed string with a \nnewline.")

"""
Strip whitespace
"""
print("\nDemonstrate use of rstrip, lstrip and strip")
print("lstrip: " + " string".lstrip())
print("rstrip: " + "string ".rstrip())
print("strip:  " + " string ".strip())

# Numbers
print(f"\nExponents:\n3 ** 3 = {3 ** 3}\n")

print("Arbitrary number of decimal places due to how numbers are present internally.")
print(0.2 + 0.1)
print(3 * 0.1)


# str() function
message = "Sup " + "k" + str(8)
print( "\nUsing str(): " + message)

value = 3 / 2
print("\nDivision of integers: " + str(value))

print("import this\nThe Zen of Python, by Tim Peters\n\n")
import this