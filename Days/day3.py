#!/usr/bin/env python

# This course follows the 100-days-of-code-challenge from the udemy course : 100-days-of-code
# While some content will be remedial, basic, etc. I feel it best serves me to do all task and complete my 100 days
# Justin Powell

# if condition:
#     code block 1
# else:
#     code block 2

# This project is a short choose your own adventure game
# The header is from the coding project, I did not make the graphic
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#This could benefit from a case statement and some more "fleshing out".... But this is sufficient to complete the task
choice = input("You find yourself at a fork in the road.\nTo you left you see a stone path.\nTo your right you see a cave.\nChoose 'L' for left or 'R' for right.\n")
if choice.upper() != "L":
    print("Oops you fell into a hole! \nGAME OVER")
    exit(0)

choice = input("\nYou come along a mighty stream!\n You can follow the banks and try to cross somewhere else or just swim.\nChoose 'W' to walk the banks or 'S' to swim.\n")
if choice.upper() != "W":
    print("You are attacked by viscious trout and killed\nGAME OVER")
    exit(0)

choice = input("\nYou find a cave.\nInside there are 3 mysterious doors of different colors\nChoose one:\n'R' for the red door,\n'Y' for the yellow door,\n'B' for the blue door.\n")
if choice.upper() == "Y":
    print("\n\n\n\nYou found the treasure!!!")
    print('''
    *******************************************************************************
              |                   |                  |                     |
     _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
              |                `"=._o`"=._      _`"=._                     |
     _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
              |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
     _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************
    ''')
    print("Congratulations!!!\n")
elif choice.upper() == "B":
    print("The room is dark, suddenly you are set upon by beast! You die!\nGAME OVER\n")
    exit(0)
elif choice.upper() == "R":
    print("As soon as you open the door, a massive file consumes you from the room!\nGAME OVER\n")
    exit(0)
else:
    print("You hesitate to make a choice.... In that time the cave moans and shudders. The Cave collapses!\nGAME OVER\n")
    exit(0)