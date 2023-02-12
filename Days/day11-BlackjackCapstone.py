#!/usr/bin/env python
# This course follows the 100-days-of-code-challenge from the udemy course : 100-days-of-code
# While some content will be remedial, basic, etc. I feel it best serves me to do all task and complete my 100 days
# Justin Powell

# This version of 21 will use a simplified deck and modified to rules to make it easier to code.
# The principles of the game will be the same.

from random import randint
from os import system
from time import sleep

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_card():
    return randint(0, len(cards) - 1)
def initial_deal():
    player_hand.append(cards[draw_card()])
    dealer_hand.append(cards[draw_card()])
    player_hand.append(cards[draw_card()])
    dealer_hand.append(cards[draw_card()])
    print(f"Your hand:   {player_hand[0]}, {player_hand[1]}")
    print(f"Dealer Hand: {dealer_hand[0]}, *")

def player_turn():
    player_hand.append(cards[draw_card()])
    print(player_hand)
    hand_string = ""
    for i in player_hand:
        i = str(i)
        hand_string += i + " "
    print(f"Your hand: {hand_string}")


def dealer_turn():
    print(f"Dealer's Hand: {dealer_hand[0]}, {dealer_hand[1]}")
    dealer_playing = True
    while dealer_playing == True:
        x = 0
        for i in dealer_hand:
            x += i
        if x < 16:
            system('clear')
            dealer_hand.append(cards[draw_card()])
            print(f"Your Hand:  {player_hand}")
            print(f"Dealer Hand:{dealer_hand}")
        elif x > 21:
            for i in range(0, len(dealer_hand) - 1):
                if dealer_hand[i] == 11:
                    dealer_hand[i] = 1
            y = 0
            for u in dealer_hand:
                y += u
            if y > 21:
                print("DEALER BUSTED!!!")
                print("You win")
                sleep(5)
                playing == False
                return playing
            else:
                break
        else:
            dealer_playing = False
    win_con()



def win_con():
    system('clear')
    x = 0
    y = 0
    for i in player_hand:
        x += i
        player_sum = x
    for i in dealer_hand:
        y += i
    if x > y:
        print(f"Your total:    {x}")
        print(f"Dealer total:  {y}")
        print(f"Player Wins!")
    elif x == y:
        print(f"Your total:    {x}")
        print(f"Dealer total:  {y}")
        print("DRAW!!!")
    else:
        print(f"Your total:    {x}")
        print(f"Dealer total:  {y}")
        print("Dealer Wins!")
    sleep(5)
    playing = False
    return playing


while True:
    # Make the game exitable
    system('clear')
    if input("Would you like to play 21? 'y' or 'n'\n") != "y":
        print("Thank you for playing")
        exit(0)
    # Blackjack game
    else:
        system('clear')
        player_hand = []
        dealer_hand = []
        playing = True
        initial_deal()
        while playing == True:
            x = 0
            for i in player_hand:
                x += i
            print(x)
            if x > 21:
                for i in range(0, len(player_hand) - 1):
                    if player_hand[i] == 11:
                        player_hand[i] = 1
                y = 0
                for u in player_hand:
                    y += u
                if y > 21:
                    system('clear')
                    print("BUSTED!!!")
                    print("You Lose!")
                    sleep(1)
                    playing == False
                    break
                else:
                    break
            if input("Would you like to draw another card? 'y' or 'n'\n") != "y":
                dealer_turn()
                playing = False
            else:
                player_turn()
