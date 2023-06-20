import random
from turtle import Turtle



class Car():

    colors = ["red", "blue", "yellow", "pink", "brown", "violet", "green"]
    starting_move = 5
    move_increment = 5

    def __init__(self):
        super().__init__()
        self.allcars = []

    def create_car(self):
        """Creats the cars"""
        #to reduce the number of cars
        #cars are created when x = 1
        x = random.randint(1, 6)
        if x ==1 or x == 5:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(self.colors))
            y = random.randint(-250, 250)
            new_car.penup()
            new_car.goto(300, y)
            self.allcars.append(new_car)

    def car_moment(self):
        """moves all the cars"""
        for car in self.allcars:
            car.backward(self.starting_move)

    def speed_increase(self):
        """increases the speed"""
        global starting_move
        self.starting_move += self.move_increment
