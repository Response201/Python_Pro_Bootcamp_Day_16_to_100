import html

class QuizBrain:

    def __init__(self, q_list):

        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    # Returnerar True om det finns fler frågor
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # Hämtar nästa fråga
    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return q_text

    # Kontrollerar om användarens svar är korrekt
    def check_answer(self, user_answer):

            correct_answer = self.current_question.answer
            if user_answer.lower() == correct_answer.lower():
                self.score += 1
                print("You got it right!")
                return True
            else:
                print("That's wrong.")
                return False


