from turtle import Turtle
WIDTH = 1200
HEIGHT = 900


class Paddle:
    def __init__(self, side: str):
        self.segments = []
        for i in range(5):
            new_segment = Turtle()
            new_segment.penup()
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.speed(0)
            if side[0].lower() == 'l':
                x = -WIDTH / 2 + 20
            else:
                x = WIDTH / 2 - 20
            new_segment.goto(x, -40 + 20 * i)
            self.segments.append(new_segment)
        self.top = self.segments[-1]
        self.bot = self.segments[0]

    def move(self, direction):
        for seg in self.segments:
            if direction == 'u':
                seg.setheading(90)
            else:
                seg.setheading(270)
            seg.fd(20)

    def up(self):
        if self.top.ycor() < HEIGHT / 2 - 10:
            self.move('u')

    def down(self):
        if self.bot.ycor() > -HEIGHT / 2 + 10:
            self.move('d')

