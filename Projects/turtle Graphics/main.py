#import colorgram
 #   rgb_colors = []
  #  colors = colorgram.extract("image.jpeg", 20)
   # for color in colors:
    #    r = color.rgb.r
     #   g = color.rgb.g
      #  b = color.rgb.b
       # new_color = (r,g,b)S2W
        #rgb_colors.append(new_color)
import random
import turtle as turtle_module

turtle_module.colormode(255)
me = turtle_module.Turtle()
colors_list = [(193, 73, 185), (115, 148, 208), (90, 89, 235), (87, 247, 192), (169, 76, 45), (152, 67, 132), (61, 106, 163), (215, 136, 189), (206, 150, 89), (40, 29, 167), (95, 205, 122), (114, 236, 248), (50, 177, 116), (181, 144, 251), (45, 131, 100), (144, 14, 110)]

me.setheading(220)
me.forward(300)
me.setheading(0)
dots = 100
for count in range(1, dots+1):
    me.dot(20, random.choice(colors_list))
    me.forward(50)

    if count % 10 == 0:
        me.setheading(90)
        me.forward(50)
        me.setheading(180)
        me.forward(500)
        me.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()