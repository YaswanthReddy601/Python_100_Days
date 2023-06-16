import turtle as t
import random

bob = t.Turtle()
colors = ["red","blue","green","pink","black","orange","CornflowerBlue", "IndianRed"]
directions = [0,45,90,18,270]
bob.pensize(10)
#bob.speed(10)
for x in range(50):
    bob.color(random.choice(colors))
    bob.forward(50)
    bob.setheading(random.choice(directions))