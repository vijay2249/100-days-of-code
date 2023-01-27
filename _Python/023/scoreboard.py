from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(-280, 250)
        self.write_score()
    
    def write_score(self):
        self.clear()
        self.write(f"Level: {self.score}", align='left', font=FONT)
    
    def update_score(self):
        self.score += 1
        self.write_score()
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align='center', font=FONT)
