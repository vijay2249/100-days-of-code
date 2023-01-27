import time
from food import Food
from score import Score
from snake import Snake
from turtle import Screen

screen = Screen()

screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Day 20 challenge")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect collision
    if snake.head.distance(food) < 15:
        score.increase()
        snake.extend()
        food.refresh()
    
    # collision with wall
    (x, y) = (snake.head.xcor(), snake.head.ycor())
    if x > 290 or x < -290 or y > 290 or y < -290:
        # game_is_on = False
        # score.game_over()
        score.reset()
        snake.reset()
    
    # self collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            # score.game_over()
            score.reset()
            snake.reset()


screen.exitonclick()