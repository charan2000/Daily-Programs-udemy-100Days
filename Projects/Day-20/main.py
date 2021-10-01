from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=550)
screen.bgcolor("black")
screen.title("My Freaking Ist Game")
screen.tracer(0)

starting_positions = [(0,0), (-20,0), (-40,0)]

segments = []

for pos in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(pos)
    segments.goto(pos)

