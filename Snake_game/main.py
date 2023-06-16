from turtle import Turtle, Screen
import time
from snake import Snake

scr = Screen()
scr.setup(600,  600)
scr.bgcolor("black")
scr.title("Snake Game")
scr.tracer(0)

snake = Snake()
scr.listen()
scr.onkey(snake.up, "Up")
scr.onkey(snake.down, "Down")
scr.onkey(snake.right, "Right")
scr.onkey(snake.left, "Left")

game_on = True
while game_on:
    scr.update()
    time.sleep(0.05)
    snake.move()




scr.exitonclick()


