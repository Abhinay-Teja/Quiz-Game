
class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
    def next_question(self):
        ques = self.question_list[self.question_number]
        self.question_number += 1
        in_answer = input(f"Q.{self.question_number}: {ques.text} (True/False):")
        self.check_answer(in_answer,ques.answer)
    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"You got it right!")
        else:
            print("Wrong!!")
            pass
        print(f"The correct answer was {correct_answer}")
        print(f"Your Score  {self.score}/{self.question_number}")
        print("\n"*1)



