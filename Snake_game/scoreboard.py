from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoreboad(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.ht()
        self.color("white")
        self.goto(x=0, y=270)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def score_up(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
