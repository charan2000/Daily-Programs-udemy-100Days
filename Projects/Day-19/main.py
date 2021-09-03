from turtle import Turtle, Screen

me = Turtle()
screen = Screen()

def move_forward():
    me.forward(15)

def move_backwards():
    me.backward(15)

def turn_left():
    new_heading = me.heading() + 10
    me.setheading(new_heading)

def clear():
    me.clear()
    me.penup()
    me.home()
    me.pendown()

def turn_right():
    new_heading = me.heading() - 10
    me.setheading(new_heading)

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()