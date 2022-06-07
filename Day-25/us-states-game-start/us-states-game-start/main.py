import turtle

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# THe 50 states dataset
import pandas


states = pandas.read_csv("50_states.csv")

#print(states["state"])

states_list = states["state"].to_list()
answer_state = screen.textinput(title="Guess the State", prompt="What's the next States Name ").title()

if answer_state in states_list:
    print(answer_state)

screen.exitonclick()
