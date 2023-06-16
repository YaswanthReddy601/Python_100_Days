import turtle
from turtle import Turtle, Screen
import random
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("image.jpg",30)
# for x in colors:
#     r = x.rgb.r
#     g = x.rgb.g
#     b = x.rgb.b
#     color = (r,g,b)
#     rgb_colors.append(color)
# print(rgb_colors)

tom = Turtle()
turtle.colormode(255)
colors = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tom.penup()
tom.hideturtle()
tom.setheading(225)
tom.forward(300)
tom.setheading(0)
tom.speed(0)
for x in range(1, 101):
    tom.dot(20, random.choice(colors))
    tom .penup()
    tom.forward(50)

    if x%10 == 0:
        tom.setheading(90)
        tom.forward(50)
        tom.setheading(180)
        tom.forward(500)
        tom.setheading(0)




scr = Screen()
scr.exitonclick()