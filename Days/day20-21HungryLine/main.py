from turtle import Screen
from time import sleep
from Classes import Line, Food, Score

# Initialize and configure the window
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Hungry-Line-Eats-Turtles-Game")
screen.listen()
screen.tracer(0)

running = True
cycles = 0
speed = 0.1

line = Line.Line_Sprite()
food = Food.Food()
current_score = Score.Scoreboard()

while running:
    screen.update()
    screen.onkey(key="Up", fun=line.up)
    screen.onkey(key="Left", fun=line.left)
    screen.onkey(key="Right", fun=line.right)
    screen.onkey(key="Down", fun=line.down)

    line.move_line()
    sleep(speed)

    # Consume food
    if line.head.distance(food) < 15:
        food.refresh()
        line.grow_line()
        current_score.update_score()

    # Check Rules
    running = line.rules()
    screen.update()

# game over screen
food.reset()
current_score.game_over()
screen.exitonclick()
