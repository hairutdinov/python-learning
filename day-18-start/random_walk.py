from turtle import Turtle, Screen
from turtle_colors import COLORS
import random

tim = Turtle()
tim.shape('classic')

directions = []
for i in range(0, 4):
    directions.append(90 * i)


for _ in range(200):
    color = random.choice(COLORS)
    tim.pen(fillcolor=color, pencolor=color, pensize=10, speed=8)
    tim.forward(25)
    tim.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()
