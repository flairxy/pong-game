from turtle import Turtle
POSITIONS = [()]


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, y)

    def up(self):
        self.goto(self.xcor(), self.ycor() + 10)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 10)
