from turtle import Turtle


class Paddle(Turtle):  # Inherit all attributes of Turtle Class
    """A paddle object for interacting with ball in Pong game."""

    def __init__(self, x_value, y_value):
        """Initializes paddle object with width, height,
        and starting coordinates
        """
        super().__init__()  # Initialize Turtle Super class
        # self.hideturtle()
        self.resizemode("user")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.shape("square")
        self.color("white")
        self.setpos(x_value, y_value)
        # self.showturtle()

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)







