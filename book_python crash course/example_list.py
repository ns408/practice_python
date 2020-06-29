#!/usr/bin/env python3

"""
Working with Python Lists
"""

alist = ["this", "that", "whatever"]
print(f"Display the list: {alist}")
print(f"Display a single item: {alist[0]}")
print(f"Display a single item using the title() method: {alist[0].title()}")
print(f"Display the last item: {alist[-1]}")

print("\nModify the list")
alist[2] = "anyhow"
print(f"Display the modified list:" + str(alist))

"""
Could have used this for the above but just to show another way of achieving it:
print(f"Display the modified list:" + str(alist))
"""

anewlist = []
print(f"\nA new empty list: {anewlist}\n")
anewlist.append("first")
anewlist.append("second")
anewlist.append("third")
anewlist.append("fourth")
print(f".append() element to the list: {anewlist}")
anewlist.insert(0, "fifth")
print(
    f".insert() element to the list shifting first element to the second place: {anewlist}")

del anewlist[0]
print()
print(f"del an item from the array: {anewlist}")

var = anewlist.pop()
print(f".pop() the last item and store it in var: {var}")
var = anewlist.pop(0)
print(f".pop(0) an item selectively and store it in var: {var}")

anewlist.remove("second")
print(
    f".remove('second') an item through value and display the list: {anewlist}")
print(".remove('value') removes only the first occurance.\n Use this method in a loop for more occurances.")

print()
alist = ["e", "d", "c", "b", "a"]
alist.sort()
print(f".sort() a list permanently: {alist}")
alist.sort(reverse=True)
print(f".sort(reverse=True) a list permanently: {alist}")


print(f"sorted() to temporarily sort a list: {sorted(alist)}")
print()

alist.reverse()
print(f".reverse() to reverse a list: {alist}")
alist.reverse()
print(f".reverse() to reverse the list again: {alist}")

print(f"Find length of the list: {len(alist)}")
