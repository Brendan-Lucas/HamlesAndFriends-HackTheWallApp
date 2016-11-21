
import pygame
import parsing as parse
from pygame import * 
from question import Question
pygame.init()

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

class Quiz: 
    #TODO: add passing of money to quiz
    
    def __init__(self): 
        self.screen = '' 
        self.score = 0 
        self.q_count = 0
        self.b_press = False
        self.questions = []
        self.file=" hamlesFile "
        self.cor_text = ''
        
        self.font = pygame.font.SysFont('Calibri', 18, True, False)
        self.clock = pygame.time.Clock()
        self.greenButton = pygame.image.load("quizAssets/ImagesForQuizApp/Button_greenAdjust.jpg")
        self.greenButton.set_colorkey(BLACK)
        self.redButton = pygame.image.load("quizAssets/ImagesForQuizApp/Button_redAdjust.jpg")
        self.redButton.set_colorkey(BLACK)
        self.whiteButton = pygame.image.load("quizAssets/ImagesForQuizApp/Button_silverAdjust.jpg")
        self.blueButton = pygame.image.load("quizAssets/ImagesForQuizApp/Button_purpleAdjust.jpg")       
        self.init_questions()
        
    def init_questions(self):  #get array of questions 
        arr = []
        (Qarr, Aarr)  = parse.parsing() 
        for i in range(0,5):
            self.questions.append(Question().init_question(Qarr[i], Aarr[i]))
        
    def make_question(self):
        font = pygame.font.SysFont('Calibri', 35, True, False)
        text = self.questions[self.q_count].get_question()
        printText = font.render(text, True, BLACK)
        self.screen.blit(printText, [10, 290])
    
    
    def make_button(self, event, left, top, width, height, buttonNum):
        
        mouse = pygame.mouse.get_pos()
        answer = self.questions[self.q_count].get_answer_at_index(buttonNum)
        
        text = self.font.render(answer.get_text(), True, BLACK)   
        if not self.b_press:
            if left+width > mouse[0] > left and top < mouse[1] < top+height: 
                rect = self.screen.blit(self.blueButton, [(left), (top)])       
                self.screen.blit(text, [left, top])
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.b_press=True
            else:
                rect = self.screen.blit(self.whiteButton, [(left), (top)])
                self.screen.blit(text, [left, top])
        
        else: 
            if answer.get_correct():
                self.cor_text = "Correct !"
                rect = self.screen.blit(self.greenButton,[left, top])
                self.screen.blit(text, [left, top])
            else:
                self.cor_text = "WRONG!!"
                rect = self.screen.blit(self.redButton,[left, top])
                self.screen.blit(text, [left, top])                
                 
        
        
        
    def run_screen(self):
        
        pygame.display.set_caption("Quiz App Launching")
        
        zFrame_background = pygame.image.load("quizAssets\ImagesForQuizApp\QuizBackgroundAdjust.jpg")
        backgroundRect=zFrame_background.get_rect()
        size = (width, length) = zFrame_background.get_size()
        self.screen = pygame.display.set_mode(size)        
        this_font = pygame.font.SysFont('Calibri', 25, True, False)
        
        
        done = False
        while not done: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done=True #true or false value
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print("will play sound\n")
                    #click_sound.play()
                
                self.screen.blit(zFrame_background, backgroundRect) 
                self.make_question()
                self.make_button(event, 60, 520, 220, 132, 0)
                self.make_button(event, 290, 520, 220, 132, 1)
                self.make_button(event, 60, 657, 220, 132, 2)
                self.make_button(event, 290, 657, 220, 132, 3)                
                if self.b_press: 
                    correct_text = this_font.render(self.cor_text, True, BLACK)
                    self.screen.blit(correct_text, [200, 500])
                
                pygame.display.flip()
            
        pygame.quit()        
        

        
    

    
    
#click_sound = pygame.mixer.Sound("laser5.ogg")
#click_sound.play