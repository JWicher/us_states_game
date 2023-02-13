import turtle
import pandas
from state import State

screen = turtle.Screen()
screen.title("US States Game")

image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

data = pandas.read_csv("./50_states.csv")
guessed = []
states = data.state.to_list()

while len(guessed) < len(states):
    screen.update()

    user_answer = screen.textinput(title=f"Guess the state [{len(guessed)}/{len(states)}]", prompt="What is your next "
                                                                                                   "answer?")
    title_type_user_answer = user_answer.title()

    if title_type_user_answer == 'Exit':
        not_guessed_filtered = filter(lambda state_name: state_name not in guessed, states)
        not_guessed_list = list(not_guessed_filtered)

        missing_states = pandas.DataFrame(not_guessed_list)
        missing_states.to_csv("missing_states.csv")
        break

    if title_type_user_answer in states and title_type_user_answer not in guessed:
        guessed.append(data[data.state == title_type_user_answer].state.item())
        state_info = data[data.state == title_type_user_answer]
        state_coordinates = (int(state_info.x), int(state_info.y))

        state = State(title_type_user_answer)
        state.put_label(state_coordinates)
