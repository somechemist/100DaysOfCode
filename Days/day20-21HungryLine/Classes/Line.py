# This class will handle all aspects of the snake itself
from turtle import Turtle

MOVEMENT_SPEED = 20
STARTING_SIZE = 2


class Line_Sprite:
    def __init__(self):

        self.Line = Turtle(shape="square")
        self.Line.pu()
        self.Line.color("white")
        self.line_body = [self.Line]
        self.line_size = 0
        self.Line.speed("fastest")
        self.start_line(STARTING_SIZE)
        self.head = self.line_body[0]

    def start_line(self, size_added):
        for body in range(size_added):
            self.line_size += 20
            self.Line = Turtle(shape="square")
            self.Line.color("white")
            self.Line.pu()
            self.Line.speed("fastest")
            self.Line.goto(x=(int(self.Line.xcor() - self.line_size)), y=0)
            self.line_body.append(self.Line)
        return self.line_size

    def move_line(self):
        for body in range(len(self.line_body) - 1, 0, -1):
            # Moving last element to next, and so on until we reach the first
            # Effectively, the body will always follow the head
            new_x = self.line_body[body - 1].xcor()
            new_y = self.line_body[body - 1].ycor()
            self.line_body[body].goto(new_x, new_y)
        self.head.forward(MOVEMENT_SPEED)

    # React to consuming food
    def grow_line(self):
        self.added = Turtle(shape="square")
        self.added.color("white")
        self.added.pu()
        self.Line.speed("fastest")
        self.line_body.append(self.added)

    # Movement functions with rules
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    # Ruleset (Prints are for debugging)

    def rules(self):
        if self.line_body[0].xcor() >= 300 or self.line_body[0].xcor() <= -300:
            print("Out of bounds X")
            return False
        if self.line_body[0].ycor() >= 300 or self.line_body[0].ycor() <= -300:
            print("Out of bounds Y")
            return False
        for body in self.line_body[1:]:
            if self.head.distance(body) < 10:
                    return False
        return True
