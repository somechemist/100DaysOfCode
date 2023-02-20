#!/usr/bin/env python
# This course follows the 100-days-of-code-challenge from the udemy course : 100-days-of-code
# While some content will be remedial, basic, etc. I feel it best serves me to do all task and complete my 100 days
# Justin Powell

# Make a random Walk

# Tuples are set in stone (They are immutable) (But you can convert them to a list)

from turtle import Turtle, Screen
from random import randint, choice

screen = Screen()
screen.colormode(255)
bob = Turtle()
mv = 25
max = 20
angle = 109.5
bob.pensize(7)

def random_walk(turns):
    for x in range(turns):
        list = [1, 2, 3]
        pick = choice(list)
        if pick == 1:
            bob.forward(mv)
        elif pick == 2:
            bob.right(angle)
            bob.forward(mv)
        else:
            bob.left(angle)
            bob.forward(mv)



for x in range(3, max):
    bob.color(randint(0, 255), randint(0, 255), randint(0, 255))
    random_walk(x)

screen = Screen()
screen.exitonclick()