#!/usr/bin/env python


"""
9-13. Dice: Make a class Die with one attribute called sides, which has a default value of 6. Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. Make a 6-sided die and roll it 10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""

class Dice:
    """
    Dice class
    """
    from random import randint

    def __init__(self, val = 6):
        self.val = val

    def roll_die(self):
        print(self.randint(1, self.val))

my_dice = Dice()
my_dice.roll_die()

my_dice1 = Dice(10)
my_dice1.roll_die()

my_dice2 = Dice(20)
my_dice2.roll_die()
print()


# Exercise 2
"""
9-14. Lottery: Make a list or tuple containing a series of 10 numbers and five letters. Randomly select four numbers or letters from the list and print a message saying that any ticket matching these four numbers or letters wins a prize.
"""
from random import choice

class Lottery:
    """
    Define lottery class
    """
    def __init__(self, var):
        self.var = var

    def select_ticket(self):
        ticket_number = []
        while len(ticket_number) < 4:
            pulled_item = choice(self.var)

            "Only add if not already present"
            if pulled_item not in ticket_number:
                ticket_number.append(pulled_item)
        return ticket_number

    def print_ticket(self):
        print(f"Any ticket matching these four numbers or letters wins a prize: {self.select_ticket()}\n")

alist = list(range(1,11)) + [chr(x) for x in range(ord('a'), ord('e') + 1)]
lottery = Lottery(alist)
lottery.select_ticket()
lottery.print_ticket()

# Exercise 3
"""
9-15. Lottery Analysis: You can use a loop to see how hard it might be to win the kind of lottery you just modeled. Make a list or tuple called my_ticket. Write a loop that keeps pulling numbers until your ticket wins. Print a message reporting how many times the loop had to run to give you a winning ticket.
"""

my_ticket = ("b", 74, "m", 98)

"""
Run the loop to generate a random ticket.
Check if elements of the ticket match my_ticket.
Keep a count of the loop.
"""

count = 0
while True:
    count += 1
    gen_ticket = Lottery(alist)
    new_ticket = gen_ticket.select_ticket()
    if my_ticket == new_ticket:
        print("found the ticket")
        break
    elif count >= 1_000_000:
        print("Count exceeded 1_000_000. Breaking out of the loop.")
        break
print()
# So much better code from https://ehmatthes.github.io/pcc_2e/solutions/chapter_9/#9-15-lottery-analysis

from random import choice

def get_winning_ticket(possibilities):
    """Return a winning ticket from a set of possibilities."""
    winning_ticket = []

    # Don't get the chars repeated
    while len(winning_ticket) < 4:
        pulled_item = choice(possibilities)

        # add items that aren't already pulled
        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)
    return winning_ticket

def check_ticket(played_ticket, winning_ticket):
    # check all elments in the played ticket. If not in winning ticket, then False
    # This doesn't seem to check the sequence and focuses on just having the elements which could be in any order.
    # Exercises content doesn't specify that.
    for element in played_ticket:
        if element not in winning_ticket:
            return False

    # We must have a winning ticket
    return True

def make_random_ticket(possibilities):
    """Return a random ticket from a set of possibilities."""
    ticket = []
    # Don't get the chars repeated
    while len(ticket) < 4:
        pulled_item = choice(possibilities)

        # add items that aren't already pulled
        if pulled_item not in ticket:
            ticket.append(pulled_item)
    return ticket

possibilities = list(range(1,11)) + [chr(x) for x in range(ord('a'), ord('e') + 1)]
winning_ticket = get_winning_ticket(possibilities)

plays = 0
won = False

# max tries
max_tries = 1_000_000

while not won:
    new_ticket = make_random_ticket(possibilities)
    won = check_ticket(new_ticket, winning_ticket)
    plays += 1
    if plays >= max_tries:
        break

if won:
    print("We have a winning ticket!")
    print(f"Your ticket: {new_ticket}")
    print(f"Your ticket: {winning_ticket}")
    print(f"It only took {plays} tries to win!")
else:
    print(f"Tried {plays} times, without pulling a winner. :(")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")