class AnswerText:
    def __init__(self, text='', correct=False):
        self.text = text
        self.correct = correct
        
    def get_text(self):
        return self.text
    
    def get_correct(self):
        return self.correct
    
    def set_text(self, text):
        self.text = text
        
    def set_correct(self, correct):
        self.correct = correct
    
    
        
class AnswerImg:
    def __init__(self):
        self.image = ''
        self.correct = False
        
    def get_text(self):
        return self.text
    
    def get_correct(self):
        return self.correct
    
    def set_text(self, imageFile):
        self.image = imageFile
        
    def set_correct(self, correct):
        self.correct = correct