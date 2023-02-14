#!/usr/bin/env python
# This course follows the 100-days-of-code-challenge from the udemy course : 100-days-of-code
# While some content will be remedial, basic, etc. I feel it best serves me to do all task and complete my 100 days
# Justin Powell

# Namespaces: Local vs Global scope
# Local scope exist within functions
# Global scope exist
# Anything you give a name to has a namespace.
# Blocks don't determine scope, just functions

# Give local and global variables different names generally

# To modify something in global scope via the local scope of a function
#
# my_global_var = 10
# def my_func():
#      global my_global_var
#
# OR (Because modifying globals isn't ideal)
# you could just return the local scope variable
#
# my_global_var = 10
# def my_func():
#      return my_global_var + 1

# Ideally, you will use globals as constants where the name is all uppercase
from random import randint
from os import system
from time import sleep

running = True

def get_number():
    print("I am thinking of a number between 1 and 100")
    return randint(1, 100)

def set_difficulty():
    ask = input("Would you like to play on 'easy' or 'hard'?\n")
    if ask == "hard" or ask == "HARD" or ask == "Hard":
        return 5
    else:
        return 10

def guess():
    print(f"You have {turns} turns remaining")
    return int(input("Pick a number between 1 and 100\n"))

while running == True:
    number = get_number()
    win = False
    if input("Would you like to play the number guessing game? y or n\n") != "n":
        turns = set_difficulty()
        while turns > 0:
            # This is the main logic, make a guess, check where it is compared to the number
            my_number = guess()
            if my_number > number:
                print("Too High")
                turns -= 1
            elif my_number < number:
                print("Too Low")
                turns -= 1
            else:
                win = True
                break

        if win == True:
            print("Good guess!")
            sleep(2)
            system('clear')
        else:
            print("Too bad!")
            sleep(2)
            system('clear')
    else:
        system('clear')
        running = False
