import collections
import pygame
import time
import thread
from timer import Timer
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
        self.timeout=False
        self.timer = Timer(self.screen, self.normalize(410, 'x'), self.normalize(470, 'y'), 'quizAssets/ImagesForQuizApp/TimerBackground.png')
        self.timer2 = Timer(self.screen, self.normalize(410, 'x'), self.normalize(470, 'y'), 'quizAssets/ImagesForQuizApp/TimerBackground.png')
        #self.timeoutTimer = Timer(self.screen)
        self.calibri_35 = pygame.font.SysFont('Calibri', 35,True,False)
        self.calibri_18 = pygame.font.SysFont('Calibri', 18,True,False)
        self.clock = pygame.time.Clock()
        self.background = self.init_and_resize_image('interim-background.png', self.screen.get_size())
        self.greenButton = self.init_and_resize_image('green_button_free.png', (self.normalize(self.normalize(220, 'x'), 'x'),self.normalize(132, 'y')))
        self.redButton = self.init_and_resize_image('red_button_free.png', (self.normalize(220, 'x'),self.normalize(132, 'y')))
        self.whiteButton = self.init_and_resize_image('blue_button_free.png', (self.normalize(220, 'x'),self.normalize(132, 'y')))
        self.blueButton = self.init_and_resize_image('purple_button_free.png', (self.normalize(220, 'x'),self.normalize(132, 'y')))  
        self.init_colorkeys(WHITE)

        self.backButtonBlue = self.init_and_resize_image('back_button_blue.png', (self.normalize(40, 'x'), self.normalize(40, 'x')))
        self.backButtonBlack = self.init_and_resize_image('back_button_black.png', (self.normalize(40, 'x'), self.normalize(40, 'x')))

        self.init_questions()
        
        
##### INIT HELPERS        
    def init_colorkeys(self, color):
        self.greenButton.set_colorkey(color)        
        self.redButton.set_colorkey(color)
        self.whiteButton.set_colorkey(color)        
        self.blueButton.set_colorkey(color)        
        
    def init_and_resize_image(self, filename, size):
        return pygame.transform.scale(pygame.image.load("quizAssets/ImagesForQuizApp/"+filename), size)
    
    def init_questions(self):  #get array of questions 
        (Qarr, Aarr)  = parse.parsing() 
        for i in range(0,5):
            self.questions.append(Question().init_question(Qarr[i], Aarr[i]))
############## End of INIT HELPERS

    def normalize(self, coordinate, x_or_y):
        if x_or_y == 'x':
            number = self.size[0]*(coordinate/560.0)
        else:
            number = self.size[1]*(coordinate/840.0)
        return int(number)
        
    def make_question(self):
        def split_question_print_text(text, arr):
            if(len(text)>25 and text.find(' ', 21)!=-1):
                num = text.find(' ', 25) if 0<text.find(' ', 25)<=26 else text.find(' ', 21)
                arr.append(self.calibri_35.render(text[:num],True,BLACK))
                return split_question_print_text(text[num:], arr)
            else: 
                arr.append(self.calibri_35.render(text,True,BLACK))
                return arr
                 
        base_q_coordinates = [X, Y] = [60, 290]
        augment_coordinates = [Xa, Ya] = [0, 32]       
        text = self.questions[self.q_count].get_question() if self.q_count < len(self.questions) else  "Finished, Hope you passed."
        print_statement = split_question_print_text(text, [])
        for i in range(0,len(print_statement)): 
            self.screen.blit(print_statement[i], [X, Y + Ya*i])
        
        
    def make_answers(self, event):
        self.make_button(event, self.normalize(60, 'x'), self.normalize(520, 'y'), self.normalize(220, 'x'), self.normalize(132, 'y'), 0)
        self.make_button(event, self.normalize(290, 'x'), self.normalize(520, 'y'), self.normalize(220, 'x'), self.normalize(132, 'y'), 1)
        self.make_button(event, self.normalize(60, 'x'), self.normalize(657, 'y'), self.normalize(220, 'x'), self.normalize(132, 'y'), 2)
        self.make_button(event, self.normalize(290, 'x'), self.normalize(657, 'y'), self.normalize(220, 'x'), self.normalize(132, 'y'), 3)        

    
    def make_score(self):
        score_coordinates = [self.normalize(475, 'x'), self.normalize(30, 'y')]
        temp_text="Score: "+str(self.score)
        score_text = self.calibri_18.render(temp_text, True, BLACK)
        self.screen.blit(score_text, score_coordinates)
            
    def make_back(self, event):
        back_pressed=True
        mouse = pygame.mouse.get_pos()
        x_center = self.normalize(30, 'x')
        y_center = self.normalize(30, 'y')
        side = 40
        coordinates_button=(x_center-(side/2), y_center-(side/2)) 
        #print("between "+str(x_center-radius) +" and " + str(x_center+radius) + " andBetween " + str(y_center-radius) +" and " + str(y_center+radius))
        if (x_center-(side/2) < mouse[0] < x_center+(side/2)) and (y_center-(side/2) < mouse[1] < y_center+(side/2)): 
            self.screen.blit(self.backButtonBlue, coordinates_button)
            if event.type == pygame.MOUSEBUTTONDOWN: return back_pressed
            else: return not back_pressed
        else:
            self.screen.blit(self.backButtonBlack, coordinates_button)
            return not back_pressed    

                                 
                 
        
    def make_button(self, event, left, top, width, height, buttonNum):            
        mouse = pygame.mouse.get_pos()
        answer = self.questions[self.q_count].get_answer_at_index(buttonNum) 
        coordinates_text=[left+self.normalize(15, 'x'), top+self.normalize(15, 'y')]
        text = self.calibri_18.render(answer.get_text(), True, BLACK)   
        if not self.b_press:
            if left+width > mouse[0] > left and top < mouse[1] < top+height: 
                rect = self.screen.blit(self.blueButton, [(left), (top)])       
                self.screen.blit(text, coordinates_text)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.b_press=True
                    if answer.get_correct():
                        self.cor_img = self.init_and_resize_image('checkmark.png', (self.normalize(300, 'x'), self.normalize(100, 'y')))
                        self.score+=1
                    else:
                        self.cor_img = self.init_and_resize_image('wrong.png', (self.normalize(300, 'x'), self.normalize(100, 'y')))
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
        self.make_question()
        if event:
            self.make_answers(event)
        
    def run_screen(self):
        pygame.display.set_caption("Try and pass ECOR 1010, In Mcrae We Trust")

        self.fresh_screen()
        switch_q = False
        this_font = pygame.font.SysFont('Calibri', 25, True, False)
        self.timeout = False
        back = False
        done = False
        self.timer.runAndPrintTimer(30, 0)
        while not (back or done or self.timeout):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done=True #true or false value
                    break
                #elif event.type == pygame.MOUSEBUTTONDOWN:
                    #click_sound.play()
                back = self.make_back(event)
                if self.q_count<len(self.questions) and not self.timer2.running:
                    self.make_answers(event)
                if not self.b_press and  not self.timer.running:
                    self.cor_img = self.init_and_resize_image('wrong.png', (self.normalize(300, 'x'), self.normalize(100, 'y')))
                    self.b_press = True
                if self.b_press and not switch_q:
                    self.timer.stop()
                    self.fresh_screen(event) #setsScoreToNewValue
                    self.screen.blit(self.cor_img, [self.normalize(130, 'x'), self.normalize(390, 'y')])
                    pygame.display.flip()
                    self.timer2.runTimer(3, 0)
                    switch_q = True
                    print(self.timer2.running)
                if switch_q and not self.timer2.running:
                    self.q_count += 1
                    self.b_press = False
                    switch_q = False
                    self.fresh_screen()
                    self.timer.runAndPrintTimer(30, 0)

                #after time passed, want to go to bulrb screen, contians image top left and info below
                pygame.display.flip()
                #if not self.timeoutTimer.running(): self.timeout = False

        if done:    
            return done   
        elif back:
            return done
        else: 
            return done

#click_sound = pygame.mixer.Sound("laser5.ogg")
#click_sound.play

