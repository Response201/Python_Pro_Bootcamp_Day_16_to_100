import random

from quiz_brain import QuizBrain
from data import question_data
from question_model import  Question



# Build the list of Question objects
question_bank =[]
for question_item in question_data:
    question_text = question_item["text"]
    question_answer= question_item["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Create quiz
current_question = QuizBrain(0,question_bank)

# Run the quiz until all questions are answered
while current_question.still_has_question_left():
    current_question.next_question()

# Display final result when the quiz ends
else:
    print(f"\nYou've completed the quiz\nYour final score was: {current_question.score}/ {current_question.question_number}")





