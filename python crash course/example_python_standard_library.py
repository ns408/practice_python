#!/usr/bin/env python

# function from random module: randint()

from random import randint
print(f"Random number between 1 and 6 on every run: {randint(1, 6)}")

# choice function
from random import choice
players = ["dumdum", "dumdum1", "dumdum2", "dumdum3"]
first_up = choice(players)
print(f"Random players from the list using choice: {first_up}")

# choice function
from random import choice
players = ("dumdum", "dumdum1", "dumdum2", "dumdum3")
first_up = choice(players)
print(f"Random players from the list using choice: {first_up}")