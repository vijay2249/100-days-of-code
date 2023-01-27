from turtle import Turtle

class Ball(Turtle):
    def __init__(self, ):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    
    def move(self):
        x, y = self.xcor()+self.x_move, self.ycor()+self.y_move
        self.goto(x, y)
    
    def ybounce(self):
        self.y_move *= -1
    
    def xbounce(self):
        self.x_move *= -1
        self.ball_speed *= 0.7
    
    def reset_position(self):
        self.goto(0,0)
        self.ball_speed = 0.1
        self.xbounce()