import os.path
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
FILE = "high_score.txt"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.high_score = self.get_high_score()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()

    def get_high_score(self):
        if os.path.exists(FILE):
            with open(FILE, "r") as hs:
                return int(hs.read())
        return 0

    def set_high_score(self, hs):
        self.high_score = hs
        with open(FILE, "w") as file:
            file.write(str(self.high_score))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.set_high_score(self.score)
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
