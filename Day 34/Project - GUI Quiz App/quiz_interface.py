import time

from numpy.ma.core import outer

THEME_COLOR = "#375362"
from tkinter import *
from tkinter import Canvas
from quiz_brain import QuizBrain

class QuizInterface:

    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizz")
        self.window.config(padx=20,pady=25, background=THEME_COLOR)
        self.window.grid_rowconfigure(2,weight=1)
        self.window.grid()


        # Score
        self.score_label = Label(text=f"Score: {self.quiz.score}", background=THEME_COLOR,   fg="white", font=("Arial", 12))
        self.score_label.config()
        self.score_label.grid(row=1, column=2)

        # Question count

        self.question_count_label = Label(text=f"{self.quiz.question_number}/{len(self.quiz.question_list)}", background=THEME_COLOR, fg="white", font=("Arial", 12))
        self.question_count_label.grid(row=1, column=1)


        # Question
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280 , text="",
        font=("Arial", 20, "italic" ))

        self.canvas.grid(row=2, column=1, columnspan=2, pady=25)


        # Btn False
        false_image = PhotoImage(file="images/false.png")
        self.btn_false = Button(image=false_image, highlightthickness=0, command=self.answer_false)
        self.btn_false.grid(row=3, column=1, pady=5)



        # Btn True
        true_image = PhotoImage(file="images/true.png")
        self.btn_true = Button(image=true_image, highlightthickness=0, command=self.answer_true)
        self.btn_true.grid(row=3, column=2, pady=5)
        self.get_next_question()


        self.window.mainloop()




    # Hämtar nästa fråga från QuizBrain
    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text = q_text)




    # Visar meddelande när quizet är klart
    def quiz_completed(self):
            self.canvas.itemconfig(self.question_text, text="You've completed the quiz")




    # Hanterar nästa steg efter användarens svar
    def next_step(self):
        self.canvas.config(bg="white", highlightbackground="white")
        self.question_count_label.config(text=f"{self.quiz.question_number}/{len(self.quiz.question_list)}")
        if self.quiz.still_has_questions():
            self.get_next_question()

        else:

            self.btn_true.config(state="disabled")
            self.btn_false.config(state="disabled")
            self.window.after(2000, self.quiz_completed)




    # Kollar om användaren svarade korrekt
    def check_answer(self, answer):

        value = self.quiz.check_answer(answer)
        self.score_label.config(text=f"Score: {self.quiz.score}")

        if value:
            self.canvas.config(bg="green", highlightbackground="green")
        else:
            self.canvas.config(bg="red", highlightbackground="red")

        self.window.after(1000, self.next_step)




    # Användaren trycker på knappen False
    def answer_false(self):
        self.check_answer("False")



    # Användaren trycker på knappen True
    def answer_true(self):
        self.check_answer("True")
