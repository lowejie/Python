import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_my_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pd.read_csv("MY_states.csv")
all_states = df.state.to_list()
guessed_states = []

while len(guessed_states) < len(all_states):
    answer_state = screen.textinput(title=f"{len(guessed_states)}/16 States/FD Correct", prompt="What is another state/fd?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = df[df.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)