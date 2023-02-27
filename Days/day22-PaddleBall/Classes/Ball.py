from turtle import Turtle
from random import choice

STARTING_VECTORS = [180, 0]
SPEED = 1
class TennisBall(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.pu()
        self.speed("fastest")
        self.start()

    def start(self):
        self.setheading(choice(STARTING_VECTORS))

    def move_ball(self):
        self.forward(SPEED)

    def bounce(self):
        self.setheading(180 - self.heading())

    def reset(self):
        self.goto(0, 0)
        self.start()
