import random
from turtle import Turtle
COLORS = ["red", "orange", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def spawn_car(self):
        new_car = Turtle()
        new_car.color(random.choice(COLORS))
        new_car.shape("square")
        new_car.penup()
        new_car.goto(320, 10 * random.randint(-26, 26))
        new_car.setheading(180)
        new_car.shapesize(stretch_len=2)
        self.cars.append(new_car)

    def move_cars(self):
        for i, car in enumerate(self.cars):
            car = self.cars[i]
            car.forward(self.move_speed)
            if car.xcor() < -320:
                self.cars.pop(i)

    def level_up(self):
        self.move_speed += MOVE_INCREMENT
        for car in self.cars:
            car.reset()
            car.hideturtle()
        self.cars = []

