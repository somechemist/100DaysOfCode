#!/usr/bin/env python
import os
from time import sleep
os.system('clear')
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

while failcounter < 7:
    print(fail_array[failcounter])
    failcounter += 1
    sleep(0.5)
    os.system('clear')