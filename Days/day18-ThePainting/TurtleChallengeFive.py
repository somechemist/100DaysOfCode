#!/usr/bin/env python
# This course follows the 100-days-of-code-challenge from the udemy course : 100-days-of-code
# While some content will be remedial, basic, etc. I feel it best serves me to do all task and complete my 100 days
# Justin Powell

# Make a spirograph with a number of circles, each with r=100

from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.colormode(255)
bob = Turtle()
angle = 1
max = int(360/angle)
bob.speed("fastest")

def make_circle(turns):
    bob.circle(100)
    bob.left(angle)



for x in range(max):
    bob.color(randint(0, 255), randint(0, 255), randint(0, 255))
    make_circle(x)

screen = Screen()
screen.exitonclick()