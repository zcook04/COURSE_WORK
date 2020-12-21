class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f'Q{self.question_number}. {current_question.text} (True/False):  ')
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        '''Returns True or False. Evaluates q_number < len(q_list)'''
        return (self.question_number < len(self.question_list))

    def check_answer(self, user_a, question_a):
        if user_a.lower() == question_a.lower():
            print('Correct')
            self.score += 1
        else:
            print('Wrong')
        print(
            f'The correct answer was {question_a}: \nCurrent Score: {self.score}/{self.question_number}\n\n')
