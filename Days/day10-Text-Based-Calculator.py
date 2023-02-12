#!/usr/bin/env python
# This course follows the 100-days-of-code-challenge from the udemy course : 100-days-of-code
# While some content will be remedial, basic, etc. I feel it best serves me to do all task and complete my 100 days
# Justin Powell

# This day is focused on the output of functions.
# The end-game for this project is to make a text-based calculator
# I can imagine a general design for this to begin with using functions
num_1 = 5
num_2 = 10

operations = {
    "+": num_1 + num_2,
    "-": num_1 - num_2,
    "*": num_1 * num_2,
    "/": num_1 / num_2,
}

for key in operations:
    print(operations[key])