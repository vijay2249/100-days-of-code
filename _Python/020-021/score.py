from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Nunito', 24, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.high_score = 0
        self.get_high_score()
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.write_score()
    
    def get_high_score(self):
        try:
            with open("score.txt", 'r') as f:
                self.high_score = int(f.read())
        except:
            with open('score.txt', 'w') as s:
                s.write(0)

    
    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_score()
        self.score = 0
    
    def update_high_score(self):
        with open('score.txt', 'w') as s:
            s.write(self.high_score)