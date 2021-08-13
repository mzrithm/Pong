from turtle import Screen
from paddle import Paddle

screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
# screen.tracer(0)  # Turns off screen animation

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "a")
screen.onkey(left_paddle.move_down, "z")
screen.listen()

game_is_on = True


screen.exitonclick()
