#!/usr/bin/env python3

"""
Working with Python Lists
"""

summary = """
###### Summary ######
- lists usually contain more than one element so better name them plural. Eg: names, addresses
"""
print(summary)

alist = ["this", "that", "whatever", "whereever"]
print(f"Display the list: {alist}")
print(f"Display a single item: {alist[0]}")
print(f"Display a single item using the title() method: {alist[0].title()}")
print(f"Display the last item: {alist[-1]}")
print(f"Display a range of elements; specifically 2nd and 2nd last: {alist[1:-1]}")

print("\nModify the list")
alist[2] = "anyhow"
print(f"Display the modified list: " + str(alist))
print(f"Display the modified list again: {str(alist)}\nJust another way of achieving it using f-strings.")

anewlist = []
print(f"\nA new empty list: {anewlist}\n")

anewlist.append("first")
anewlist.append("second")
anewlist.append("third")
anewlist.append("fourth")
print(f".append() element to the end of the list: {anewlist}")
anewlist.insert(0, "fifth")
print(
    f".insert() element to the list shifting first element to the second place: {anewlist}")

del anewlist[0]
print()
print(f"del an item from the array: {anewlist}")

var = anewlist.pop()
print(f".pop() the last item and store it in var: {var}")
var = anewlist.pop(0)
print(f".pop(0) an item selectively and store it in var: {var}\n")

anewlist.remove("second")
print(
    f".remove('second') an item through value and display the list: {anewlist}\n"
    ".remove('value') removes only the first occurance. Use this method in a loop for more occurances.\n"
    )

alist = ["e", "d", "c", "b", "a"]
alist.sort()
print(f".sort() a list permanently in alphabetical order: {alist}")
alist.sort(reverse=True)
print(f".sort(reverse=True) a list permanently in reverse alphabetical order: {alist}")

print(f"sorted() to temporarily sort a list: {sorted(alist)}\n")

alist.reverse()
print(f".reverse() to rearrage the list in reverse chronological order: {alist}")
alist.reverse()
print(f".reverse() to reverse the list again: {alist}")

print(f"Find length of the list: {len(alist)}")
