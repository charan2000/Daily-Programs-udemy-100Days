from turtle import Turtle
STARTING_POSITION = (0,-280)
MOVE_DISTANCE = 10
FINISH_LINE = 290

class Playermovement(Turtle):

    def __init__(self):
        super(Playermovement, self).__init__()
        self.color("Blue")
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def is_at_finish(self):
        if self.ycor() >= FINISH_LINE:
            return True
        else:return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def move(self):
        if self.ycor() < 290:
            self.forward(MOVE_DISTANCE)
