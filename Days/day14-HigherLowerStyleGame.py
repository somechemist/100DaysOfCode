#!/usr/bin/env python
# This course follows the 100-days-of-code-challenge from the udemy course : 100-days-of-code
# While some content will be remedial, basic, etc. I feel it best serves me to do all task and complete my 100 days
# Justin Powell

# Using the data file she provides, you will mimic higher-lower with a list of (now outdated) instagram stats

from random import randint
from day14_data import data
from time import sleep
from os import system

#globals
running = True
score = 0

# Create a new challenge for the user
def getChallenge():
    #Select the random challengers
    firstOption = data[randint(0, len(data) - 1)]
    secondOption = data[randint(0, len(data) - 1)]

    #If the challengers are the same, pick again
    test = True
    while test == True:
        if firstOption['name'] == secondOption['name']:
            secondOption = data[randint(0, len(data) - 1)]
        else:
            test = False

    # Game time
    print("Who had more followers?")
    print(f"Enter '1' for {firstOption['name']}, who is a(n) {firstOption['description']} from {firstOption['country']}?")
    print(f"Enter '2' for {secondOption['name']}, who is a(n) {secondOption['description']} from {secondOption['country']}?")

    # Handle bad input
    try:
        choice = int(input(":: "))
    except:
        print(f"Invalid input, {firstOption['name']} has been chosen instead")
        choice = 1

    # Lets see how they did
    return evalResponse(choice, firstOption, secondOption)

# Evaluate response
def evalResponse(choice, firstOption, secondOption):
    if choice == 1:
        if firstOption['follower_count'] > secondOption['follower_count']:
            return False
        else:
            return True
    else:
        if firstOption['follower_count'] < secondOption['follower_count']:
            return False
        else:
            return True

# main
while running == True:
    if getChallenge() == False:
        system('clear')
        print("Great job! Let's play again!!")
        sleep(3)
        system('clear')
        score += 1
    else:
        system('clear')
        print("Oh no! You picked wrong!\nPlay again later!")
        print(f"Your score was: {score}")
        sleep(3)
        system('clear')
        running = False