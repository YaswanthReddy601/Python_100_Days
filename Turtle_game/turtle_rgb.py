import turtle as t
import random

bob = t.Turtle()
directions = [0,45,90,18,270]
bob.pensize(10)
bob.speed(0)
t.colormode(255)

def color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colorrr = (r, g, b)
    return colorrr

#bob.speed(10)
for x in range(100):
    bob.color((color()))
    bob.forward(50)
    bob.setheading(random.choice(directions))