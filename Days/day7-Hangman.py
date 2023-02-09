#!/usr/bin/env python
# This course follows the 100-days-of-code-challenge from the udemy course : 100-days-of-code
# While some content will be remedial, basic, etc. I feel it best serves me to do all task and complete my 100 days
# Justin Powell
# Diagram from drawio
# asci art from ascii-art-generator.org
# random words from randomlist.com
import os
from day7_printables import banner, fail_array
from day7_wordlist import wordlist
from time import sleep
from random import randint
os.system('clear')

# game state
running = True
win = False
lose = False

# Globals
word_selected = wordlist[randint(0, len(wordlist) -1)]
selected_array = list(word_selected)
challenge_word = list("_"*len(list(word_selected)))
failcounter = 0
bad_letters = []

## Start Game ##
def start_game():
    # Just for pretty
    graphic_counter = 0
    sleep_count = 0.05
    while graphic_counter < 7:
        print(banner)
        print(fail_array[graphic_counter])
        graphic_counter += 1
        sleep(sleep_count)
        sleep_count = sleep_count + 0.05
        os.system('clear')

def new_screen():
    # Resets the screen with updated information after each round
    os.system('clear')
    print(banner)
    print(fail_array[failcounter])
    # Makes the display for the challenge word
    pr_challenge = ""
    for l in challenge_word:
        pr_challenge += l + " "
    print(pr_challenge)
    if len(bad_letters) > 0:
        # Shows the incorrect guesses as it is annoying without this
        pr_bletters = ""
        for l in bad_letters:
            pr_bletters += l + " "
        print(f"Incorrect : {pr_bletters}")

def win_con():
    os.system('clear')
    print("!!!Congratulations!!!")
    print(f"{word_selected} was the word!")
    exit(0)

def lose_con():
    os.system('clear')
    print("!!!Game Over!!!")
    print(f"The word was: {word_selected}")
    exit(0)

start_game()

while running:
    if not win and not lose:
        new_screen()
        round_pass = 0
        current_letter = 0
        my_letter = input("Please enter a letter.\n").strip()
        if len(my_letter) > 1:
            # Handles putting in more than one character
            os.system('clear')
            print("Too many letters")
            sleep(1)
            round_pass += 1
            pass
        elif len(my_letter) == 0:
            # Handles pressing enter without a letter
            round_pass += 1
            pass
        try:
            # Should pass only if the number is a valid int. Thereby handling the accidental use of numbers
            my_letter = int(my_letter)
            os.system('clear')
            print("Invalid choice, letters ONLY!")
            sleep(1)
        except:
            # Makes a bad letter list to display
            for n in bad_letters:
                if n == my_letter:
                    os.system('clear')
                    print("You already guessed this letter incorrectly")
                    sleep(1)
                    round_pass += 1
                    pass
            # Checks if the letter exist in the word
            for n in selected_array:
                current_letter += 1
                if my_letter == n:
                    challenge_word[current_letter - 1] = my_letter
                    round_pass = 1
            # If the letter didn't occur, round_pass == 0 and therefore the letter failed 1 time
            if round_pass < 1:
                failcounter = failcounter + 1
                bad_letters += my_letter
            # Checks to see if you won
            wd_test = ""
            for m in challenge_word:
                wd_test += m
            if wd_test.lower().strip() == word_selected.lower().strip():
                # probably excessive... But seems safe
                win = True
            elif failcounter == 6:
                lose = True
    elif win == True:
        win_con()
    else:
        lose_con()
