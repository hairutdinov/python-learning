from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(x=-290, y=270)
        self.update_level_title()

    def update_level_title(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_level_title()
