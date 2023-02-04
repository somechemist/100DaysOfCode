#!/usr/bin/env python

# This course follows the 100-days-of-code-challenge from the udemy course : 100-days-of-code
# While some content will be remedial, basic, etc. I feel it best serves me to do all task and complete my 100 days
# Justin Powell

# Covers different data types and how that can affect your program
# You can us _ as a comma to easily read large numbers
# a = 123_456_900
# print(a)

# You can convert types and check types by using methods like str() or type() and more.

# The project is a tip calculator
bill = input("The total bill is: $")
bill = float(bill)
patrons = input("Your party size is: ")
patrons = int(patrons)
tip = input("What percent would you like to tip? (15 recommended) %")
tip = int(tip)
if tip == 0:
    print("\n\nwow, don't be cheap")
    exit(0)
tip = tip/100

tot_bill = (bill * tip) + bill
if patrons == 0:
    tot_bill=round(tot_bill, 2)
    print(f"\n\nYour total bill is: ${tot_bill}")
else:
    spl_bill = round(tot_bill/patrons, 2)
    print(f"\n\nYour total bill is: ${spl_bill}")
exit(0)

# IIRC, round doesn't do well to round up. So this can be improved