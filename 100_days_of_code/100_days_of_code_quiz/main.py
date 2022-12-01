from question_model import *
from data import *
from quiz_brain import *

question_bank = []
for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    question_level = question['difficulty']
    new_question = Question(question_text, question_answer, question_level)
    question_bank.append(new_question)
    
quiz = QuizBrain(question_bank)

while quiz.still_has_questions() == True:
    quiz.next_question()
    
print(f"You've completed the quiz\nYour final score was: {quiz.score}/{quiz.question_number}")
input("Click enter to exit")
