import time
from paddle import Paddle, WIDTH, HEIGHT
from turtle import Screen
from ball import Ball
from random import randint
from scoreboard import Scoreboard
RANDOM_THRESHOLD = 45

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

scoreboard = Scoreboard()
Scoreboard().draw_line()
player = Paddle('l')
opponent = Paddle('r')

ball = Ball()

screen.update()

screen.listen()
screen.onkeypress(key='w', fun=player.up)
screen.onkeypress(key='s', fun=player.down)

game_on = True

while game_on:
    scoreboard.update_score()
    screen.update()
    time.sleep(0.05)
    ball.move()

    if abs(ball.xcor()) >= opponent.segments[0].xcor():
        if ball.xcor() > 0:
            scoreboard.player_score += 1
        else:
            scoreboard.opponent_score += 1
        scoreboard.update_score()
        time.sleep(1)
        ball.reset()

    for seg in player.segments + opponent.segments:
        if seg.distance(ball) < 25:
            ball.vector[0] *= -1

    should_opponent_move = randint(0, 100)
    if opponent.bot.ycor() < ball.ycor() and ball.vector[1] > 0 and should_opponent_move < RANDOM_THRESHOLD:
        opponent.up()
    elif opponent.top.ycor() > ball.ycor() and ball.vector[1] < 0 and should_opponent_move < RANDOM_THRESHOLD:
        opponent.down()


screen.exitonclick()
