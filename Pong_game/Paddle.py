from turtle import Turtle


class Paddle(Turtle):


    def __init__(self,x,y):
        """Creating the paddles"""
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x,y)


    #Snake controls
    def go_up(self):
        # paddle.left(90)
        # paddle.forward(20)
        y = self.ycor() + 20
        self.goto(self.xcor(), y)

    def go_down(self):
        y = self.ycor() - 20
        self.goto(self.xcor(), y)