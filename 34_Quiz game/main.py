import requests
import pandas as pd
import html

from ui import QuizInterface
from quiz_brain import QuizBrain
from question_model import Question


def get_questions(amount=10, diff=0, category=0):
    parameters = {
        "amount": amount,
        "difficulty": diff,
        "category": category,  # 16 is Board games, 19 is math
        "type": "boolean"
    }
    if diff == 0:
        parameters.pop("difficulty")
    elif diff == 1:
        parameters[diff] = 'easy'
    elif diff == 2:
        parameters[diff] = 'medium'
    else:
        parameters[diff] = 'hard'
    if category == 0:
        parameters.pop("category")
    db_url = "https://opentdb.com/api.php"
    response = requests.get(url=db_url, params=parameters)
    response.raise_for_status()
    df = pd.DataFrame(response.json()['results'])
    with open("data.csv", 'w') as data_file:
        df.to_csv(data_file, index=False)


get_questions(category=19)
data = pd.read_csv("data.csv")
questions_list = [Question(html.unescape(question), answer) for question, answer in zip(data.question, data.correct_answer)]

# print(*questions_list, sep=";\n")

quiz_brain = QuizBrain(questions_list)
ui = QuizInterface(quiz_brain)


