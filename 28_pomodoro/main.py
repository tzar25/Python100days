from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9BDEAC"
YELLOW = "#FEF0D5"
FONT_NAME = "Courier"
WORK_SEC = 25 * 60
SHORT_BREAK_SEC = 5 * 60
LONG_BREAK_SEC = 20 * 60
reps = 0
timer = None


def start():
    global reps
    if reps == 7:
        seconds = LONG_BREAK_SEC
        timer_label.config(text="Have a\nlong break!", fg=RED)
        checkmarks.config(text="")
    elif reps % 2 == 1:
        seconds = SHORT_BREAK_SEC
        timer_label.config(text="Take a\nshort break!", fg=PINK)
        checkmarks.config(text=checkmark * int((reps + 1) / 2))
    else:
        seconds = WORK_SEC
        timer_label.config(text="\nLet's work!", fg=GREEN)
    reps += 1
    reps %= 8
    count_down(seconds)


def reset():
    global timer, reps
    if timer:
        window.after_cancel(timer)
    timer_label.config(text="\nTimer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmarks.config(text="")
    timer = None
    reps = 0


def count_down(count):
    global timer
    display = f"{int(count/60):>02}:{count%60:>02}"
    canvas.itemconfig(timer_text, text=display)
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start()


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="\nTimer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "normal"))
timer_label.grid(row=0, column=1)

canvas = Canvas(width=248, height=248, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(124, 124, image=tomato_image)
timer_text = canvas.create_text(130, 150, text="00:00", fill="white", font=(FONT_NAME, 22, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", command=start, bg=YELLOW, fg=RED, font=(FONT_NAME, 12, "bold"), highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset, bg=YELLOW, fg=RED, font=(FONT_NAME, 12, "bold"), highlightthickness=0)
reset_button.grid(column=2, row=2)

checkmark = "✔"
checkmarks = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20))
checkmarks.grid(column=1, row=3)


window.mainloop()
