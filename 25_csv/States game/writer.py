from turtle import Turtle
import pandas as pd
FONT = ('Arial', 8, 'normal')

STATES = pd.DataFrame(pd.read_csv("50_states.csv", delimiter=','))
NUM_STATES = len(STATES.state)


class Writer(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.states = STATES
        self.missing = self.states["state"].to_list()
        self.guesses = []
        self.score = len(self.guesses)

    def state_checker(self, name: str):
        name = name.title()
        if name not in list(self.states.state):
            print("That is not a US state!")
            return
        elif name in self.guesses:
            print(f"You already guessed {name}!")
            return
        else:
            self.guesses.append(name)
            self.missing.remove(name)
            self.score = len(self.guesses)
            x = self.states[self.states.state == name].x.item()
            y = self.states[self.states.state == name].y.item()
            self.goto(x, y)
            self.write(f"{name}", align='center', font=FONT)


class Timer(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 230)
        self.write("10:00")

    def update(self, time):
        pass