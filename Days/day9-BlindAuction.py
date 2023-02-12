#!/usr/bin/env python
# This course follows the 100-days-of-code-challenge from the udemy course : 100-days-of-code
# While some content will be remedial, basic, etc. I feel it best serves me to do all task and complete my 100 days
# Justin Powell

# Dictionaries, list, nesting one in another or two of the same or whatever

# Dictionaries in python have a key and a value that is associated to that key

# {key: value, key2: value2} is a dictionary.

# to add to dictionary:
#dictionary_1["key3"] = "Value3"

#Initialize or clear
#dictionary_2 = {}

#edit
#dictionary_1["key3"] = "value4"

#Looping it
#for key in dictionary_1:
#   print(key) # its the key
#   print(dictionary_1[key]) # its the value

# nesting is like:
#{key: [list],
#key2: {dict},}

# You can nest dictionaries in a list, list in a dictionary and dictionary in a dictionary

from os import system
from time import sleep

bids = []
#Running = True

def add_bid(name, bid):
    system('clear')
    bids.append({
        name: bid
    })

def end_auction():
    system('clear')
    big_bid = []
    winner = ""
    win_bid = 0
    # This could really be simplified by just using a dictionary and just storing values, checking to see if the current bid > biggest so far
    for i in bids:
        for key in i:
            big_bid.append(i[key])
    for i in bids:
        for key in i:
            if i[key] == max(big_bid):
                winner = key
                win_bid = i[key]
    print(f"Congratulations to {winner} for a winning bid of ${win_bid}!")
    # program will not work well with identical bids. This is something else I could improve.
    exit(0)

while True:
    name = input("What is your name? ")
    end = "y"
    try:
        bid = int(input("What is your bid? $"))
        add_bid(name, bid)
        end = input("Is there anyone else looking to bid?\nEnter Yes or No.\n")
    except:
        print("Invalid bid")
        sleep(0.5)
        system('clear')
        pass
    if end.lower() == "yes" or end.lower() == "y":
        pass
    else:
        end_auction()
