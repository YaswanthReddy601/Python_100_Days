from turtle import Turtle


STARTING = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 10
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.tails = []
        self.create_snake()
        self.head = self.tails[0]

    def create_snake(self):
        """Creating the snake"""
        for x in STARTING:
            self.add_tail(x)

    def add_tail(self,position):
        """Adding a tail"""
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        snake.speed(10)
        self.tails.append(snake)


    def extend(self):
        """extending the snakes boy"""
        self.add_tail(self.tails[-1].position())

    #snake's bosy controls
    def move(self):
       for tail_num in range(len(self.tails) - 1, 0, -1):
           new_x = self.tails[tail_num - 1].xcor()
           new_y = self.tails[tail_num - 1].ycor()
           self.tails[tail_num].goto(new_x, new_y)

       self.tails[0].forward(DISTANCE)

    #Snake's head contrils
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)




