#!/usr/bin/env python
# This course follows the 100-days-of-code-challenge from the udemy course : 100-days-of-code
# While some content will be remedial, basic, etc. I feel it best serves me to do all task and complete my 100 days
# Justin Powell

from turtle import Turtle, Screen

bob = Turtle()
move = 10
for x in range(15):
    bob.forward(move)
    bob.pu()
    bob.forward(move)
    bob.pd()



screen = Screen()
screen.exitonclick()