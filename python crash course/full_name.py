#!/usr/bin/env python3
"""
use a variable’s value inside a string.
f-strings: python formats the string by replacing the name of any variable in
braces with its value.
"""
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")

"""
f-strings were introduced in 3.6.
If using python3.4 or earlier, use format().

Example: full_name = "{} {}".format(first_name, last_name)
"""