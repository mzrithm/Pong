from turtle import Screen
from paddle import Paddle

screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
# screen.tracer(0)  # Turns off screen animation

paddle = Paddle()
screen.onkey(paddle.move_up, "Up")
screen.onkey(paddle.move_down, "Down")
screen.listen()

game_is_on = True


screen.exitonclick()
