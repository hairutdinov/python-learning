from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape('square')
        self.setheading(270)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)

    def up(self):
        if self.ycor() < 225:
            self.backward(20)

    def down(self):
        if -225 < self.ycor():
            self.forward(20)
        