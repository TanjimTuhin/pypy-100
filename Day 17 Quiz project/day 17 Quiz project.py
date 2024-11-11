from Question_model import Question
from data import question_data
#-------------------------------------------
# question_data = [
# {"text": "A slug's blood is green.", "answer": "True"},
# {"text": "The loudest animal is the African Elephant.", "answer": "False"}]
# #-------------------------------------------
# class Question:
#     def __init__(self, q_text, q_answer):
#         self.text = q_text
#         self.answer = q_answer
#-------------------------------------------        
question_bank=[]
for question in question_data:
    question_text= question["text"]
    question_answer= question["answer"]
    new_question=Question(question_text, question_answer )
    question_bank.append(new_question) 

print(question_bank[0].answer)



