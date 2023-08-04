import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


player = Player()
screen.onkey(key="Up", fun=player.up)

scoreboard = Scoreboard()
car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            break

    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.increase_level()
        car_manager.increase_speed()
        continue
    car_manager.create_car()
    car_manager.delete_unused_cars()
    car_manager.move_cars()

screen.exitonclick()
