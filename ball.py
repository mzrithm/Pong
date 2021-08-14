from turtle import Turtle


class Ball(Turtle):
    """Ball class..."""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setposition(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.right_hit = 0
        self.left_hit = 0
        print(self.heading())

    def move(self):
        # self.speed("slowest")
        self.setpos(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1

    def reset(self):
        self.setposition(0, 0)
        self.x_move *= -1
        self.y_move *= -1
