#!/usr/bin/env python

# This course follows the 100-days-of-code-challenge from the udemy course : 100-days-of-code
# While some content will be remedial, basic, etc. I feel it best serves me to do all task and complete my 100 days
# Justin Powell

# This is my pedantic solution to the fizzbuzz challenge

for num in range(1,101):
    fizz = False
    buzz = False
    if num % 3 == 0:
        fizz = True
    if num % 5 == 0:
        buzz = True
    if fizz and buzz:
        print("FizzBuzz")
    elif fizz:
        print("Fizz")
    elif buzz:
        print("Buzz")
    else:
        print(num)