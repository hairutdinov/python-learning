import turtle
import random
# import colorgram
from turtle import Turtle, Screen

# colors = colorgram.extract('image.png', 30)
# rgb_colors = list(map(lambda c: (c.rgb.r, c.rgb.g, c.rgb.b), colors))
# print(rgb_colors)

color_list = [(204, 155, 102), (70, 107, 128), (165, 77, 50), (123, 154, 168), (234, 238, 242), (236, 243, 240), (133, 173, 156), (115, 84, 100), (226, 196, 134), (53, 40, 25), (182, 92, 106), (154, 139, 79), (184, 128, 143), (23, 41, 54), (81, 166, 132), (82, 115, 112), (212, 101, 80), (232, 166, 163)]


turtle.colormode(255)
timmy = Turtle()
timmy.hideturtle()
timmy.speed('fastest')
timmy.penup()
timmy.setposition(-200, -100)
for _ in range(10):
    for _ in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.forward(50)
    timmy.setposition(-200, timmy.ycor() + 30)

screen = Screen()
screen.exitonclick()
print(screen.screensize())