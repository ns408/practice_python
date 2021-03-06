#!/usr/bin/env python

# create the file
with open('tmp_pi_digits.txt', "w") as file_object:
    file_object.write("""
3.1415926535
  8979323846
  2643383279
""")

# Reading an entire file
# file_reader.py
with open('tmp_pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())

# Reading line by line
filename = "tmp_pi_digits.txt"

with open(filename) as file_object:
    for line in file_object:
        # Using rstrip() on each line in the print() call eliminates these extra blank lines
        print(line.rstrip())

# Making a line of lines from a file

filename = "tmp_pi_digits.txt"

with open(filename) as file_object:
    # store the file’s lines in a list inside the block and then work with that list
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
print()

# Working with a file's content

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))
print()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# Is birthday contained in Pi?
import os.path as os_path
# pi_string.py
filename = os_path.dirname(os_path.realpath(__file__)) + "/tmp_pi_million_digits.txt"

# Oh well, let's just download the file, cause we can
import urllib.request, os

url = "https://raw.githubusercontent.com/ehmatthes/pcc_2e/master/chapter_10/pi_million_digits.txt"
if not os.path.exists(filename):
    urllib.request.urlretrieve(url, filename)

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

#birthday = input("Enter your birthday, in the form of ddmmyy: ")
#if birthday in pi_string:
#    print("Your birthday appears in the first million digits of pi!")
#else:
#    print("Your birthday does not appear in the first million digits of pi.")


# Try it yourself
"""
10.1 Learning Python
"""

# learning_python.txt

file_content = """
brown fox jumps
and does whatever
it needs to do."""

filename = "tmp_learning_python.txt"
with open(filename, "w") as file_object:
    file_object.write(file_content)
    file_object.write("This is to show how 'write()' doesn't add a whitespace or a new line.")

count = 0

# Reading the entire file
with open(filename) as file_object:
    print(file_object.read())

# Looping over the lines:
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# Storing the lines in a list:
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

"""
10-2 Learning C:
"""

# Doesn't seem to modify the variable
message = "I like"
print(message)
print(message.replace("like", "don't"))

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip().replace("and", "but"))
print()

# EXCEPTIONS

"""
ZeroDivisionError is an exception object.
"""
try:
    print(5/0)
except ZeroDivisionError:
    print("you can't divide by zero!")


"""
try except else

try block's successful execution is the dependency for else block
"""

try:
    answer = 5 / 1
except ZeroDivisionError:
    print("You can't divide by 0!")
else:
    print(answer)

# FileNotFoundError Exception

filename = "tmp_blah.txt"

try:
    with open(filename) as f:
        contents = f.read()
except FileNotFoundError:
    print(f"\nNo file with this name: {filename}.")

# Analysing text

# Splitting a string into a list of words
title = "Alice in Wonderland"
print(title.split())

import urllib.request
import os.path

filename = os.path.dirname(os.path.realpath(__file__)) + "/tmp_alice_in_wonderland.txt"
url = "https://www.gutenberg.org/files/11/11-0.txt"
if not os.path.exists(filename):
    urllib.request.urlretrieve(url, filename)

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"File {filename} not found.")
else:
    # Count the number of words in the file.
    words = contents.split()
    print(f"\nFile has words: {len(words)}")


# Working with multiple files

def count_word(filename):
    """Count the approx number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"File {filename} not found")
    else:
        words = contents.split()
        print(f"\nFile has words: {len(words)}")


import urllib
import os.path

url = "https://www.gutenberg.org/files/12/12.txt"
filename = os.path.dirname(os.path.realpath(__file__)) + "/tmp_" + "Through the Looking-Glass".lower().replace(' ', '_') + ".txt"
if not os.path.exists(filename):
    urllib.request.urlretrieve(url, filename)
count_word(filename)

try:
    print("\nI'm gonna try to divide 5 by 0 cause I am smart")
    print(5 / 0)
except ZeroDivisionError:
    print("So stupid.. 'pass'")
    pass
else:
    print("I managed to divide it by zero.")
print()

# Exercise:

"""
10-6. Addition: One common problem when prompting for numerical input occurs when people provide text instead of numbers. When you try to convert the input to an int, you’ll get a ValueError. Write a program that prompts for two numbers. Add them together and print the result. Catch the ValueError if either input value is not a number, and print a friendly error message. Test your program by entering two numbers and then by entering some text instead of a number.
10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop so the user can continue entering numbers even if they make a mistake and enter text instead of a number.
10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three names of cats in the first file and three names of dogs in the second file. Write a program that tries to read these files and print the contents of the file to the screen. Wrap your code in a try-except block to catch the FileNotFound error, and print a friendly message if a file is missing. Move one of the files to a dif- ferent location on your system, and make sure the code in the except block executes properly.
10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail silently if either file is missing.
10-10. Common Words: Visit Project Gutenberg (https://gutenberg.org/ ) and find a few texts you’d like to analyze. Download the text files for these works, or copy the raw text from your browser into a text file on your computer.
You can use the count() method to find out how many times a word or phrase appears in a string. For example, the following code counts the number of times 'row' appears in a string:
"""


#10-6
"""
try:
    print("Add two numbers to add")
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))
except ValueError:
    print("Please input numbers only")
else:
    print(num1 + num2)
"""

#10-7
"""
while True:
    try:
        print("Add two numbers to add or 'quit' to exit.")
        num1 = input("Please enter the first number: ")
        if str(num1).lower() == 'quit':
            print("Exiting the program now.")
            break
        num2 = input("Please enter the second number: ")
        if str(num2).lower() == 'quit':
            print("Exiting the program now.")
            break
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        print("Sorry, input numbers only\n")
    else:
        print(num1 + num2)
"""

# Create files for the next execise
import os.path
def create_file(content, filename):
    filename = os.path.dirname(os.path.realpath(__file__)) + "/" + filename
    with open(filename, "w") as f:
        f.write(content)

filename1 = "tmp_cats.txt"
content1 = """\
cat1
cat2
cat3\
"""
create_file(content1, filename1)

filename2 = "tmp_dogs.txt"
content2 = """\
dog1
dog2
dog3\
"""
create_file(content2, filename2)

# 10-8
import os.path
def read_file(param_filename):
    try:
        filename = os.path.dirname(os.path.realpath(__file__)) + "/" + param_filename
        with open(filename) as f:
            print(f.read())
    except FileNotFoundError:
        print(f"\nFile '{param_filename}' cannot be found. Please check the filename and path.\n")

read_file("tmp_cats.txt")
read_file("tmp_dogs.txt")
print()

# 10-9
import os.path
def read_file1(param_filename):
    """Fail silently if the file is missing"""
    try:
        filename = os.path.dirname(os.path.realpath(__file__)) + "/" + param_filename
        with open(filename) as f:
            print(f.read())
    except FileNotFoundError:
        pass

read_file1("tmp_cats1.txt")
read_file1("tmp_dogs.txt")
print()

# 10-10
"""
This gets downloaded previously in this script so just re-using.
"""
filename = os.path.dirname(os.path.realpath(__file__)) + "/tmp_alice_in_wonderland.txt"

def common_words(filename, param_word):
    try:
        word_count = 0
        with open(filename, encoding='utf-8') as f:
            for line in f.readlines():
                word_count += line.lower().count(param_word)
    except FileNotFoundError:
        pass
    else:
        print(f"Total number of '{param_word}': {word_count}")

common_words(filename, "the")
common_words(filename, "the ")

# Storing Data

# number_writer.py
import json
import os.path

numbers = [ 2, 3, 5, 7, 11, 13 ]

filename = os.path.dirname(os.path.realpath(__file__)) + '/' + 'tmp_numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)

# number_reader.py
with open(filename) as f:
    numbers = json.load(f)
print(numbers)

# remember_me.py
import json
import os.path

def greet_user():
    """
    Retrieve name if the file exits or ask for the name and dump it into a json file.
    """
    try:
        filename = os.path.dirname(os.path.realpath(__file__)) + '/' + 'tmp_username.json'
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("\nPlease enter the username: ")
        with open(filename, "w") as f:
            json.dump(username, f)
            print(f"\nhey {username}")
    except ValueError:
        print("Probably encountered an empty file")
    else:
        print(f"\nhey {username}")

greet_user()

# Refactor greet_user()

import json
def get_stored_username():
    """Get stored username if avaialble."""
    filename = os.path.dirname(os.path.realpath(__file__)) + '/' + 'tmp_username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    except ValueError:
        print("Probably encountered an empty file")
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = os.path.dirname(os.path.realpath(__file__)) + '/' + 'tmp_username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user1():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you: {username}")

greet_user1()


# 10-11
print()
import json
import os.path

#dump_favourite_number.py
def dump_favourite_number():
    try:
        filename = os.path.dirname(os.path.realpath(__file__)) + '/' + 'tmp_fav_number.json'
        number = input("Please enter your fav number: ")
        with open(filename, 'w') as f:
            json.dump(int(number), f)
    except ValueError:
        print(f"Value entered {number} is not a number")
    except FileNotFoundError:
        print(f"File {filename} doesn't exist")
    else:
        pass

#dump_favourite_number()

#load_favourite_number.py
def load_favourite_number():
    try:
        filename = os.path.dirname(os.path.realpath(__file__)) + '/' + 'tmp_fav_number.json'
        with open(filename) as f:
            number = json.load(f)
    except ValueError:
        print(f"File is empty")
    except FileNotFoundError:
        print(f"File {filename} doesn't exist")
    else:
        print(number)

load_favourite_number()
