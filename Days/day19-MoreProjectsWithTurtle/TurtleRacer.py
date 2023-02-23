#!/usr/bin/env python
# This course follows the 100-days-of-code-challenge from the udemy course : 100-days-of-code
# While some content will be remedial, basic, etc. I feel it best serves me to do all task and complete my 100 days
# Justin Powell

from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Racer")
user_bet = screen.textinput(title="Place your bet!", prompt="Which color turtle will win?")
colors = ["red", "orange", "green", "blue", "purple"]
y_start_pos = [-100, -50, 0, 50, 100]
race = True

finish_line = Turtle(shape="arrow")
finish_line.pu()
finish_line.pensize(5)
finish_line.goto(x=230, y=-200)
finish_line.pd()
finish_line.left(90)
finish_line.forward(400)
finish_line.pu()
finish_line.goto(x=-300, y=0)

all_turtles = []
for turtle_index in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.pu()
    new_turtle.goto(x=-230, y=y_start_pos[turtle_index])
    all_turtles.append(new_turtle)

while race:
    random_distance = randint(0, 10)
    for turtle in all_turtles:
        random_distance = randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() >= 230:
            winning_turtle = turtle.color()[0]
            race = False

try:
    if str(winning_turtle).lower()[0] == user_bet.lower()[0]:
        screen.title(f"The {str(winning_turtle)} turtle wins! You win the bet!")
    else:
        screen.title(f"The {str(winning_turtle)} turtle wins! You lose the bet!")
except:
    screen.title("Bet was invalid!")

screen.exitonclick()
