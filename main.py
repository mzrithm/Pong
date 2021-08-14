from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
score = Turtle()
score.hideturtle()
score.pendown()
score.pencolor("white")

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


def scoreboard():
    message = f"Player One: {ball.right_hit}     Player Two: {ball.left_hit}"
    score.goto(0, 270)
    score.clear()
    score.write(message, False, align="center", font=("Arial", 20, "normal"))


game_is_on = True

while game_is_on:
    time.sleep(.05)
    screen.update()
    ball.move()
    if ball.ycor() == 300 or ball.ycor() == -300:
        ball.y_bounce()
    if ball.xcor() == 400:
        ball.right_hit += 1
        ball.reset()
        scoreboard()
    elif ball.xcor() == -400:
        ball.left_hit += 1
        ball.reset()
        scoreboard()
    if ball.xcor() == 340:
        if ball.ycor() < right_paddle.ycor() + 80:
            if ball.ycor() > right_paddle.ycor() - 80:
                ball.x_bounce()
    if ball.xcor() == -340:
        if ball.ycor() < left_paddle.ycor() + 80:
            if ball.ycor() > left_paddle.ycor() - 80:
                ball.x_bounce()
