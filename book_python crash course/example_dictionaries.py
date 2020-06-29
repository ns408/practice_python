#!/usr/bin/env python3

"""
Time to play with Python Dictionaries
key-value pair
"""

days = {
    "monday": 1,
    "tuesday": 2,
    }
print(days)
print(days["tuesday"])

print("""
days = {
    {
        "one": 1,
        "two": 2,
    }: 1,
}

# throws an error
Traceback (most recent call last):
  File "./example_dictionaries.py", line 19, in <module>
    }: 1,
TypeError: unhashable type: 'dict'

So it seems that only a string or a number can be the key.
""")

adict = {
    "this": "that",
    "when": "now",
}
print(f'{adict["this"]} is {adict["when"]}')
# Playing with interpolation using single quotes here.
# In bash, variables don't work with single quotes.
print()

# ..... skipping stuff

adict = {"colour": "black", "quantity": "enough"}
var = adict.get("volume", 'No volume key assigned.')
print(var)
print()

adict = {}
var = adict.get("something")
print(f"when .get() doesn't find a value, it returns: {var}")

# ..... skipping stuff

# A set is a collection in which each item must be unique

favourite_lang = {
    "me": "python",
    "myself": "ruby",
    "I": "golang",
    "you": "golang",
}
print("Run the loop against a list")
for language in favourite_lang.values():
    print(language.title())
print()
print("Run the loop against a set")
for language in set(favourite_lang.values()):
    print(language.title())

print("Example of building a set directly:")
print("""
lang = {'python', 'ruby', 'ruby', 'golang'}
""")

# Exercise

# Polling
"""
Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.
Loop through the list of people who should take the poll.
If they have already taken the poll, print a message thanking them for
responding. If they have not yet taken the poll, print a message inviting them
to take the poll.
"""

people_poll = {
    "james": "ruby",
    "dick": "erlang",
    "julie": "golang",
    "alex": "python",
}

people_list = [
    "james",
    "dick",
    "julie",
    "alex",
    "julia",
    "calum",
]

for item in people_list:
    if item not in people_poll.keys():
        print(f"Come on ya, take the poll please {item} :)")

