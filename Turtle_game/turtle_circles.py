import turtle
from turtle import Turtle, Screen
import random


tom = Turtle()
turtle.colormode(255)
tom.speed(0)

def color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, b, g

for x in range(0,int(360/2)):
    tom.color(color())
    tom.left(2)
    tom.circle(100)



scr = Screen()
scr.exitonclick()
