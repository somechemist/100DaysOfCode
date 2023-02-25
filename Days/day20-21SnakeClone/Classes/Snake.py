# This class will handle all aspects of the snake itself
from turtle import Turtle

MOVEMENT_SPEED = 20
STARTING_SIZE = 16
class Snake_Sprite:
    def __init__(self):

        self.snake = Turtle(shape="square")
        self.snake.pu()
        self.snake.color("white")
        self.snake_body = [self.snake]
        self.snake_size = 0
        self.Start_Snake(STARTING_SIZE)
        self.head = self.snake_body[0]

    def Start_Snake(self, size_added):
        global snake_size
        for body in range(size_added):
            self.snake_size += 20
            self.snake = Turtle(shape="square")
            self.snake.color("white")
            self.snake.pu()
            self.snake.goto(x=(int(self.snake.xcor() - self.snake_size)), y=0)
            self.snake_body.append(self.snake)
        return self.snake_size

    def MoveSnake(self):
        for body in range(len(self.snake_body) - 1, 0, -1):
            # Moving last element to next, and so on until we reach the first
            # Effectively, the body will always follow the head
            new_x = self.snake_body[body - 1].xcor()
            new_y = self.snake_body[body - 1].ycor()
            self.snake_body[body].goto(new_x, new_y)
        self.head.forward(MOVEMENT_SPEED)

    # React to consuming food
    def Grow_Snake(self):
        self.added = Turtle(shape="square")
        self.added.color("white")
        self.added.pu()
        self.snake_body.append(self.added)

    # Movement functions with rules
    def Up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def Left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def Down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def Right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    # Ruleset (Prints are for debugging)

    def Rules(self):
        if self.snake_body[0].xcor() >= 300 or self.snake_body[0].xcor() <= -300:
            print("Out of bounds X")
            return False
        if self.snake_body[0].ycor() >= 300 or self.snake_body[0].ycor() <= -300:
            print("Out of bounds Y")
            return False
        # This rule doesn't function properly yet
        for body in self.snake_body:
            if body == self.snake_body[0]:
                pass
            else:
                if int(self.head.ycor()) == int(body.ycor()) or int(self.head.ycor()) == int(body.ycor()):
                    print("Same Y")
                    if int(self.head.xcor()) == int(body.xcor()) or int(self.head.xcor()) == int(body.xcor()):
                        print("Same X")
                        return False
        return True
