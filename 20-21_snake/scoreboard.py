from turtle import Turtle
from food import MAP_SIZE
ALIGNMENT ="center"
FONT = ('Arial', 10, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, MAP_SIZE / 2 - 20)
        self.score = -1
        self.pendown()
        self.color("white")
        self.update()

    def update(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(F"GAME OVER! Your final score is {self.score}", align=ALIGNMENT, font=FONT)
