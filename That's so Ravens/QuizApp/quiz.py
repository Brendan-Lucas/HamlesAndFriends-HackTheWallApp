
import pygame
from pygame import * 
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
        self.qFrame = '' 
        self.score = 0 
        self.q_num = 0
        
        self.questions = []
        self.file=" hamlesFile "
        
        event = ''
        self.clock = pygame.time.Clock()
        self.greenButton = pygame.image.load("quizAssets/ImagesForQuizApp/Button_greenAdjust.jpg")
        self.greenButton.set_colorkey(BLACK)
        self.redButton = pygame.image.load("quizAssets/ImagesForQuizApp/Button_redAdjust.jpg")
        self.redButton.set_colorkey(BLACK)
        self.whiteButton = pygame.image.load("quizAssets/ImagesForQuizApp/Button_silverAdjust.jpg")
        self.blueButton = pygame.image.load("quizAssets/ImagesForQuizApp/Button_purpleAdjust.jpg")       
        #self.init_questions(self)
        
        
    def make_button(self, event, left, top, width, height, Answer):
    
        mouse = pygame.mouse.get_pos()
                    
        if left+width > mouse[0] > left and top < mouse[1] < top+height: 
            rect = self.screen.blit(self.blueButton, [(left), (top)])       
            if event.type == pygame.MOUSEBUTTONDOWN:
                print 'button' + str(mouse)
        else:
            rect = self.screen.blit(self.whiteButton, [(left), (top)])          
        X = left+(width/2)
        Y = top+(height/2)      
        TextFont = pygame.font.Font("freesansbold.ttf",20)                
        
        
        
    def run_screen(self):
        
        pygame.display.set_caption("Quiz App Launching")
        
        zFrame_background = pygame.image.load("quizAssets\ImagesForQuizApp\QuizBackgroundAdjust.jpg")
        backgroundRect=zFrame_background.get_rect()
        size = (width, length) = zFrame_background.get_size()
        self.screen = pygame.display.set_mode(size)
        
        done = False
        while not done: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done=True #true or false value
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print("will play sound\n")
                    #click_sound.play()
                self.screen.blit(zFrame_background, backgroundRect)    
                self.make_button(event, 60, 520, 220, 132, 'plop')
                self.make_button(event, 290, 520, 220, 132, 'plop')
                self.make_button(event, 60, 657, 220, 132, 'plop')
                self.make_button(event, 290, 657, 220, 132, 'plop')                
                
                
                pygame.display.flip()
            
        pygame.quit()        
        

        
    

    
    
#click_sound = pygame.mixer.Sound("laser5.ogg")
#click_sound.play