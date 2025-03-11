from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def move_forwards():
    t.fd(10)


def move_back():
    t.back(10)


def turn_left():
    t.left(10)


def turn_right():
    t.right(10)


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)


screen.exitonclick()
