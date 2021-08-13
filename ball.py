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
        self.speed("slowest")
        self.setpos(self.xcor() + 10, self.ycor() + 10)

    def detect_collision(self):
        if self.ycor() == 300 or self.ycor() == -300:
            self.color("red")
            angle = self.towards(0, 0)
            print(angle)
            # new_heading = self.heading() - 45
            # self.setheading(new_heading)

