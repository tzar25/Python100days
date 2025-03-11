from turtle import Turtle
import random as r
MAP_SIZE = 800
GRID_SIZE = 20


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed(0)
        self.move()

    def move(self):
        max = int(MAP_SIZE / GRID_SIZE / 2 - 1)
        x, y = r.randint(-max, max), r.randint(-max, max)
        self.goto(20 * x, 20 * y)
