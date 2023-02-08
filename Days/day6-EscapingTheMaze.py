#!/usr/bin/env python

# This course follows the 100-days-of-code-challenge from the udemy course : 100-days-of-code
# While some content will be remedial, basic, etc. I feel it best serves me to do all task and complete my 100 days
# Justin Powell

# day covers codeblocks, functions, while loops
# just like the built-in functions we have been using (int(), print(), etc.) we can make and call our own function()

# to make functions, you define them using the def keyword

#def my_function():
#    print("Hello")
#    print("Bye")
#
#my_function() #Call the function

# She demoes with reborgsworld

# She covers indentation in python. I like using the filesystem explorer to demonstrate indentation.
# don't mix tabs and spaces in python

# while loop
# while condition_is_true:
#     do thing

# So, the project is inside of a maze challenge on rebordsworld. You have a character inside a maze.
# They start at a random valid position
# they start facing one of four directions randomly
# You are given the functions needed to test if the way forward or to the right is clear
# You are given the function needed to turn left
# You are given the function to determine if you are at the final location

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def move_test():
    try:
        move()
    except:
        turn_left()


while not at_goal():
    if right_is_clear() == True:
        turn_right()
        move_test()
    elif front_is_clear() == True:
        move_test()
    else:
        turn_left()
        move_test()



