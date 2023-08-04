import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtles = {}


for idx in range(0, len(colors)):
    color = colors[idx]
    turtles[color] = Turtle(shape="turtle")
    turtles[color].penup()
    turtles[color].color(color)
    turtles[color].goto(x=-230, y=-60 + idx * 30)

if user_bet not in colors:
    print(f"There's no turtle with color '{user_bet}'.\nAvailable colors: {', '.join(colors)}")
    screen.bye()
    exit(0)
else:
    is_race_on = True

while is_race_on:
    for color in turtles:
        if turtles[color].xcor() >= 220:
            is_race_on = False
            print(color)
            break
        else:
            turtles[color].forward(random.randint(0, 10))

screen.exitonclick()
