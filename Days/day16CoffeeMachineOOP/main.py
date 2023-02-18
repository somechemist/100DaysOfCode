#!/usr/bin/env python
# This course follows the 100-days-of-code-challenge from the udemy course : 100-days-of-code
# While some content will be remedial, basic, etc. I feel it best serves me to do all task and complete my 100 days
# Justin Powell
# She made all of the Class files for this project,
# They have been gitignored so you will not be able to run this

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from time import sleep
from os import system

my_menu = Menu()
my_money_machine = MoneyMachine()
my_coffee_maker = CoffeeMaker()
running = True


def get_reports():
    clear_Screen(0)
    my_coffee_maker.report()
    my_money_machine.report()

def clear_Screen(stime):
    sleep(stime)
    system('clear')

def get_drink(type):
    drink = my_menu.find_drink(type)
    print(drink.name)
    if my_money_machine.make_payment(drink.cost):
        pass
    else:
        clear_Screen(2)
        return
    if my_coffee_maker.is_resource_sufficient(drink):
        my_coffee_maker.make_coffee(drink)
        clear_Screen(2)
        return
    else:
        clear_Screen(2)
        return

while running:
    choice = input(f"What would you like to drink?\n{my_menu.get_items()}\n")
    if choice == "espresso" or choice == "e" or choice == "E" or choice == "Espresso":
        get_drink("espresso")
    elif choice == "cappuccino" or choice == "c" or choice == "C" or choice == "Cappuccino":
        get_drink("cappuccino")
    elif choice == "latte" or choice == "l" or choice == "L" or choice == "Latte":
        get_drink("latte")
    elif choice == "report":
        get_reports()
    elif choice == "exit" or choice == "quit":
        running = False
    else:
        print("Invalid Selection!\nPlease Try Again")
        clear_Screen(2)
