from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.goto(-230, 265)
        self.write(arg=f"Score:{self.score}", align="center", font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score:{self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"GAME OVER", align="center", font=FONT)
