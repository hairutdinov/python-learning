import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.move_distance = STARTING_MOVE_DISTANCE
        self.all_cars = []

    def create_car(self):
        if random.randint(1, 6) != 1:
            return
        car = Turtle("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.setheading(180)
        car.color(random.choice(COLORS))
        car.penup()
        car.goto((300, random.randint(-250, 250)))
        self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.move_distance)

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT

    def delete_unused_cars(self):
        for idx in range(0, len(self.all_cars)-1):
            car = self.all_cars[idx]
            if car.xcor() < -350:
                car.reset()
                car.hideturtle()
                del self.all_cars[idx]

