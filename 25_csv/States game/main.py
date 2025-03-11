import turtle
import pandas as pd
import time
from writer import Writer, Timer, NUM_STATES


screen = turtle.Screen()
screen.setup(725, 491)
screen.title("US states game")
screen.bgpic("blank_states_img.gif")

writer = Writer()
timer = Timer()

timer_started = False
while writer.score < NUM_STATES:
    user_guess = turtle.textinput(f" {writer.score}/{NUM_STATES} Guess a state!", "US state:")
    if user_guess == 'q':
        break
    writer.state_checker(user_guess)

missed = pd.DataFrame(writer.missing)
missed.to_csv("states_to_learn.csv")
