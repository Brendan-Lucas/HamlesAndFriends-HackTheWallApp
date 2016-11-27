
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
        self.background = pygame.image.load("quizAssets\ImagesForQuizApp\QuizBackgroundAdjust.jpg")
        self.greenButton = pygame.image.load("quizAssets/ImagesForQuizApp/Button_greenAdjust.jpg")
        self.greenButton.set_colorkey(BLACK)
        self.redButton = pygame.image.load("quizAssets/ImagesForQuizApp/Button_redAdjust.jpg")
        self.redButton.set_colorkey(BLACK)
        self.whiteButton = pygame.image.load("quizAssets/ImagesForQuizApp/Button_silverAdjust.jpg")
        self.blueButton = pygame.image.load("quizAssets/ImagesForQuizApp/Button_purpleAdjust.jpg")       
        self.init_questions()
        
    def init_questions(self):  #get array of questions 
        (Qarr, Aarr)  = parse.parsing() 
        for i in range(0,5):
            self.questions.append(Question().init_question(Qarr[i], Aarr[i]))
        
    def make_question(self):
        font = pygame.font.SysFont('Calibri', 35, True, False)
        text = self.questions[self.q_count].get_question()
        printText = font.render(text, True, BLACK)
        self.screen.blit(printText, [10, 290])
    
    def make_score(self):
        score_coordinates = [475, 30]
        temp_text="Score: "+str(self.score)
        score_text = self.font.render(temp_text, True, BLACK)
        self.screen.blit(score_text, score_coordinates)
        
    def make_back(self, event):
        back_pressed=True
        mouse = pygame.mouse.get_pos()
        x_center =30
        y_center = 30
        coordinates_button=(x_center, y_center) 
        radius = 20
        line_thick = 2
        #print("between "+str(x_center-radius) +" and " + str(x_center+radius) + " andBetween " + str(y_center-radius) +" and " + str(y_center+radius))
        if (x_center-radius < mouse[0] < x_center+radius) and (y_center-radius < mouse[1] < y_center+radius): 
            circle = pygame.draw.circle(self.screen, BLUE, coordinates_button, radius, line_thick) 
            if event.type == pygame.MOUSEBUTTONDOWN: return back_pressed
            else: return not back_pressed
        else:
            circle = pygame.draw.circle(self.screen, BLACK, coordinates_button, radius, line_thick)
            return not back_pressed    
                                 
                 
        
    def make_button(self, event, left, top, width, height, buttonNum):            
        mouse = pygame.mouse.get_pos()
        answer = self.questions[self.q_count].get_answer_at_index(buttonNum)
        coordinates_text=[left+15, top+15]
        text = self.font.render(answer.get_text(), True, BLACK)   
        if not self.b_press:
            if left+width > mouse[0] > left and top < mouse[1] < top+height: 
                rect = self.screen.blit(self.blueButton, [(left), (top)])       
                self.screen.blit(text, coordinates_text)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.b_press=True
                    if answer.get_correct():
                        self.cor_text = "Correct !"
                        self.score+=1
                        self.screen.blit(self.greenButton,[left, top])
                        self.screen.blit(text, coordinates_text)
                    else:
                        self.cor_text = "WRONG!!"
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
    
    def fresh_screen(self):
        backgroundRect=self.background.get_rect()
        self.screen.blit(self.background, self.background.get_rect())        
        self.make_score() 
        self.make_question()
        
    def run_screen(self):
        
        pygame.display.set_caption("Try and pass ECOR 1010, In Mcrae We Trust")
        
        size = (width, length) = self.background.get_size()
        self.screen = pygame.display.set_mode(size) 
        
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
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print("will play sound\n")
                    #click_sound.play()
                
                self.make_button(event, 60, 520, 220, 132, 0)
                self.make_button(event, 290, 520, 220, 132, 1)
                self.make_button(event, 60, 657, 220, 132, 2)
                self.make_button(event, 290, 657, 220, 132, 3)
                back = self.make_back(event)
                if self.b_press: 
                    self.make_score()
                    #trigger the clock to wait for like 1 seccond to proccess information that will be presented to screen
                    correct_text = this_font.render(self.cor_text, True, BLACK)
                    self.screen.blit(correct_text, [250, 437])
                    self.q_count+=1
                    self.fresh_screen()
                    self.b_press = False
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