from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.color("Black")
        self.penup()
        self.hideturtle()
        self.level_score = 0
        self.location()
        self.update_score()



    def location(self):
        self.goto(-390, 260)
        self.write("Level: ", align="Left", font=("Courier", 20, "normal"))

    def update_score(self):
        self.clear()
        self.location()
        self.level_score += 1
        self.goto(-290, 260)
        self.write(self.level_score, align="left", font=("Courier", 20, "normal"))



