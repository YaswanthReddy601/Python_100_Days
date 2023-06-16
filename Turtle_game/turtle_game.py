import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")
#Square
#timmy.forward(100)
#timmy.right(90)
#timmy.forward(100)
#timmy.right(90)
#timmy.forward(100)
#timmy.right(90)
#timmy.forward(100)

#a line
#for x in range(14):
#    turtle.forward(10)
#    turtle.penup()
#    turtle.forward(10)
#    turtle.pendown()

#shapes
colors = ["red","blue","green","pink","black","orange","CornflowerBlue", "IndianRed"]


def shapes(num_sides):
    for x in range(num_sides):
        angle = 360/num_sides
        turtle.forward(100)
        turtle.right(angle)

for sides in range(3,15):
    timmy.color(random.choice(colors))
    shapes(sides)




screen = Screen()
screen.exitonclick()