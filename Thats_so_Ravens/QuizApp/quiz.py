import collections
import Thats_so_Ravens.Helpers as helpers
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
    

    def __init__(self, size): 
        self.size = size
        self.screen = pygame.display.set_mode(size) 
        self.score = 0 
        self.q_count = 0
        self.b_press = False
        self.questions = []
        self.file=" hamlesFile "
        self.cor_text = ''
        self.cor_img = ''
        
        self.calibri_35 = pygame.font.SysFont('Calibri', 35,True,False)
        self.calibri_18 = pygame.font.SysFont('Calibri', 18,True,False)
        self.clock = pygame.time.Clock()
        self.background = helpers.init_and_resize_image('QuizApp/quizAssets/ImagesForQuizApp/interim-background.png', self.screen.get_size())
        self.greenButton = helpers.init_and_resize_image('QuizApp/quizAssets/ImagesForQuizApp/green_button_free.png', (helpers.normalize(self.size, helpers.normalize(self.size, 220, 'x'), 'x'),helpers.normalize(self.size, 132, 'y')))
        self.redButton = helpers.init_and_resize_image('QuizApp/quizAssets/ImagesForQuizApp/red_button_free.png', (helpers.normalize(self.size, 220, 'x'),helpers.normalize(self.size, 132, 'y')))
        self.whiteButton = helpers.init_and_resize_image('QuizApp/quizAssets/ImagesForQuizApp/blue_button_free.png', (helpers.normalize(self.size, 220, 'x'),helpers.normalize(self.size, 132, 'y')))
        self.blueButton = helpers.init_and_resize_image('QuizApp/quizAssets/ImagesForQuizApp/purple_button_free.png', (helpers.normalize(self.size, 220, 'x'),helpers.normalize(self.size, 132, 'y')))
        self.init_colorkeys(WHITE)

        self.backButtonBlue = helpers.init_and_resize_image('QuizApp/quizAssets/ImagesForQuizApp/back_button_blue.png', (helpers.normalize(self.size, 40, 'x'), helpers.normalize(self.size, 40, 'x')))
        self.backButtonBlack = helpers.init_and_resize_image('QuizApp/quizAssets/ImagesForQuizApp/back_button_black.png', (helpers.normalize(self.size, 40, 'x'), helpers.normalize(self.size, 40, 'x')))

        self.init_questions()
        
        
##### INIT HELPERS        
    def init_colorkeys(self, color):
        self.greenButton.set_colorkey(color)        
        self.redButton.set_colorkey(color)
        self.whiteButton.set_colorkey(color)        
        self.blueButton.set_colorkey(color)

    def init_questions(self):  #get array of questions 
        (Qarr, Aarr)  = parse.parsing() 
        for i in range(0,5):
            self.questions.append(Question().init_question(Qarr[i], Aarr[i]))
############## End of INIT HELPERS

    def make_answers(self, event):
        self.make_button(event, helpers.normalize(self.size, 60, 'x'), helpers.normalize(self.size, 520, 'y'), helpers.normalize(self.size, 220, 'x'), helpers.normalize(self.size, 132, 'y'), 0)
        self.make_button(event, helpers.normalize(self.size, 290, 'x'), helpers.normalize(self.size, 520, 'y'), helpers.normalize(self.size, 220, 'x'), helpers.normalize(self.size, 132, 'y'), 1)
        self.make_button(event, helpers.normalize(self.size, 60, 'x'), helpers.normalize(self.size, 657, 'y'), helpers.normalize(self.size, 220, 'x'), helpers.normalize(self.size, 132, 'y'), 2)
        self.make_button(event, helpers.normalize(self.size, 290, 'x'), helpers.normalize(self.size, 657, 'y'), helpers.normalize(self.size, 220, 'x'), helpers.normalize(self.size, 132, 'y'), 3)

    
    def make_score(self):
        score_coordinates = [helpers.normalize(self.size, 475, 'x'), helpers.normalize(self.size, 30, 'y')]
        temp_text="Score: "+str(self.score)
        score_text = self.calibri_18.render(temp_text, True, BLACK)
        self.screen.blit(score_text, score_coordinates)
        
    def make_button(self, event, left, top, width, height, buttonNum):            
        mouse = pygame.mouse.get_pos()
        answer = self.questions[self.q_count].get_answer_at_index(buttonNum) 
        coordinates_text=[left+helpers.normalize(self.size, 15, 'x'), top+helpers.normalize(self.size, 15, 'y')]
        text = self.calibri_18.render(answer.get_text(), True, BLACK)   
        if not self.b_press:
            if left+width > mouse[0] > left and top < mouse[1] < top+height: 
                rect = self.screen.blit(self.blueButton, [(left), (top)])       
                self.screen.blit(text, coordinates_text)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.b_press=True
                    if answer.get_correct():
                        # self.cor_text = "Correct !"
                        self.cor_img = helpers.init_and_resize_image('QuizApp/quizAssets/ImagesForQuizApp/checkmark.png', (helpers.normalize(self.size, 300, 'x'), helpers.normalize(self.size, 100, 'y')))
                        self.score+=1
                    else:
                        # self.cor_text = "WRONG!!"
                        self.cor_img = helpers.init_and_resize_image('QuizApp/quizAssets/ImagesForQuizApp/Wrong.png', (helpers.normalize(self.size, 300, 'x'), helpers.normalize(self.size, 100, 'y')))
                        rect = self.screen.blit(self.redButton,[left, top])
                        self.screen.blit(text, coordinates_text)
            else:
                rect = self.screen.blit(self.whiteButton, [(left), (top)])       
                self.screen.blit(text, coordinates_text)                
        else: 
            if answer.get_correct():
                rect = self.screen.blit(self.greenButton, [left, top])
                self.screen.blit(text, coordinates_text)
            else:
                rect = self.screen.blit(self.redButton, [left, top])
                self.screen.blit(text, coordinates_text)          
    
    
    def fresh_screen(self, event=False):
        backgroundRect=self.background.get_rect()
        self.screen.blit(self.background, self.background.get_rect())        
        self.make_score() 
        helpers.make_question(self)
        if event:
            self.make_answers(event)
        
    def run_screen(self):

        pygame.display.set_caption("Try and pass ECOR 1010, In Mcrae We Trust")
        
        self.fresh_screen()
        
        this_font = pygame.font.SysFont('Calibri', 25, True, False)      
        
        timeout = False
        back = False
        done = False
        while not (back or done or timeout): 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done=True #true or false value
                    break;
                #elif event.type == pygame.MOUSEBUTTONDOWN:
                    #click_sound.play()
                
                if self.q_count<len(self.questions):
                    self.make_answers(event)
                back = helpers.make_back(self, event)
                if self.b_press: 
                    self.fresh_screen(event) #setsScoreToNewValue
                    #trigger the clock to wait for like 1 seccond to proccess information that will be presented to screen the clock wait is pygame.time.wait(#of milliseconds
                    self.b_press = False
                    #correct_text = this_font.render(self.cor_text, True, BLACK)
                    self.screen.blit(self.cor_img, [helpers.normalize(self.size, 130, 'x'), helpers.normalize(self.size, 390, 'y')])
                    pygame.display.flip()##wont be needed after clock
                    pygame.time.wait(3000)
                    self.q_count+=1
                    self.fresh_screen()
                #after time passed, want to go to bulrb screen, contians image top left and info below
                pygame.display.flip()	
        if done:    
            return done   
        elif back:
            return done
        else: 
            return done

#click_sound = pygame.mixer.Sound("laser5.ogg")
#click_sound.play

