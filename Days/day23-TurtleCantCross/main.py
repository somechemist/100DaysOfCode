from turtle import Screen

running = True

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("green")
screen.title("Turtle Can't Cross")
screen.listen()
screen.tracer(0)

screen.exitonclick()
