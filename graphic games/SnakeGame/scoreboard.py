from turtle import Turtle
FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("White")
        self.hideturtle()
        self.penup()
        self.goto(-20, 280)
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-280,280)
        self.write(f"Score : {self.score} High Score : {self.high_score}", False, align="left", font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()


    def writeScore(self):
        self.score += 1
        self.clear()
        self.update_score()

    #def game_over(self):
     #   self.goto(0,0)
      #  self.write("Game Over",False,align="center",font=FONT)