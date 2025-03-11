from turtle import Turtle

UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0


class Snake:

    def __init__(self):
        self.segments = []
        for i in range(3):
            self.add_segment((-20 * i, 0))
        self.head = self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.fd(20)

    def add_segment(self, position):
        new_turtle = Turtle()
        new_turtle.shape("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    def grow(self):
        self.add_segment(self.segments[-1].position())

    def turn_north(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)

    def turn_south(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def turn_west(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_east(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
