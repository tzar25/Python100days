import random
import turtle

is_race_on = False
screen = turtle.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle are you betting on?")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = dict()

y = - 75
for color in colors:
    turtles[color] = turtle.Turtle(shape="turtle")
    turtles[color].color(color)
    turtles[color].penup()
    turtles[color].goto(-230, y)
    y += 30

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles.keys():
        turtles[turtle].fd(random.randint(0, 10))
        if turtles[turtle].xcor() > 230:
            if user_bet == turtle:
                won = "won"
            else:
                won = "lost"
            print(f"The {turtles[turtle].pencolor()} turtle won! You have {won}!")
            is_race_on = False



screen.exitonclick()
