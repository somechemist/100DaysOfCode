#!/usr/bin/env python
# This course follows the 100-days-of-code-challenge from the udemy course : 100-days-of-code
# While some content will be remedial, basic, etc. I feel it best serves me to do all task and complete my 100 days
# Justin Powell

from os import system
from time import sleep

# globals
running = True

inventory = {
    'Water': 100, #ml
    'Milk': 50, #ml
    'Coffee': 76, #grams
    'Till': 2.50 #dollars
}

Currency = {
    'Quarters': 0.25,
    'Dimes': 0.10,
    'Nickles': 0.05,
    'Pennies': 0.01,
}

def restock():
    clear_Screen(0)
    print("Change inventory values: \nUse a negative like -1.0 to remove quantities \nUse 0 to leave alone")
    for key in inventory:
        inventory[key] += int(input(f"How much {key}?\n"))
    clear_Screen(1)



def clear_Screen(stime):
    sleep(stime)
    system('clear')
def gen_report():
    print("Inventory Report:")
    print(f"Water :: {inventory['Water']}ml")
    print(f"Milk :: {inventory['Milk']}ml")
    print(f"Coffee :: {inventory['Coffee']}g")
    print(f"Till :: ${inventory['Till']}")
    clear_Screen(4)


def get_latte():
    latte = {
        'Water': 200,
        'Milk': 150,
        'Coffee': 24,
        'Cost': 2.50,
    }
    if not check_supplies(latte['Water'], latte['Milk'], latte['Coffee']):
        print("Insufficient Inventory")
        return
    else:
        for key in latte:
            if key == "Cost":
                break
            inventory[key] -= latte[key]
    print("Please deposit change.")
    if calc_change(int(input("Quarters?\n")), int(input("Dimes?\n")), int(input("Nickles?\n")),
                   int(input("Pennies?\n")),
                   latte['Cost']) != False:
        print("Thank you for your business.")
    else:
        print("Insufficient funds deposited. \nPlease try again.")
    clear_Screen(2)
def get_espresso():
    espresso = {
        'Water': 50,
        'Milk': 0,
        'Coffee': 18,
        'Cost': 1.50,
    }
    if not check_supplies(espresso['Water'], espresso['Milk'], espresso['Coffee']):
        print("Insufficient Inventory")
        return
    else:
        for key in espresso:
            if key == "Cost":
                break
            inventory[key] -= espresso[key]
    print("Please deposit change.")
    if calc_change(int(input("Quarters?\n")), int(input("Dimes?\n")), int(input("Nickles?\n")),
                   int(input("Pennies?\n")),
                   espresso['Cost']) != False:
        print("Thank you for your business.")
    else:
        print("Insufficient funds deposited. \nPlease try again.")
    clear_Screen(2)

def get_cappucinno():
    cappucinno = {
        'Water': 250,
        'Milk': 100,
        'Coffee': 24,
        'Cost': 3.00,
    }
    if not check_supplies(cappucinno['Water'], cappucinno['Milk'], cappucinno['Coffee']):
        print("Insufficient Inventory")
        return
    else:
        for key in cappucinno:
            if key == "Cost":
                break
            inventory[key] -= cappucinno[key]
    print("Please deposit change.")
    if calc_change(int(input("Quarters?\n")), int(input("Dimes?\n")), int(input("Nickles?\n")),
                   int(input("Pennies?\n")),
                   cappucinno['Cost']) != False:
        print("Thank you for your business.")
    else:
        print("Insufficient funds deposited. \nPlease try again.")
    clear_Screen(2)

def calc_change(quarters, dimes, nickles, pennies, cost):
    clear_Screen(0)
    deposited = (Currency['Quarters'] * quarters) + (Currency['Dimes'] * dimes) + (Currency['Nickles'] * nickles) + \
                (Currency['Pennies'] * pennies)
    print(f"Total deposited: {deposited}")
    if deposited < cost:
        return False
    elif deposited > cost:
        change = deposited - cost
        inventory['Till'] += cost
        print(f"Returning ${round(change, 2)} difference.")
    else:
        inventory['Till'] += cost

def check_supplies(water, milk, coffee):
    if inventory['Water'] < water:
        return False
    elif inventory['Milk'] < milk:
        return False
    elif inventory['Coffee'] < coffee:
        return False
    else:
        return True

while running:
    choice = input("Would you like an espresso, cappuccino or latte?\n")
    if choice == "espresso" or choice == "e" or choice == "E" or choice == "Espresso":
        get_espresso()
    elif choice == "cappuccino" or choice == "c" or choice == "C" or choice == "Cappuccino":
        get_cappucinno()
    elif choice == "latte" or choice == "l" or choice == "L" or choice == "Latte":
        get_latte()
    elif choice == "report":
        gen_report()
    elif choice == "stock" or choice == "restock":
        restock()
    elif choice == "exit" or choice == "quit":
        running = False
    else:
        print("Invalid Selection!\nPlease Try Again")
        clear_Screen(2)
