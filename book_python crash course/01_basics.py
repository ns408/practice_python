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
print("Demonstrate use of rstrip, lstrip and strip")
print("strip1 :" + "strip1 ".lstrip())