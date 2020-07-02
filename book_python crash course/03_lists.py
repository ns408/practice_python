#!/usr/bin/env python3

"""
Working with Python Lists
"""

alist = ["item1", "item2", "item3", "item4"]
print("Looping through list elements:")
for item in alist:
    print(item, end='\t') # forcing print to not use '\n' and instead use '\t'

print("\n\nrange() function use:")
print("start at first argument and stop before second: range(1, 4)")
for item in range(1, 4):
    print(item, end='\t')

print("\nrun 0 to 3: range(4)")
for item in range(4):
    print(item, end='\t')

print("\nuse list() function to make a list using range")
alist = list(range(1, 6))
print(alist)

print("\nuse list(range(2,11,2)) to create an array of even numbers")
alist = list(range(2, 11, 2))
print(alist, end='\t')

print("\nDisplay squares of 1-10 using range()")
square = []
for item in range(1, 11):
    square.append(item**2)
print(square)

print("\nSimple stats with a list of numbers")
digits = list(range(1, 6))
print(f"min() of the digits list: {min(digits)}")
print(f"max() of the digits list: {max(digits)}")
print(f"sum() of the digits list: {sum(digits)}")

print("\nList comprehensions: allows concise creation of lists through one liners")
square = [item**2 for item in range(1, 6)]
print(square)

"""
#Exercise:

# Count to twenty
for item in range(1,21):
  print(item)

# One million - list to loop and print
print("Python 3.6 onwards can understand numbers even with the _")
alist = list(range(1,1_00_00_01))
for item in alist:
  print(item)

# Sum a million
alist = list(range(1,1_00_00_01))
for func in min, max, sum:
  print(str(func) + "(alist): " + str(func(alist)))

# Odd numbers - use third argument of the range() function
alist = list(range(1,21,2))
for item in alist:
  print(item)
# Output: 1, 3, 5, 7, 9 ... 19

# Threes: list of multiples of 3 from 3 to 30
alist = list(range(3,31,3))
for item in alist:
  print(item)

# Cubes - list of first 10 cubes
alist = []
for item in range(1,11):
  alist.append(item**3)
print(f"List first 10 cubes: {alist}")

# Cube list comprehension
alist = [item**3 for item in range(1,11)]
print(f"Using list comprehension: {alist}")
"""

print("List slicing examples:")
alist = ["str1", "str2", "str3", "str4", "str5"]
print(f"print first 4 items (alist[4]): {alist[:4]}")
print(f"print last 2 items (alist[-2:]): {alist[-2:]}")
print(f"print all items 2 onwards (alist[2:]): {alist[2:]}")
print(f"print 2nd and 3rd item (alist[1:3]): {alist[1:3]}")
print(f"print items skipping 1 (alist[::2]): {alist[::2]}")

print("\nloop through a slice")
for item in alist[:2]:
    print(item)

print("\nCopy a list using slicing [:]")
things_i_like = ["python", "ruby", "workouts"]
things_my_clone_likes = things_i_like[:]
print(things_my_clone_likes)

print("You can't just copy a list using this: anewlist = alist\n")
alist = ["whatever", "whenever", "whereever"]
anewlist = alist
alist.append("test")
print(f"Display anwelist after modifying alist variables: {anewlist}")
print("Above we have associated two variables with the same list so any changes to either variables will make change to the same list.\n")
