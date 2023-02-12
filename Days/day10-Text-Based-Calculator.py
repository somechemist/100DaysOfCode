#!/usr/bin/env python
# This course follows the 100-days-of-code-challenge from the udemy course : 100-days-of-code
# While some content will be remedial, basic, etc. I feel it best serves me to do all task and complete my 100 days
# Justin Powell

# This day is focused on the output of functions.
# The end-game for this project is to make a text-based calculator
# I can imagine a general design for this to begin with using functions
from os import system
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    carry = False
    c = a / b
    if a % b != 0:
        d = a % b
        modu = True
    if modu == True:
        e = f"{c} MOD {d}"
    else:
        e = c
    return e

def error():
    print("An error has occured.\nPlease ensure your entries are correct and try again.")
    exit(0)

num_1 = float(input("Enter the first value:\n"))
num_2 = float(input("Enter the Second value:\n"))


operations = {
    "+": addition(num_1, num_2),
    "-": subtraction(num_1, num_2),
    "*": multiplication(num_1, num_2),
    "/": division(num_1, num_2),
}
try:
    print("Choose one of the following operations:")
    for key in operations:
        print(key)
    operator = input("")
    for key in operations:
        if key == operator:
            system('clear')
            print(f"Result: {operations[key]}")

except:
    error()