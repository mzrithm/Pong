from turtle import Turtle


class Ball(Turtle):
    """Ball class..."""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setposition(0, 0)

    def move(self):
        self.setheading(45)
        self.speed("slow")
        self.forward(10)

