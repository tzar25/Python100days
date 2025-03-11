import pandas as pd
from tkinter import *
from random import choice
GREEN = "#B1DDC6"
FONT_LANG = ("Arial", 40, "italic")
FONT_WORD = ("Arial", 60, "bold")
english_word, french_word = "", ""


# =============================  Data handling  ============================ #
def load_file():
    data_file = None
    try:
        data_file = open("data/words_to_learn.csv", "r")
    except FileNotFoundError:
        data_file = open("data/french_words.csv", "r")
    finally:
        loaded_data = pd.read_csv("data/french_words.csv", delimiter=",")
        data_file.close()
        return loaded_data


def pick_word():
    global english_word, french_word
    french_word, english_word = choice(list(words_to_learn.items()))
    canvas.itemconfig(card, image=card_front_img)
    canvas.itemconfig(text_word, text=french_word, fill="black")
    canvas.itemconfig(text_lang, text="French", fill="black")


def update_card():
    global english_word
    canvas.itemconfig(card, image=card_back_img)
    canvas.itemconfig(text_word, text=english_word, fill="white")
    canvas.itemconfig(text_lang, text="English", fill="white")

    window.after(1000, pick_word)


def answer_right():
    words_to_learn.pop(french_word)
    if len(words_to_learn):
        df = pd.DataFrame(words_to_learn.items(), columns=["French", "English"])
        df.to_csv("data/words_to_learn.csv", index=False)
        update_card()
    else:
        exit(0)


data = load_file()
words_to_learn = dict(zip(data.French, data.English))
# data_dict = data.to_dict(orient="records")

# ==================================  UI  ================================== #

window = Tk()
window.config(width=800, height=800, padx=50, pady=50, bg=GREEN)
window.title("French flashcards")

canvas = Canvas(width=800, height=526, bg=GREEN, highlightthickness=0)
card_front_img = PhotoImage(file="img/card_front.png")
card_back_img = PhotoImage(file="img/card_back.png")
card = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)

# timer_text = canvas.create_text(130, 150, text="00:00", fill="white", font=(FONT_NAME, 22, "bold"))
text_lang = canvas.create_text(400, 150, font=FONT_LANG)
text_word = canvas.create_text(400, 263, font=FONT_WORD)

right_img = PhotoImage(file="img/right.png")
button_right = Button(image=right_img, command=answer_right, highlightthickness=0)
button_right.grid(row=1, column=1)

wrong_img = PhotoImage(file="img/wrong.png")
button_wrong = Button(image=wrong_img, command=update_card, highlightthickness=0)
button_wrong.grid(row=1, column=0)


pick_word()
window.mainloop()
