class  QuizBrain:
    def __init__(self, qlist):
        self.question_number = 0
        self.question_list = qlist
        self.score = 0


    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            False

    def next_question(self):
        crnt_question =  self.question_list[self.question_number]
        self.question_number = 1
        u_ans = input(f"Q.{self.question_number}: {crnt_question.text} (True/False): ")
        self.check_answer(u_ans,crnt_question.answer)

    def check_answer(self, user_answer, actual_answer):
        if user_answer == actual_answer:
            self.score += 1
            print("you got it right")
        else:
            print("Your answer is wrong")
        print(f"the current answer: {actual_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")
