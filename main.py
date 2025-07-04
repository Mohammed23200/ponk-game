from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("ponk")
screen.setup(height=600,width=800)
screen.tracer(0)
paddle_left = Paddle(position=-350)
paddle_right = Paddle(position=350)
ball = Ball()
score = ScoreBoard()
screen.listen()
screen.onkey(key='Up',fun=paddle_right.up)
screen.onkey(key='Down',fun=paddle_right.down)
screen.onkey(key='w',fun=paddle_left.up)
screen.onkey(key='s',fun=paddle_left.down) 
is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()
    if ball.distance(paddle_right)<50 and ball.xcor()>320 or ball.distance(paddle_left)<50 and ball.xcor()<-320 :
        ball.bounce_h()
        ball.increas_speed()
    if ball.xcor()>380:
        ball.reset_position()
        score.l_point()
    if ball.xcor()<-380:
        ball.reset_position()
        score.r_point()
screen.exitonclick()
