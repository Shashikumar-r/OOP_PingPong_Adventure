from turtle import Screen
from paddle import Paddle
from ball import Ball
import time



# TODO 1:- create the screen
screen = Screen()
screen.tracer(0)
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("pong")


# TODO 2:-create a paddle
r_paddle = Paddle()
r_paddle.common_paddle()
r_paddle.goto(380, 0)
# TODO 3:-create a another paddle
l_paddle = Paddle()
l_paddle.common_paddle()
l_paddle.goto(-390,0)

r_paddle.r_paddle_move(screen)
l_paddle.l_paddle_move(screen)

# TODO 4:- create a ball
ball = Ball()
game_is_on = True
while game_is_on:
    screen.tracer(1)
    ball.ball_move()
    time.sleep(0.01)

    # TODO 5:- detect a collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bouncing_ball_y()

    # TODO 6:- detect a collision with paddle
    if ball.distance(r_paddle)< 50 and ball.xcor()> 320 or ball.distance(l_paddle)< 50 and ball.xcor()<-320 :
        ball.bouncing_ball_x()

    # TODO 6:- if ball voes outside of boundary rest_position
    if ball.xcor()>360:
        ball.reset_position()


screen.exitonclick()