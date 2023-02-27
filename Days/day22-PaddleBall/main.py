from turtle import Screen
from Classes import Paddle, Ball, Score
from time import sleep
from random import choice

running = True
scoreboard = Score.Scoreboard()
distance_rule = 30
clock = 0.0018
heading_var = (-5, 5)

# Initialize and configure the window
screen = Screen()
screen.setup(width=1200, height=800)
screen.bgcolor("green")
screen.title("Paddle Ball Game")
screen.listen()
screen.tracer(0)

player = Paddle.Paddles()

ball = Ball.TennisBall()

while running:
    screen.update()
    screen.onkey(key='w', fun=player.one_up)
    screen.onkey(key='s', fun=player.one_down)
    screen.onkey(key='Up', fun=player.two_up)
    screen.onkey(key='Down', fun=player.two_down)

    sleep(clock)

    ball.move_ball()

    if ball.distance(player.player_two) < distance_rule:
        ball.setheading(choice(heading_var) + int(ball.heading()))
        ball.bounce()

    if ball.distance(player.player_one) < distance_rule:
        ball.setheading(choice(heading_var) + int(ball.heading()))
        ball.bounce()

    if ball.ycor() < -330:
        ball.setheading(45)

    if ball.ycor() > 330:

        ball.setheading(135)

    if ball.xcor() < -530:
        running = scoreboard.update_player_two_score()
        player.paddle_reset()
        sleep(1)
        ball.reset()

    if ball.xcor() > 530:
        running = scoreboard.update_player_one_score()
        player.paddle_reset()
        sleep(1)
        ball.reset()


screen.exitonclick()
