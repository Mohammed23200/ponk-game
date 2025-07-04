from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.title("ponk")
screen.setup(height=600,width=800)
screen.tracer(0)
paddle_left = Paddle(position=-350)
paddle_right = Paddle(position=350)
ball = Ball()
screen.listen()
screen.onkey(key='Up',fun=paddle_right.up)
screen.onkey(key='Down',fun=paddle_right.down)
screen.onkey(key='w',fun=paddle_left.up)
screen.onkey(key='s',fun=paddle_left.down) 
is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()
screen.exitonclick()
