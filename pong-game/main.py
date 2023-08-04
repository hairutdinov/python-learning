import time
from turtle import Turtle, Screen
from dash import Dash
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

CANVAS_HEIGHT = 600
CANVAS_WIDTH = 800

screen = Screen()
screen.title("Pong Game")
screen.setup(width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
screen.bgcolor("black")
screen.tracer(0)

dash = Dash(CANVAS_HEIGHT)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)


game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()
    # detect bounce with both paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()
    # detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    # detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.update()
screen.exitonclick()
