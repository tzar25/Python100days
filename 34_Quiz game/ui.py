from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = "Arial", 20, "italic"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.question = ""
        self.answer = ""
        self.score = 0

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(height=500, width=300, padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(height=250, width=300, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="Question", font=FONT, fill="black", width=290)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="imgs/true.png")
        false_image = PhotoImage(file="imgs/false.png")
        self.false_button = Button(image=false_image, command=self.false_function, highlightthickness=0)
        self.true_button = Button(image=true_image, command=self.true_function, highlightthickness=0)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.score_text = Label(text=f"Score: {self.score}", font=("Arial", 10), bg=THEME_COLOR, fg="white")
        self.score_text.grid(row=0, column=1)

        self.get_next_question()

        self.window.mainloop()

    def true_function(self):
        if self.answer:
            self.score += 1
            self.score_text.config(text=f"Score: {self.score}")
        self.give_feedback(self.answer is True)

    def false_function(self):
        if not self.answer:
            self.score += 1
            self.score_text.config(text=f"Score: {self.score}")
        self.give_feedback(self.answer is False)

    def get_next_question(self):
        self.canvas.config(bg="white")
        try:
            self.question, self.answer = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=self.question)
        except IndexError:
            self.canvas.itemconfig(self.question_text, text=f"Congratulations, you finished with {self.score}/{len(self.quiz_brain.question_list)}")
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")

    def give_feedback(self, correct: bool):
        if correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(500, self.get_next_question)

