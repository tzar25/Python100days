import random as r
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_handler = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="space", fun=player.step)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if r.randint(1, 100) < 20:
        car_handler.spawn_car()
    car_handler.move_cars()

    # collision detection
    for car in car_handler.cars:
        if car.xcor() - 30 <= player.xcor() <= car.xcor() + 30 and car.ycor() - 20 <= player.ycor() < car.ycor() + 20:
            game_is_on = False
            scoreboard.game_over()

    # level up
    if player.ycor() > 290:
        player.level_up()
        car_handler.level_up()
        scoreboard.update()

screen.exitonclick()
