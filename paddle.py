from turtle import Turtle, Screen


class Paddle:
    """A paddle object for interacting with ball in Pong game."""

    def __init__(self):
        """Initializes paddle object with width, height,
        and starting coordinates
        """
        self.x_pos = 350
        self.y_pos = 0
        self.paddle = Turtle()
        self.paddle.hideturtle()
        self.paddle.resizemode("user")
        self.paddle.turtlesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.setpos(self.x_pos, self.y_pos)
        self.paddle.showturtle()

    # def create_paddle(self):
    #     paddle = Turtle()
    #     paddle.hideturtle()
    #     paddle.resizemode("user")
    #     paddle.turtlesize(stretch_wid=5, stretch_len=1)
    #     paddle.penup()
    #     paddle.shape("square")
    #     paddle.color("white")
    #     paddle.setpos(350, 0)
    #     paddle.showturtle()

    def move_up(self):
        self.y_pos += 20
        self.paddle.goto(self.x_pos, self.y_pos)

    def move_down(self):
        self.y_pos -= 20
        self.paddle.goto(self.x_pos, self.y_pos)







