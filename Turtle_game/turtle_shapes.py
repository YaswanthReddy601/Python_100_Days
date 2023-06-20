import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")

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