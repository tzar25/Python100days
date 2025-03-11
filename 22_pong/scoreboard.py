from turtle import Turtle
from paddle import HEIGHT, WIDTH


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.speed(0)
        self.penup()
        self.goto(0, HEIGHT / 2 - 100)
        self.player_score, self.opponent_score = 0, 0

    def draw_line(self):
        self.goto(0, -HEIGHT / 2)
        self.setheading(90)
        while self.ycor() < HEIGHT / 2:
            self.width(3)
            self.fd(10)
            self.pendown()
            self.fd(10)
            self.penup()

    def update_score(self):
        self.clear()
        self.write(f"{self.player_score:>02}  {self.opponent_score:>02}", align="center", font=('Courier', 50, 'normal'))
