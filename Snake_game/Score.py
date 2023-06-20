from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Calibre", 16, "normal")


class Score(Turtle):

    #
    #
    def __init__(self):
        """Creating score board"""
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        """Showing the scores"""
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """game over banner, once Snake colloids walls or itself"""
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increasing the score board"""
        self.score += 1
        self.clear()
        self.update_score()