#!/usr/bin/env python
# This course follows the 100-days-of-code-challenge from the udemy course : 100-days-of-code
# While some content will be remedial, basic, etc. I feel it best serves me to do all task and complete my 100 days
# Justin Powell

# This lesson covers arguments vs. parameters, functions with inputs and the final project is to create a caeser cipher

# Simple Function with inputs

#def greet(name):
#    print(f"Hello {name}!")
#    print("How are you today?")
#    print("How is the weather?")
#name = input("What is your name?\n")
#greet(name)

# The argument is the data passed to function. The name of the variable that hold the argument is the parameter i.e. parameter = argument // bob = "Person"

# Function with more than 1 input
# def newFunction(name, location):
#    print(f"Hello {name}")
#    print(f"How is it in {location}")
#
#newFunction("Bob", location="London") #first argument is shown as positional while the second is showed as keyword

# The caeser Cipher will take a phrase as input, shift it by the number desired and print out an encrypted version

# Build the array to allow for upper and lower case letters
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for a in alpha:
    a = list(a.upper())
    alpha = alpha + a
for b in alpha:
    b = list(b)
    alpha = alpha + b

def encrypt(cipher, position):
    encrypted_string = ""
    cipher = list(cipher)
    for x in cipher:
        if x == " " or x == "." or x == "," or x == "!":
            encrypted_string = encrypted_string + x
        else:
            y = alpha.index(x)
            enc_char = alpha[y + position]
            encrypted_string = encrypted_string + enc_char
    print(encrypted_string)

def decode(cipher, position):
    unencrypted_string = ""
    cipher = list(cipher)
    for x in cipher:
        if x == " " or x == "." or x == "," or x == "!":
            unencrypted_string = unencrypted_string + x
        else:
            y = alpha.index(x)
            unenc_char = alpha[y - position]
            unencrypted_string = unencrypted_string + unenc_char
    print(unencrypted_string)

# Main
print()
print(f"Choose whether to encrypt or decode a message. Note: Position must be less than {int(len(alpha) / 2)}")
choose = input("To Encrypt, Enter 1 ... To Decode, Enter 2\n")
try:
    choose = int(choose)
except:
    print("\nInvalid selection\n")
    exit(0)
if choose == 1:
    cipher = input("What phrase would you like to encrypt?\n")
    try:
        cipher = int(cipher)
        print("\nInvalid selection\n")
        exit(0)
    except:
        pass
    try:
        position = int(input("What is the position shift?\n"))
        if position > 52:
            exit(0)
    except:
        print("\nInvalid selection\n")
        exit(0)
    encrypt(cipher, position)
elif choose == 2:
    cipher = input("What phrase would you like to encrypt?\n")
    try:
        cipher = int(cipher)
        print("\nInvalid selection\n")
        exit(0)
    except:
        pass
    try:
        position = int(input("What is the position shift?\n"))
        if position > 52:
            exit(0)
    except:
        print("\nInvalid selection\n")
        exit(0)
    decode(cipher, position)
else:
    print("Invalid selection")
    exit(0)
