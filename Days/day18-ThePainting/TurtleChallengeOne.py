#!/usr/bin/env python
# This course follows the 100-days-of-code-challenge from the udemy course : 100-days-of-code
# While some content will be remedial, basic, etc. I feel it best serves me to do all task and complete my 100 days
# Justin Powell

# draw a square

from turtle import Turtle, Screen

bob = Turtle()
bob.shape("turtle")
bob.color("red")

for x in range(4):
    bob.forward(200)
    bob.left(90)

screen = Screen()
screen.exitonclick()