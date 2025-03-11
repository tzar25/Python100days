from turtle import Turtle
from food import MAP_SIZE
ALIGNMENT = "center"
FONT = ('Arial', 10, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, MAP_SIZE / 2 - 20)
        self.score = 0
        with open("data.txt", 'r') as file:
            self.high_score = int(file.read().strip())
        self.pendown()
        self.color("white")
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}   High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", 'w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update()

    def increase_score(self):
        self.score += 1
        self.update()
