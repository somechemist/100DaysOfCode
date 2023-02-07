#!/usr/bin/env python

# This course follows the 100-days-of-code-challenge from the udemy course : 100-days-of-code
# While some content will be remedial, basic, etc. I feel it best serves me to do all task and complete my 100 days
# Justin Powell

# Welcome message
# Ask for length of letters, then symbols and then numbers

# import and set our needed variables
from random import randint
password = ""
added = []
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# prompt the user
print("Welcome to the Password Generator")
num_letters = int(input("How many letters should this password have?\n"))
num_symbols = int(input("How many symbols should this password have?\n"))
num_numbers = int(input("How many numbers should this password have?\n"))

# Semi-Randomly assign values to the added array (Whatever runs first will be the first character type for the password, so that lacks randomness
for n in range(num_letters):
    if len(added) != 0:
        added.insert(randint(0, len(added) - 1), letters[randint(0, len(letters) - 1)])
    else:
        added.append(letters[randint(0, len(letters) - 1)])
for n in range(num_symbols):
    if len(added) != 0:
        added.insert(randint(0, len(added) - 1), symbols[randint(0, len(symbols) - 1)])
    else:
        added.append(symbols[randint(0, len(symbols) - 1)])
for n in range(num_numbers):
    if len(added) != 0:
        added.insert(randint(0, len(added) - 1), numbers[randint(0, len(numbers) - 1)])
    else:
        added.append(numbers[randint(0, len(numbers) - 1)])

# Now, lets convert added[] into a string called password
for n in added:
    password += n

print(password)