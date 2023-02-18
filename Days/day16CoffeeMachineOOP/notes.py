#!/usr/bin/env python
# This course follows the 100-days-of-code-challenge from the udemy course : 100-days-of-code
# While some content will be remedial, basic, etc. I feel it best serves me to do all task and complete my 100 days
# Justin Powell

# Objects are generated from classes and have attributes and do methods
# Classes are normally in pascal case

# We will use turtle graphics
from turtle import Turtle, Screen
# we are going to use a turtle class from this module
bob = Turtle()
print(bob)
bob.shape("turtle")
bob.color("AliceBlue")
bob.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
print(my_screen.canvwidth)
my_screen.exitonclick()