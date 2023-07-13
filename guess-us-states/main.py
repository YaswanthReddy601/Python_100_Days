import turtle as t

import pandas

screen = t.Screen()
screen.title("US Map")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)

# def get_mouse_click_coordinates(x,y):
#     print(x,y)
#
# t.onscreenclick(get_mouse_click_coordinates)
# t.mainloop()
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

score = 0
guessed_states = []
missed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 states are guessed.", prompt="Guess a state in US ").title()

    if answer == "Exit":
        [missed_states.append(state) for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missed_states.append(state)
        missed_states_data = pandas.DataFrame(missed_states)
        missed_states_data.to_csv("missed_states.csv")
        y = t.Turtle()
        y.hideturtle()
        y.write(f" You named {score} states in us map!!!", align="center",
                font=("calibre", 14, "normal"))
        break
    elif answer in all_states:
        guessed_states.append(answer)
        x = t.Turtle()
        x.penup()
        x.hideturtle()
        state_data = data[data.state == answer]
        x.goto(float(state_data.x), float(state_data.y))
        x.write(answer)
        # x.write(f"{answer}", align="center", font=("calibre", 8, "normal"))
        score += 1

screen.exitonclick()
