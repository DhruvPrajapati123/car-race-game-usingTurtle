from turtle import Turtle
MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.STARTING_POSITION = (0, -280)
        self.FINISH_LINE_Y = 280
        self.shape("turtle")
        self.penup()
        self.goto(self.STARTING_POSITION)
        self.setheading(self.heading() + 90)

    def up(self):
        self.forward(MOVE_DISTANCE)
