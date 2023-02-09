#!/usr/bin/env python
# This course follows the 100-days-of-code-challenge from the udemy course : 100-days-of-code
# While some content will be remedial, basic, etc. I feel it best serves me to do all task and complete my 100 days
# Justin Powell
# Diagram from drawio
# asci art from ascii-art-generator.org
import os
from time import sleep
from random import randint
os.system('clear')

# game state
running = True
win = False
lose = False

# printables
banner = ('\n'
          '    _/    _/\n'
          '   _/    _/    _/_/_/  _/_/_/      _/_/_/   _/_/_/ _/_/     _/_/_/  _/_/_/\n'
          '  _/ _/ _/  _/    _/  _/    _/  _/     _/  _/   _/   _/  _/    _/  _/    _/\n'
          ' _/    _/  _/    _/  _/    _/  _/     _/  _/   _/   _/  _/    _/  _/    _/\n'
          '_/    _/    _/_/_/  _/    _/     _/_/_/  _/   _/   _/    _/_/_/  _/    _/\n'
          '                                    _/\n'
          '                               _/_/_/         By: Justin Powell\n')

wordlist = ["puncture", "saw", "jeans", "vase", "crabby", "ship", "ladybug", "sprout", "stormy", "grab", "teaching", "sable", "collar", "poison", "activity", "pushy", "improve", "charming", "post", "demonic", "wander", "even", "stitch", "deliver", "fish", "slow", "squeeze", "oven", "solid", "person", "juvenile", "sniff", "rebel", "act", "serve", "broken", "search", "arch", "fetch", "basin", "tap", "entertain", "mountain", "steel", "disgusted", "plain", "incompetent", "aunt", "zippy", "wretched", "cool", "false", "class", "ski", "yarn", "brainy", "anger", "attach", "boast", "bomb", "fumbling", "bawdy", "argue", "adorable", "able", "amuse", "liquid", "ambiguous", "hair", "shelf", "advertisement", "risk", "stone", "clever", "straw", "foolish", "dry", "release", "home", "place", "explode", "direful", "helpless", "reward", "natural", "spark", "honey", "detail", "outgoing", "bite-sized", "shoe", "slope", "perpetual", "hypnotic", "sick", "descriptive", "eatable", "queue", "homely", "fallacious"]

fail_0 = ('\n'
          '  +---+\n'
          '  |   |\n'
          '      |\n'
          '      |\n'
          '      |\n'
          '      |\n'
          '=========\n')
fail_1 = ('\n'
          '  +---+\n'
          '  |   |\n'
          '  O   |\n'
          '      |\n'
          '      |\n'
          '      |\n'
          '=========\n')
fail_2 = ('\n'
          '  +---+\n'
          '  |   |\n'
          '  O   |\n'
          '  |   |\n'
          '      |\n'
          '      |\n'
          '=========\n')
fail_3 = ('\n'
          '  +---+\n'
          '  |   |\n'
          '  O   |\n'
          ' /|   |\n'
          '      |\n'
          '      |\n'
          '=========\n')
fail_4 = ('\n'
          '  +---+\n'
          '  |   |\n'
          '  O   |\n'
          ' /|\  |\n'
          '      |\n'
          '      |\n'
          '=========\n')
fail_5 = ('\n'
          '  +---+\n'
          '  |   |\n'
          '  O   |\n'
          ' /|\  |\n'
          ' /    |\n'
          '      |\n'
          '=========\n')
fail_6 = ('\n'
          '  +---+\n'
          '  |   |\n'
          '  O   |\n'
          ' /|\  |\n'
          ' / \  |\n'
          '      |\n'
          '=========\n')

fail_array = [fail_0, fail_1, fail_2, fail_3, fail_4, fail_5, fail_6]

failcounter = 0

## Start Game ##
def start_game():
    failcounter = 0
    while failcounter < 7:
        print(banner)
        print(fail_array[failcounter])
        failcounter += 1
        sleep(0.5)
        os.system('clear')

def new_screen():
    os.system('clear')
    print(banner)
    print(fail_array[failcounter])
    pr_challenge = ""
    for l in challenge_word:
        pr_challenge += l + " "
    print(pr_challenge)

def win_con():
    os.system('clear')
    print("Congratulations!!!")
    exit(0)

def lose_con():
    os.system('clear')
    print("Game Over!")
    print(word_selected)
    exit(0)

start_game()
failcounter = 0

word_selected = wordlist[randint(0, len(wordlist) -1)]
selected_array = list(word_selected)
challenge_word = list("_"*len(list(word_selected)))
right_count = 0
while running:
    if not win and not lose:
        new_screen()
        round_pass = 0
        current_letter = 0
        my_letter = input("Please enter a letter.\n").strip()
        if len(my_letter) > 1:
            os.system('clear')
            print("Too many letters")
            sleep(1)
            round_pass += 1
            pass
        for n in selected_array:
            current_letter += 1
            if my_letter == n:
                challenge_word[current_letter - 1] = my_letter
                right_count += 1
                round_pass = 1
        if round_pass < 1:
                failcounter = failcounter + 1
        wd_test = ""
        for m in challenge_word:
            wd_test += m
        if wd_test.lower().strip() == word_selected.lower().strip():
            win = True
        elif failcounter == 6:
            lose = True
    elif win == True:
        win_con()
    else:
        lose_con()
