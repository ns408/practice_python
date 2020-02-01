#!/usr/bin/env python3

"""
Items which didn't fit anywhere else go in here.
"""

"""
\n - newline
\t - tab
"""
var = "myname\n\tFirstname\n\tLastname\nyourname"
print(var)

"""
rstrip()
lstrip()
strip()
"""
var_l = " string_with_space_on_left"
print(var_l)
print(var_l.lstrip())
var_r = "string_with_space_on_right "
print(var_r)
print(var_r.rstrip())
var = " string_with_space_on_left_and_right "
print(var)
print(var.strip())

# Print things dynamically
# https://stackoverflow.com/questions/3249524/print-in-one-line-dynamically
item = 0
while True:
  item += 1
  print(f"{item} ", sep=' ', end='', flush=True)
