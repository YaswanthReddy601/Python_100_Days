from turtle import Turtle, Screen
import time

from Food import Food
from snake import Snake
from Score import Score

#Settingup the screen
scr = Screen()
scr.setup(600,  600)
scr.bgcolor("black")
scr.title("Snake Game")
#pauses showing the animation
scr.tracer(0)

#Creating snake
snake = Snake()
#Creating food
food = Food()
#Creating Score board
score = Score()

#Snake controls
scr.listen()
scr.onkey(snake.up, "Up")
scr.onkey(snake.down, "Down")
scr.onkey(snake.right, "Right")
scr.onkey(snake.left, "Left")

game_on = True
while game_on:
    #resumes showing the animation
    scr.update()
    #Ball sleeps 0.04 second before snake moving.
    time.sleep(0.04)
    #To move the snake
    snake.move()

    #Eating the food, increasing the score boars, and extending the snake's tail
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    #Checking that snakes head hits (any of its tail) anywhere of its body
    for tail in snake.tails[1:]:
        if snake.head.distance(tail) < 5:
            game_on = False
            score.game_over()

    #Checking snake head hits any of the 4 walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -280:
        game_on = False
        score.game_over()

#Bind method to mouse clicks on the Screen
scr.exitonclick()


