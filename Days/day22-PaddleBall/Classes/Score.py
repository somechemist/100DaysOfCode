from turtle import Turtle

ALIGNMENT = "center"
FONT = ('ariel', 70, 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player_one_score = -1
        self.player_two_score = -1
        self.pu()
        self.speed("fastest")
        self.goto(x=0, y=315)
        self.color("white")
        self.ht()
        self.update_player_one_score()
        self.update_player_two_score()



    def update_player_one_score(self):
        self.player_one_score += 1
        self.clear()
        self.write_score()
        if self.player_one_score >= 12:
            self.game_over()
            return False
        return True

    def update_player_two_score(self):
        self.player_two_score += 1
        self.clear()
        self.write_score()
        if self.player_two_score >= 12:
            self.game_over()
            return False
        return True

    def write_score(self):
        self.write(f"{self.player_one_score}       {self.player_two_score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.color("red")
        self.write("!!!! MATCH OVER !!!!", False, align=ALIGNMENT, font=FONT)