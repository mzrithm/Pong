from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)  # Turns off screen animation

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()

screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "a")
screen.onkey(left_paddle.move_down, "z")

screen.onkey(screen.bye, "q")

screen.listen()

game_is_on = True

while game_is_on:
    time.sleep(.05)
    screen.update()
    ball.move()
    ball.detect_collision()
