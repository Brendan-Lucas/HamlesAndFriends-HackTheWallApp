

class AnswerText:
    def __init__(self):
        self.text = ''
        self.correct = false
        
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
        self.correct = false
        
    def get_text(self):
        return self.text
    
    def get_correct(self):
        return self.correct
    
    def set_text(self, imageFile):
        self.image = imageFile
        
    def set_correct(self, correct):
        self.correct = correct