class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions

    def next_question(self):
        # ans = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} "
        #             f"(True or False) ").lower()[0]
        # if ans == self.question_list[self.question_number].answer.lower()[0]:
        #     print("Correct!")
        #     self.score += 1
        # else:
        #     print("Wrong!")
        # self.question_number += 1
        # self.report()
        if self.has_questions_left():
            question = self.question_list[self.question_number]
            self.question_number += 1
            return question.text, question.answer
        else:
            raise IndexError("No more questions are left!")

    def has_questions_left(self):
        return self.question_number < len(self.question_list)

    def report(self):
        print(f"Your score is: {self.score}/{self.question_number}\n")
