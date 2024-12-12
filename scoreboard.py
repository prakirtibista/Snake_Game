from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(-30,210)
        self.color("white")

    def increase_score(self):
        self.score +=1
        self.clear()
        self.write(f"Your score {self.score}", move=False, align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", move=False, align="center", font=("Arial", 24, "normal"))


