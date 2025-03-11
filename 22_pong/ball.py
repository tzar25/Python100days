from turtle import Turtle
from paddle import WIDTH, HEIGHT
from random import randint


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(0)
        self.vector = [0, 0]
        self.reset()

    def move(self):
        if abs(self.ycor()) > HEIGHT / 2 - 30:
            self.vector[1] *= -1
        self.goto(self.xcor() + self.vector[0], self.ycor() + self.vector[1])

    def reset(self):
        y = randint(int(-HEIGHT / 40) + 2, int(HEIGHT / 40) - 2)
        self.goto(0, y * 20)
        self.vector = [randint(0, 1) * 20 - 10, randint(0, 1) * 20 - 10]



