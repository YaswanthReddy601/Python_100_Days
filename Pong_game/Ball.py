from turtle import Turtle

class Ball(Turtle):

    #Creating ball
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        """ball moving 10 pixles per second"""
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    #self.y_move => 10 * -1 = -10
    def change_direction_y(self):
        """Y-coordinate changes the direstion"""
        self.y_move *= -1

    #self.x_move => 10 * -1 = -10
    def change_direction_x(self):
        """X-coordinate changes the direstion"""
        self.x_move *= -1

    def reset_position(self):
        """Ball coming back to middle (0,0) axis."""
        self.goto(0, 0)
        self.change_direction_x()