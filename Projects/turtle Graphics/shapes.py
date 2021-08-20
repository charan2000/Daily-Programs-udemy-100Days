import turtle as t
import random

color_lst = ["dark green", "chartreuse", "orange red", "navy", "orange", "dark turquoise", "dark slate gray", "dark slate blue"]
me = t.Turtle()


def draw_shape(num_sides):
    for i in range(num_sides):
        angle = 360/num_sides
        me.forward(100)
        me.right(angle)


until = int(input("No. of shapes from 3 ?"))

for i in range(3, until+1):
    me.color(random.choice(color_lst))
    draw_shape(i)