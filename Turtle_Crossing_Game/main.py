from turtle import Turtle, Screen
import time

from Cars import Car
from Player import Player
from ScoreBoard import Scoreboard

#Settingup the screen
screen = Screen()
screen.setup(600, 600)
#Stopping the animation
screen.tracer(0)

#Creating the score board
score = Scoreboard()
#Creating car class object
car = Car()
#Creating a blayer
player = Player()

#Controls of turtle
screen.listen() #detect when the user has hit certain keys on the keyboard or moved/clicked the mouse.
screen.onkey(player.moveup, "Up")
screen.onkey(player.movedown, "Down")

game_on = True
#Starting the game
while game_on:
    #reducing the speed
    time.sleep(0.1)
    # turn turtle animation on or off
    screen.update()
    #Creating cars
    car.create_car()
    #Moving all cars
    car.car_moment()

    #Checking if player reached the finishing line or not
    if player.tim.ycor() > 280:
        score.increament()
        player.reset_position()
        car.speed_increase()

    #Checking if each car, that they colloid with the player or not
    for each_car in car.allcars:
        if each_car.distance(player.tim) < 20:
            game_on = False
            score.game_over_Banner()

#Helps to show the screen after completing the game
screen.exitonclick()