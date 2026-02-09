from dotenv import load_dotenv
import requests
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from quiz_interface import QuizInterface
import os

load_dotenv()
base_url = os.getenv("BASE_URL", "base_url")


question_bank = []

# Hämtar data
def get_data(url, param=None):
    response = requests.get(url, params=param)
    response.raise_for_status()
    data = response.json()

    return data


# Hämtar frågor och sparar dem i data.py
def set_questions():
    # Antal frågor och typ av svarsmodell
    params = {
        "amount":10,
        "type":"boolean"
    }
    data = get_data(base_url, params)
    print(data["results"])
    with open("data.py", mode="w") as file:
        file.write(f"question_data = {repr(data['results'])}")


set_questions()


# Skapar Question-objekt från hämtad data
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Skapar quiz
quiz = QuizBrain(question_bank)

# Skapar gränssnitt
quiz_interface = QuizInterface(quiz)


