#!/usr/bin/env python
# This course follows the 100-days-of-code-challenge from the udemy course : 100-days-of-code
# While some content will be remedial, basic, etc. I feel it best serves me to do all task and complete my 100 days
# Justin Powell

# Have to leverage event listeners to make this app do what we want

from turtle import Turtle, Screen
from random import randint

sketchy = Turtle()
screen = Screen()
screen.colormode(255)
screen.listen()


def move_forward():
    sketchy.forward(10)

def move_backward():
    sketchy.forward(-10)

def turn_left():
    sketchy.left(5)

def turn_right():
    sketchy.right(5)

def change_color():
    rand_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    sketchy.color(rand_color)

#needs a function
screen.onkey(key="Up", fun=move_forward)
screen.onkey(key="Down", fun=move_backward)
screen.onkey(key="Left", fun=turn_left)
screen.onkey(key="Right", fun=turn_right)
screen.onkey(key="c", fun=change_color)

screen.exitonclick()