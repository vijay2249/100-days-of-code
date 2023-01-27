from turtle import Turtle, Screen


viz = Turtle()

def move_forward():
    viz.forward(30)

def move_backwards():
    viz.backward(30)


def clockwise():
    viz.setheading(viz.heading() + 10)

def counter_clockwise():
    viz.setheading(viz.heading() - 10)

screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="a", fun=counter_clockwise)
screen.exitonclick()