from turtle import Turtle

class Scoreboard(Turtle):

    alignment = "left"
    font = ["Calibri", 16, "normal"]
    High_Score = 0
    def __init__(self):
        """
        Creats Score Board
        """
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-290, 270)
        self.level = 1
        self.score()

    def score(self):
        """gets the score and high score"""
        with open("High_Score.txt") as HS:
            self.High_Score = int(HS.read())
        self.update_score()

    def increament(self):
        """increases the score"""
        self.level += 1
        self.clear()
        self.update_score()

    def update_score(self):
        """shows and updates the score"""
        self.clear()
        self.write(f"Level-{self.level}  High Score-{self.High_Score}", align=self.alignment, font=self.font)


    def game_over_Banner(self):
        """shows the game over and score """
        score = Turtle()
        if self.level > self.High_Score:
            with open("High_Score.txt", mode= "w") as HS:
                HS.write(f"{self.level-1}")
            with open("High_Score.txt") as HS:
                self.High_Score = int(HS.read())
        score.write(f"Game Over\nYour score is {self.level-1} and High Score-{self.High_Score}", align="center", font= self.font)





