from turtle import Turtle, Screen


class Paddle:
    """A paddle object for interacting with ball in Pong game."""

    def __init__(self):
        """Initializes paddle object with width, height,
        and starting coordinates
        """
        self.paddle = Turtle()
        self.x_pos = self.paddle.xcor()
        self.y_pos = self.paddle.ycor()
        self.paddle.hideturtle()
        self.paddle.resizemode("user")
        self.paddle.turtlesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.setpos(350, 0)
        self.paddle.showturtle()

    def move_up(self):
        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() + 20)

    def move_down(self):
        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() - 20)







