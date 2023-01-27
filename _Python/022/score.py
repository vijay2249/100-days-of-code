from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.r_score = 0
        self.l_score = 0
        self.write_score()
    
    def write_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=('Nunito', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=('Nunito', 80, 'normal'))
    
    def rpoint(self):
        self.r_score += 1
        self.write_score()
    
    def lpoint(self):
        self.l_score += 1
        self.write_score()
