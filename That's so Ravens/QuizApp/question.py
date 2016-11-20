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
    
    def get_correct(self):
        return self.correct
        
    def get_question(self):
        return self.question
    
    def set_correct(self, index):
        self.correct = self.get_answer_at_index(index).isCorrect()
        
    def init_question(self, number):
        self.question = parse.parsing(number)[0]
        self.answers.append(AnswerText(parse.parsing(number)[1], True))
        for i in range(0,3):
            self.answers.append(AnswerText(parse.parsing(number)[2][i], False))
        np.random.shuffle(self.answers)

question = Question()
question.init_question(0)
print question.answers[0].get_text()