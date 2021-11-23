from turtle import Screen
from player_movement import Playermovement
from cars import Cars
import time
from scoreboard import Scoreboard
import random

level = 6
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Cross the Road")
screen.tracer(0)
playermovement = Playermovement()
cars = Cars()
screen.listen()
screen.onkey(playermovement.move, "Up")
scoreboard = Scoreboard()

game_on = True
while game_on:
    time.sleep(0.1)
    cars.create_cars(level)
    cars.car_moves()
    screen.update()
    for i in cars.all_cars:
        if i.distance(playermovement) < 22:
            game_on = False
    # Detect successful Crossing
    if playermovement.is_at_finish():
        cars.level_up()
        scoreboard.update_score()
        playermovement.go_to_start()




screen.exitonclick()



