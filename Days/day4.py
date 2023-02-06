#!/usr/bin/env python

# This course follows the 100-days-of-code-challenge from the udemy course : 100-days-of-code
# While some content will be remedial, basic, etc. I feel it best serves me to do all task and complete my 100 days
# Justin Powell

# This module covers using the random library
# This code will create a rock-paper-scissors game in python
from random import randint

choice = input("Enter 1 for Rock, 2 for Paper or 3 for Scissors\n")
rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
rps_list = [rock, paper, scissors]

try:
    choice = int(choice)
except:
    print("invalid option")
    exit(1)

if type(choice) == int and choice > 0 and choice <= 3:
    print("You Chose:")
    print(rps_list[choice-1])
else:
    print("invalid option")
    exit(1)
comp_num = randint(1, 3)
comp_choice = rps_list[comp_num - 1]
print("The computer chose:")
print(comp_choice)
print("\n")
if (choice-1) == 0:
    if comp_num-1 == 0:
        print("Tie!")
    elif comp_num-1 == 1:
        print("You Lose :(")
    else:
        print("You Win :)")
elif (choice-1) == 1:
    if comp_num-1 == 0:
        print("You Win :)")
    elif comp_num-1 == 1:
        print("Tie!")
    else:
        print("You Lose :(")
else:
    if comp_num-1 == 0:
        print("You Lose :(")
    elif comp_num-1 == 1:
        print("You Win :)")
    else:
        print("Tie!")
