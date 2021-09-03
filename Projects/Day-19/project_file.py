import random
from turtle import Turtle, Screen

game_on = False
screen = Screen()
screen.setup(width=500, height=500)
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which color turtle wins the race ?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_axis = -100
all_turtles = []
for i in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(i)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_axis)
    all_turtles.append(new_turtle)
    y_axis = y_axis + 30

if user_bet:
    game_on = True

while game_on:
    for j in all_turtles:
        if j.xcor() > 230:
            game_on = False
            color_won = j.pencolor()
            if color_won == user_bet:
                print(f"You've won ! {color_won} turtle won the race !")
            else:
                print(f"You've lost ! {color_won} turtle won the race !")
        random_dist = random.randint(0, 10)
        j.forward(random_dist)

screen.exitonclick()
