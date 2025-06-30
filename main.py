from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for char in range(0,12):
    var = Question(question_data[char]["text"],question_data[char]["answer"])
    question_bank.append(var)
quiz = QuizBrain(question_bank)
for i in range(0,12):
    quiz.next_question()



