from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.ht()
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(arg=f"{self.l_score}   |   {self.r_score }", align="center", font=("Times New Roman", 15, "bold"))

    def update_l_score(self):
        self.l_score += 1
        self.write_score()

    def update_r_score(self):
        self.r_score += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", align="center", font=("Times New Roman", 15, "bold"))
