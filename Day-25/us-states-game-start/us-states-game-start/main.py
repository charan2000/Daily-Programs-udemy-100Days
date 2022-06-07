import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# THe 50 states dataset


states = pandas.read_csv("50_states.csv")

# print(states["state"])

states_list = states["state"].to_list()
print(len(states_list))
correct_count = 0
guessed_states = []

while len(guessed_states) < 50:

    answer_state = str(screen.textinput(title="Guess the State Name", prompt=f"{len(guessed_states)} of 50 States guessed")).title()

    if answer_state == "Exit":
        missing_states = [st for st in states_list if st not in guessed_states]
        for st in states_list:
            if st not in guessed_states:
                missing_states.append(st)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in states_list:
        guessed_states.append(answer_state)
        #print(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        stat_cord = states[states.state == answer_state]
        t.goto(int(stat_cord.x), int(stat_cord.y))
        t.write(answer_state)



