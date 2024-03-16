class QuizBrain:
    def __init__(self, question):
        self.question_number = 0
        self.question_list = question
        self.score = 0
        
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False): ")
        self.question_number += 1
        self.check_answer(user_answer, current_question.answer)

    
    def still_has_question(self):
        if self.question_number < len(self.question_list): 
            return True
        else:
            return False
        
    def check_answer(self, user_answer, correct_answer):
        self.number_of_answered_question += 1
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print('You got it right!')
            #return True
        else:
            print('you got it wrong!')
            #return False
        
        print(f'The correct answer is {correct_answer}')
        print(f'Your current score is {self.score}/{self.question_number}')
        print('\n')
        

    def announce_final_score(self):
        print('You have competed the quiz')
        print(f'Your final score is {self.score}/{self.question_number}')