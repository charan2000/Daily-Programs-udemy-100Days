from turtle import Turtle
import random

COLORS = ["red", "green", "blue", "yellow", "orange", "grey"]
MOVEMENT = 10
STARTING_DISTANCE = 10
MOVEMENT_INCREMENT = 10


class Cars():

    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVEMENT_INCREMENT

    def create_cars(self, level):
        random_choice = random.randint(1, level)
        if random_choice == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-230, 230)
            new_car.goto(300, random_y)
            # self.setheading(180)
            self.all_cars.append(new_car)

    def car_moves(self):
        for c in self.all_cars:
            c.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVEMENT_INCREMENT
