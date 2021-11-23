from turtle import Turtle
FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("White")
        self.hideturtle()
        self.penup()
        self.goto(-20, 280)
        self.update_score()

    def update_score(self):
        self.goto(-280,280)
        self.write(f"Score : {self.score}", False, align="left", font=FONT)

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.goto(270, 280)
            self.write(f"High Score : {self.high_score}", False, align="right", font=FONT)
        else: pass

    def writeScore(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",False,align="center",font=FONT)