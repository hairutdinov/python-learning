from turtle import Turtle, Screen

tim = Turtle()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def counter_clockwise():
    tim.setheading(tim.heading() + 10)


def clockwise():
    tim.setheading(tim.heading() - 10)


def clear():
    tim.clear()
    tim.reset()


screen = Screen()
screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=counter_clockwise)
screen.onkeypress(key="d", fun=clockwise)
screen.onkeypress(key="c", fun=clear)
screen.exitonclick()
