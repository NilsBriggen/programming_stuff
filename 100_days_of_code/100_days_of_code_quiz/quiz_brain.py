class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
    
    def still_has_questions(self):
        return len(self.question_list) > self.question_number
 
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Level: {current_question.level}\nQ.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(
            user_answer, self.question_list[self.question_number-1].answer)
        
    def check_answer(self, user_answer, true_answer):
        if user_answer.lower() == true_answer.lower():
            print("You got it right!")
            self.score += 1
            print(f"Your score is {self.score}/{self.question_number}\n")
        else:
            print("That's wrong.")
            print(f"The correct answer was: {true_answer}.")
            print(f"Your score is {self.score}/{self.question_number}\n")
        
        
