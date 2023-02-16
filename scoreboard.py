from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level=1
        self.goto(-280, 250)
        self.update_score_board()

    def increase_level(self):
        self.level += 1
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(f"level :{self.level}", align="left", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER your score is :{self.level}", align="center", font=FONT)
