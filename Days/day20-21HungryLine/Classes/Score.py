from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Sans', 20, 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.pu()
        self.goto(x=0, y=270)
        self.color("white")
        self.ht()
        self.update_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"SCORE: {self.score}", False, align=ALIGNMENT, font=FONT)
    def game_over(self):
        self.goto(x=0, y=0)
        self.color("red")
        self.write("!!!! GAME OVER !!!!", False, align=ALIGNMENT, font=FONT)

