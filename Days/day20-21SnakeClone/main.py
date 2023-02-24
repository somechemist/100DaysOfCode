from turtle import Turtle, Screen
from time import sleep

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake-Style-Game")
screen.listen()
screen.tracer(0)

running = True
cycles = 0
speed = 0.2

snake = Turtle(shape="square")
snake.pu()
snake.color("white")

snake_body = [snake]
snake_size = 0


def grow_snake(size_added):
    global snake_size
    for body in range(size_added):
        snake_size += 20
        snake = Turtle(shape="square")
        snake.color("white")
        snake.pu()
        snake.goto(x=(int(snake.xcor() - snake_size)), y=0)
        snake_body.append(snake)
    return snake_size

def turn_right():
    snake_body[0].right(90)
    screen.update()

def turn_left():
    snake_body[0].left(90)
    screen.update()

grow_snake(2)
screen.onkey(key="Left", fun=turn_left)

while running:
    screen.onkey(key="Left", fun=turn_left)
    screen.onkey(key="Right", fun=turn_right)
    for body in range(len(snake_body) - 1, 0, -1):
        # Moving last element to next, and so on until we reach the first
        # Effectively, the body will always follow the head
        new_x = snake_body[body - 1].xcor()
        new_y = snake_body[body - 1].ycor()
        snake_body[body].goto(new_x, new_y)
    snake_body[0].forward(20)
    sleep(speed)
    screen.update()
    cycles += 1
    if cycles > 100:
        speed = 0.1
    if snake_body[0].xcor() >= 300 or snake_body[0].xcor() <= -300:
        print("Out of bounds")
        running = False
    if snake_body[0].ycor() >= 300 or snake_body[0].ycor() <= -300:
        print("Out of bounds")
        running = False

screen.exitonclick()
