import time
from ball import Ball
from score import Score
from paddle import Paddle
from turtle import Screen

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Day 22")
screen.tracer(0)

paddleR = Paddle((350, 0))
paddleL = Paddle((-350,0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(paddleR.go_up, 'Up')
screen.onkey(paddleR.go_down, 'Down')
screen.onkey(paddleL.go_up, 'w')
screen.onkey(paddleL.go_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 290 or ball.ycor() < -280:
        ball.ybounce()
    
    if ball.distance(paddleR) < 50 and ball.xcor() < 330 or \
        ball.distance(paddleL) < 50 and ball.xcor() < -330:
        ball.xbounce()
    
    if ball.xcor() > 380:
        ball.reset_position()
        score.lpoint()
    
    if ball.xcor() < -380:
        ball.reset_position()
        score.rpoint()








screen.exitonclick()