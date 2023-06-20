from turtle import Turtle

ALIGNMENT = "center"
FONT = ("calinre", 16, "normal")


class Score(Turtle):

    def __init__(self):

        #Creating score board
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.update_score()
        self.hideturtle()

    def update_score(self):
        """Showing the scores"""
        self.goto(100, 260)
        self.write(f"Score : {self.r_score}", align=ALIGNMENT, font=FONT)
        self.goto(-100, 260)
        self.write(f"Score : {self.l_score}", align=ALIGNMENT, font=FONT)

    def l_point(self):
        """Increases left padle points"""
        self.l_score += 1
        self.clear()
        self.update_score()

    def r_point(self):
        """Increases right padle points"""
        self.r_score += 1
        self.clear()
        self.update_score()

    #game over banner, once a player win
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align= ALIGNMENT, font= FONT)

