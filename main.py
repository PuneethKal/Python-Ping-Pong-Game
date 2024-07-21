# Scoreboard
# pong class - tracks the pong and other features
# ball class - tracks the ball
# main file to hold everything

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Set up the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# Creating Paddles
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

# Create ball
ball = Ball()

# create scoreboard
scoreboard = Scoreboard()

# Movement of paddle
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Collision for Wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    # Collision for with paddle
    if ball.xcor() > 320 and r_paddle.distance(ball) < 50 or ball.xcor() < -320 and l_paddle.distance(ball) < 50:
        ball.paddle_bounce()

    # Detect when R paddle misses
    if ball.xcor() > 350:
        scoreboard.update_l_score()
        ball.reset_ball()

    # Detect when L paddle misses
    if ball.xcor() < -350:
        scoreboard.update_r_score()
        ball.reset_ball()

screen.exitonclick()
