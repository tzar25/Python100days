from turtle import  Turtle
FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280, 280)
        self.color("black")
        self.level = 0
        self.update()

    def update(self):
        self.clear()
        self.level += 1
        self.write(f"Current level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
