from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuaizIntetrface:
    #Cerating and setting up the window
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizz")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)
        self.score_lable = Label(text="Score: 0", bg="white")
        self.score_lable.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     width= 280,
                                                     text="questions here",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic")
                                                    )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        true = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true, highlightthickness=0, command=self.question_correct)
        self.true_button.grid(row=2, column=0)
        false = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false, highlightthickness=0, command=self.question_wrong)
        self.false_button.grid(row=2, column=1)
        self.get_next()

        self.window.mainloop()
    #Showing next question
    def get_next(self):
        self.canvas.config(bg="white")
        #if have next question then shows otherwise disables the butttons
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_lable.config(text=f"Score {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text = q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    #Verifies the questuion
    def question_correct(self):
        ans = self.quiz.check_answer("True")
        self.feedback(ans)
    def question_wrong(self):
        self.feedback(self.quiz.check_answer("False"))

    #Based on the given answer, gives color to the window
    def feedback(self, answer):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next)












