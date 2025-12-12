class QuizBrain:
    def  __init__(self, q_number, q_list, ):
        self.question_number = 0
        self.question_list= q_list
        self.score = 0

    # Return True if there are more questions to ask
    def still_has_question_left(self):
           return self.question_number < len(self.question_list)


    # Display the question and validate the user's answer
    def next_question(self):

           current_question = self.question_list[self.question_number].text
           number_question = self.question_number + 1

           uses_answer = input(f"{number_question}. {current_question} True or False\n").lower()

           # Validate the input
           while uses_answer != "true" and uses_answer != "false":
               print("Wrong input")
               uses_answer = input(f"True or False\n").lower()

           # Check if answer where correct
           self.check_if_correct_answer(uses_answer.title())



    # Compare the user's answer with the correct one and update the score
    def check_if_correct_answer(self, user_answer):

        correct_answer = self.question_list[self.question_number].answer

        if correct_answer == user_answer:
            self.score += 1
            print(f"That's correct")
        else:
            print(f"That's wrong")
        print(f"Your current score is: {self.score}/{self.question_number + 1}\n")
        self.question_number += 1









