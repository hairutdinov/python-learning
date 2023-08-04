from turtle import Turtle


class Dash(Turtle):
    def __init__(self, canvas_height):
        super().__init__()
        self.canvas_height = canvas_height
        self.color("white")
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.create()
        
    def create(self):
        self.goto(y=self.canvas_height, x=0)
        self.setheading(270)
        for i in range(self.canvas_height, self.canvas_height*-1, -10):
            if i % 20 == 0:
                self.penup()
            else:
                self.pendown()
            self.forward(10)

        