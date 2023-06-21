from turtle import Turtle
SIDES = (0, 1)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def score(self, side):
        print(SIDES[0] == side)
        print(SIDES[1] == side)
        if side == SIDES[0]:
            self.l_score += 1
        else:
            self.r_score += 1

        self.update_scoreboard()
