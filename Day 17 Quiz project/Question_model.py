class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

class QuizBrain:
    def __init__(self, q_list):
        self.question_number=0
        self.question_list=q_list
    def next_question(self): 
        current_question=self.question_list[self.question_number]
               
