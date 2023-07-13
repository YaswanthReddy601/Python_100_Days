from turtle import Turtle, Screen
import time
from Ball import Ball
from Paddle import Paddle
from ScoreBoard import Score

#Creating object of screen to setup the screen color, size.
screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
#Stops the all turtles animation untill we update manually.
screen.tracer(0)

#Creating Paddles
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

#Creating the ball
ball = Ball()

#Creating Score ball
score = Score()
screen.listen()

#right paddle controls
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
#left paddle controls
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_on = True

while game_on:
    #Ball sleeps 0.1 second before moving and then updates the ball
    time.sleep(0.1)
    #Helps to stop animation
    screen.update()
    #To move the ball
    ball.move()

    #Changing the direction when ball colloids upper or lower wall
    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.change_direction_y()

    #Changing the direction when ball colloids paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.change_direction_x()

    #when ball passed side walls the ball will come to middle of the screen and score will be increased
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

    #if a players score 5 points game will over
    if score.l_score == 5 or score.r_score == 5:
        game_on = False
        score.game_over()



screen.exitonclick()


