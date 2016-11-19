
import pygame
from pygame import * 
pygame.init()

class Quiz: 
    #TODO: add passing of money to quiz
    
    def __init__(self): 
        self.screen = '' 
        self.qFrame = '' 
        self.score = 0 
        self.q_num = 0
        self.questions = []
        self.file=" hamlesFile "
        #self.init_questions(self)
        
        
    def init_screen(self):
        
        
        pygame.display.set_caption("Quiz App Launching")
        
        zFrame_background = pygame.image.load("quizAssets\ImagesForQuizApp\portraitBackgroundGood.jpg")
        backgroundRect=zFrame_background.get_rect()
        size = (width, length) = zFrame_background.get_size()
        self.screen = pygame.display.set_mode(size)
        
        done = False
        while not done: 
            for event in pygame.event.get():
                done = event.type == pygame.QUIT #true or false value
                self.screen.blit(zFrame_background, backgroundRect)
         
        
        
        
        
        
quiz = Quiz()
        
        
quiz.init_screen()
    