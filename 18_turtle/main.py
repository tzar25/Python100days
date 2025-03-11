import turtle
import random as r
import colorgram

t = turtle.Turtle()
t.shape("turtle")
turtle.colormode(255)
t.color("green")
t.speed(0)

# """Drawing a square"""
# for _ in range(4):
#     t.fd(100)
#     t.right(90)

# """Same with dashed lines"""
# for _ in range(4):
#     for _ in range(5):
#         t.fd(10)
#         t.pu()
#         t.fd(10)
#         t.pd()
#     t.right(90)


def random_color():
    _r = r.randint(0, 255)
    _g = r.randint(0, 255)
    _b = r.randint(0, 255)
    return _r, _g, _b


# """Draw n-gons"""
# for i in range(8):
#     n = i + 3
#     t.pencolor(random_color())
#     for j in range(n):
#         t.fd(100)
#         t.right(360/n)


# """random walk"""
# def step(_turtle):
#     _turtle.pencolor(random_color())
#     _turtle.fd(30)
#     _turtle.setheading(90 * r.randint(0, 3))
#
#
# for _ in range(200):
#     t.pensize(15)
#     step(t)

# def draw_spirograph(num_circles, size=100):
#     turn_angle = 360 / num_circles
#     for _ in range(num_circles):
#         t.pencolor(random_color())
#         t.circle(size)
#         t.right(turn_angle)
#
#
# draw_spirograph(100, 200)


def draw_filled_circle(size=10):
    t.begin_fill()
    t.circle(size)
    t.end_fill()


def painting(palette, paint_size=10, dot_size=5, gap_size=5):
    t.penup()
    start = - int((paint_size - 1) * dot_size * gap_size / 2)
    t.setpos(start, start)
    for col in range(paint_size):
        t.pendown()
        for row in range(paint_size):
            color = r.choice(palette)
            t.pencolor(color)
            t.fillcolor(color)
            draw_filled_circle(dot_size)
            t.penup()
            t.fd(gap_size * dot_size)
            t.pendown()
        t.penup()
        t.setpos(start, t.ycor() + gap_size * dot_size)
    t.setpos(start, start)


def extract_colors(f_):
    painting_colors = []
    colors = colorgram.extract(f_, 20)
    for color in colors:
        _r = color.rgb[0]
        _g = color.rgb[1]
        _b = color.rgb[2]
        if _r < 240 or _g < 240 or _b < 240:
            painting_colors.append((_r, _g, _b))
    return painting_colors


t.hideturtle()
painting(extract_colors("dot_painting.jpg"), 10, 10, 5)

screen = turtle.Screen()
screen.exitonclick()
