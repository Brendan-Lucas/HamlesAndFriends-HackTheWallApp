from answer import AnswerImg, AnswerText
import parsing as parse
import numpy as np

class Question:
    def __init__(self):
        self.answers = []
        self.question = ''
        self.correct = False
        
    def get_answer_at_index(self, index):
        return self.answers[index]
    
    def get_answers(self):
        return self.answers

    
    def get_correct(self):
        return self.correct
        
    def get_question(self):
        return self.question
    
    def set_correct(self, index):
        self.correct = self.get_answer_at_index(index).isCorrect()
        
    def init_question(self, in_question, in_answers):
        self.question = in_question
        self.answers.append(AnswerText(in_answers[0], True))
        for i in range(1,4):
            self.answers.append(AnswerText(in_answers[i], False))
        np.random.shuffle(self.answers)
        return self

        