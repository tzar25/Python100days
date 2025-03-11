import time
from turtle import Screen
from snake import Snake
from food import Food, MAP_SIZE, GRID_SIZE
from scoreboard import Scoreboard


is_game_on = True
play_more = True
screen = Screen()
screen.setup(width=MAP_SIZE, height=MAP_SIZE)
screen.bgcolor("black")
screen.title("Snake game")
snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(key="w", fun=snake.turn_north)
screen.onkey(key="a", fun=snake.turn_west)
screen.onkey(key="s", fun=snake.turn_south)
screen.onkey(key="d", fun=snake.turn_east)

screen.tracer(0)
screen.update()

while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect food collision
    if snake.head.distance(food) < 15:
        food.move()
        scoreboard.increase_score()
        snake.grow()

    # Detect wall collision
    if max(abs(snake.head.xcor()), abs(snake.head.ycor())) > int((MAP_SIZE - GRID_SIZE) / 2):
        scoreboard.reset()
        snake.reset()

    # Detect tail collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
