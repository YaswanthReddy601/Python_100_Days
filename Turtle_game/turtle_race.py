import random
from turtle import Turtle, Screen

game_on = False
scr = Screen()
scr.setup(800, 400)
users_turtle = scr.textinput(title= "Choose", prompt="Choose your turtle ")
colors = ["red","purple", "green", "blue", "orange", "brown","pink"]
angles = [0, 50, -50, 100, -100, -150, 150 ]
all_turtles = []
for x in range(0,7):
    tim = Turtle("turtle")
    tim.color(colors[x])
    tim.penup()
    tim.goto(x=-380,y=angles[x])
#    tim.speed(10)
    all_turtles.append(tim)

if users_turtle:
    game_on = True

while game_on:

    for turtle in all_turtles:
        if turtle.xcor() > 380:
            game_on = False
            winner = turtle.pencolor()
            if winner == users_turtle:
                print(f"Your {winner} turtle won the game")
                break
            else:
                print(f"Your turtle lost the game")
                break
        distance = random.randint(0,10)
        turtle.forward(distance)


scr.exitonclick()
