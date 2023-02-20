#!/usr/bin/env python
# This course follows the 100-days-of-code-challenge from the udemy course : 100-days-of-code
# While some content will be remedial, basic, etc. I feel it best serves me to do all task and complete my 100 days
# Justin Powell

# Have it draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon

from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.colormode(255)
bob = Turtle()
mv = 100
max = 20

bob.pu()
bob.sety(-250)
bob.pd()
def draw_shape(turns):
    for x in range(turns):
        bob.forward(mv)
        bob.left(360/turns)


for x in range(3, max):
    bob.fillcolor(randint(0, 255), randint(0, 255), randint(0, 255))
    draw_shape(x)

screen = Screen()
screen.exitonclick()