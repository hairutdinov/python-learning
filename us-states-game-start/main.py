import turtle
import pandas
from turtle import Turtle, Screen

image = "blank_states_img.gif"

screen = Screen()
screen.title("U.S. States Game")
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

guessed_states = []


while len(guessed_states) < 50:
    answer = screen.textinput(f"{len(guessed_states)}/50 States Correct", "What's another state's name?")
    if answer.lower() in data.state.str.lower().to_list():
        guessed_states.append(answer)
        s = data[data.state.str.lower() == answer.lower()]
        t = Turtle()
        t.hideturtle()
        t.penup()
        t.speed("fast")
        t.goto(int(s.x.item()), int(s.y.item()))
        t.write(s.state.item())




screen.exitonclick()