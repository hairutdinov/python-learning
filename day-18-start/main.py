import turtle
from turtle import Turtle, Screen
from turtle_colors import COLORS
import random


def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

turtle.colormode(255)
tim = Turtle()
tim.shape('classic')
tim.speed('fastest')
def draw_spirograph(size_of_gep):
    for _ in range(int(360 / size_of_gep)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gep)

draw_spirograph(3)
screen = Screen()
screen.exitonclick()
