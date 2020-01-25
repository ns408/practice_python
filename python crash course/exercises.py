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
        for item in range(0,4):
            ticket_number += str(choice(self.var))
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

