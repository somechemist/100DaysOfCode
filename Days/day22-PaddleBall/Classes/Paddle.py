from turtle import Turtle

class Paddles:
    def __init__(self):
        # Draw the court
        self.court()

        # Make the paddles
        self.paddle_size = 0
        self.player_one = Turtle(shape="square")
        self.player_one.pu()
        self.player_one.color("white")
        self.player_one_body = [self.player_one]
        self.player_one.speed("fastest")
        self.player_one.setheading(90)
        self.player_one.shapesize(stretch_wid=0.75, stretch_len=3.75)

        self.player_two = Turtle(shape="square")
        self.player_two.pu()
        self.player_two.color("white")
        self.player_two_body = [self.player_two]
        self.player_two.speed("fastest")
        self.player_two.setheading(90)
        self.player_two.shapesize(stretch_wid=0.75, stretch_len=3.75)

        self.paddle_reset()

    def court(self):
        self.divider = Turtle(shape="square")
        self.divider.pu()
        self.divider.color("grey")
        self.divider.shapesize(stretch_wid=40, stretch_len=0.2)

        for x in (-550, 550):
            self.score_divider = Turtle(shape="square")
            self.score_divider.pu()
            self.score_divider.color("grey")
            self.score_divider.shapesize(stretch_wid=40, stretch_len=0.1)
            self.score_divider.goto(x=x, y=0)

        for y in (-330, 330):
            self.bounce_divider = Turtle(shape="square")
            self.bounce_divider.pu()
            self.bounce_divider.color("grey")
            self.bounce_divider.shapesize(stretch_wid=0.1, stretch_len=60)
            self.bounce_divider.goto(x=0, y=y)

    def one_up(self):
        if self.player_one.ycor() < 330:
            self.player_one.forward(20)

    def one_down(self):
        if self.player_one.ycor() > -330:
            self.player_one.forward(-20)

    def two_up(self):
        if self.player_two.ycor() < 330:
            self.player_two.forward(20)

    def two_down(self):
        if self.player_two.ycor() > -330:
            self.player_two.forward(-20)

    def paddle_reset(self):
        self.player_one.goto(x=-530, y=0)
        self.player_two.goto(x=520, y=0)

