from turtle import Turtle


class Player():

    starting_point = (0, -280)
    move_distance = 10

    def __init__(self):
        """Creats a player"""
        self.tim = Turtle()
        self.tim.shape("turtle")
        self.tim.tilt(90)
        self.tim.penup()
        self.tim.goto(self.starting_point)


    def moveup(self):
        """Moves the player up words"""
        y  =self.tim.ycor() + self.move_distance
        self.tim.goto(0, y)

    def movedown(self):
        """moves the player down words"""
        y  =self.tim.ycor() - self.move_distance
        self.tim.goto(0, y)

    def reset_position(self):
        """sends the player to its starting position"""
        self.tim.goto(self.starting_point)



