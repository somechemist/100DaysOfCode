from turtle import Screen
from time import sleep
from Classes import Snake

# Initialize and configure the window
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake-Style-Game")
screen.listen()
screen.tracer(0)

running = True
cycles = 0
speed = 0.2

snake = Snake.Snake_Sprite()

while running:
    screen.update()
    screen.onkey(key="Up", fun=snake.Up)
    screen.onkey(key="Left", fun=snake.Left)
    screen.onkey(key="Right", fun=snake.Right)
    screen.onkey(key="Down", fun=snake.Down)

    snake.MoveSnake()
    sleep(speed)
    # cycles += 1
    # if cycles > 100:
    #     speed = 0.1
    # if snake.snake_body[0].xcor() >= 300 or snake.snake_body[0].xcor() <= -300:
    #     print("Out of bounds")
    #     running = False
    # if snake.snake_body[0].ycor() >= 300 or snake.snake_body[0].ycor() <= -300:
    #     print("Out of bounds")
    #     running = False
    running = snake.Rules()

screen.exitonclick()
