from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuaizIntetrface

question_bank = []
#Getting the questions and answers ade adding them to question_bank list
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_a   nswer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

#creates the score as 0
quiz = QuizBrain(question_bank)
ui = QuaizIntetrface(quiz)

#Checks if there are some more questions if there, asks the next question
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
