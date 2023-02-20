#!/usr/bin/env python
# This course follows the 100-days-of-code-challenge from the udemy course : 100-days-of-code
# While some content will be remedial, basic, etc. I feel it best serves me to do all task and complete my 100 days
# Justin Powell

# Make a spirograph with a number of circles, each with r=100

from turtle import Turtle, Screen
from random import randint

# Control the while loop
running = True
# Initialize the screen object and set the color mode
screen = Screen()
screen.colormode(255)
# Used to control movement
movement = 100
size = movement / 2
offset = movement * 2
# Initialize the dot varaible and set its speed
dot = Turtle()
dot.speed("fastest")
# Set up the initial positioning
y_pos = 0 - ((screen.window_height() / 2) - movement)
x_pos = 0 - ((screen.window_width() / 2) - offset)
dot.pu()
dot.setx(x_pos)
dot.sety(y_pos)
dot.pd()

def draw_dots(y):
    # if we are at the end of the line:
    if dot.xcor() >= ((screen.window_width() / 2) - movement):
        # if we are at the top of the page, stop
        if dot.ycor() >= ((screen.window_height() / 2) - offset):
            return False
        # else move up a row
        else:
            dot.pu()
            dot.end_fill()
            dot.setx(0 - ((screen.window_width() / 2) - offset))
            y += offset
            dot.sety(y)
            # adjust the input
            global y_pos
            y_pos = y
            dot.pd()
            dot.begin_fill()
    # draw the dot
    dot.circle(size)
    dot.pu()
    dot.forward(offset)
    dot.pd()
    return True




while running:
    rand_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    dot.color(rand_color)
    dot.begin_fill()
    dot.fillcolor(rand_color)
    running = draw_dots(y_pos)
    dot.end_fill()


screen = Screen()
screen.exitonclick()