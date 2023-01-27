import time
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
player = Player()
score = Scoreboard()
cars = CarManager()

screen.bgcolor('white')
screen.setup(width=600, height=600)
screen.title("Day 23")
screen.tracer(0)

screen.listen()
screen.onkey(player.move_up, 'Up')


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move()

    for car in cars.all_Cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()
    
    if player.new_level():
        player.restart()
        cars.level_up()
        score.update_score()


screen.exitonclick()