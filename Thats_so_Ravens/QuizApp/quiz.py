import pygame
import Thats_so_Ravens.Helpers as helpers
import Thats_so_Ravens.info
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
        self.clock = pygame.time.Clock()
        self.b_press = False
        self.back = False
        self.done = False
        self.switch_q = False
        self.questions = []
        self.file=" hamlesFile "
        self.cor_text = ''
        self.cor_img = ''
        self.timeout=False
        self.timer = Timer(self.screen, helpers.normalize(self.size, 410, 'x'), helpers.normalize(self.size, 470, 'y'), "assets/TimerBackground.png")
        self.timer2 = Timer()
        self.timeoutTimer = Timer()
        self.calibri_35 = pygame.font.SysFont('Calibri', 35,True,False)
        self.calibri_18 = pygame.font.SysFont('Calibri', 18,True,False)
        self.background = self.init_and_resize_image('interim-background.png', self.screen.get_size())
        self.greenButton = self.init_and_resize_image('green_button_free.png', (helpers.normalize(self.size, helpers.normalize(self.size, 220, 'x'), 'x'),helpers.normalize(self.size, 132, 'y')))
        self.redButton = self.init_and_resize_image('red_button_free.png', (helpers.normalize(self.size, 220, 'x'),helpers.normalize(self.size, 132, 'y')))
        self.whiteButton = self.init_and_resize_image('blue_button_free.png', (helpers.normalize(self.size, 220, 'x'),helpers.normalize(self.size, 132, 'y')))
        self.blueButton = self.init_and_resize_image('purple_button_free.png', (helpers.normalize(self.size, 220, 'x'),helpers.normalize(self.size, 132, 'y')))
        self.init_colorkeys(WHITE)

        self.backButtonBlue = self.init_and_resize_image('back_button_blue.png', (helpers.normalize(self.size, 40, 'x'), helpers.normalize(self.size, 40, 'x')))
        self.backButtonBlack = self.init_and_resize_image('back_button_black.png', (helpers.normalize(self.size, 40, 'x'), helpers.normalize(self.size, 40, 'x')))

        self.init_questions()


##### INIT HELPERS
    def init_colorkeys(self, color):
        self.greenButton.set_colorkey(color)
        self.redButton.set_colorkey(color)
        self.whiteButton.set_colorkey(color)
        self.blueButton.set_colorkey(color)

    def init_and_resize_image(self, filename, size):
        return pygame.transform.scale(pygame.image.load("QuizApp/quizAssets/ImagesForQuizApp/"+filename), size)

    def init_questions(self):  #get array of questions
        (Qarr, Aarr)  = parse.parsing()
        for i in range(0,5):
            self.questions.append(Question().init_question(Qarr[i], Aarr[i]))
############## End of INIT HELPERS
    #Make questions fit within size provided and blit question lines to screen font 35
    # --requires background blit before
    def make_question(self, font=None):
        if font is None: font = self.calibri_35
        base_q_coordinates = [X, Y] = [60, 290]
        augment_coordinates = [Xa, Ya] = [0, 32]
        text = self.questions[self.q_count].get_question() if self.q_count < len(self.questions) else  "Finished, Hope you passed."
        print_statement = helpers.split_question_print_text(text, [], font)
        for i in range(0,len(print_statement)):
            self.screen.blit(print_statement[i], [X + Xa*i, Y + Ya*i])
    #Blit Score: self.score to screen in top right corner font 18
    # --requires blit background first
    def make_score(self):
        score_coordinates = [helpers.normalize(self.size, 475, 'x'), helpers.normalize(self.size, 30, 'y')]
        temp_text="Score: "+str(self.score)
        score_text = self.calibri_18.render(temp_text, True, BLACK)
        self.screen.blit(score_text, score_coordinates)

    #Blits back button to screen and listens for action,
    # -- hopefully replaced by action listener.
    def make_back(self, event=None):
        back_pressed=True
        x_center = helpers.normalize(self.size, 30, 'x')
        y_center = helpers.normalize(self.size, 30, 'y')
        side = 40
        coordinates_button=(x_center-(side/2), y_center-(side/2))
        mouse = pygame.mouse.get_pos()
        if (x_center-(side/2) < mouse[0] < x_center+(side/2)) and (y_center-(side/2) < mouse[1] < y_center+(side/2)):
            self.screen.blit(self.backButtonBlue, coordinates_button)
            if event:
                if event.type == pygame.MOUSEBUTTONDOWN: return back_pressed
                else: return not back_pressed
        else:
            self.screen.blit(self.backButtonBlack, coordinates_button)
            return not back_pressed

    def make_answers(self, event=None):
        self.make_button(helpers.normalize(self.size, 60, 'x'), helpers.normalize(self.size, 520, 'y'), helpers.normalize(self.size, 220, 'x'), helpers.normalize(self.size, 132, 'y'), 0, event)
        self.make_button(helpers.normalize(self.size, 290, 'x'), helpers.normalize(self.size, 520, 'y'), helpers.normalize(self.size, 220, 'x'), helpers.normalize(self.size, 132, 'y'), 1, event)
        self.make_button(helpers.normalize(self.size, 60, 'x'), helpers.normalize(self.size, 657, 'y'), helpers.normalize(self.size, 220, 'x'), helpers.normalize(self.size, 132, 'y'), 2, event)
        self.make_button(helpers.normalize(self.size, 290, 'x'), helpers.normalize(self.size, 657, 'y'), helpers.normalize(self.size, 220, 'x'), helpers.normalize(self.size, 132, 'y'), 3, event)

    def make_button(self, left, top, width, height, buttonNum, event=None):
        mouse = pygame.mouse.get_pos()
        answer = self.questions[self.q_count].get_answer_at_index(buttonNum)
        coordinates_text=[left+helpers.normalize(self.size, 15, 'x'), top+helpers.normalize(self.size, 15, 'y')]
        text = self.calibri_18.render(answer.get_text(), True, BLACK)
        if not self.b_press:
            if left+width > mouse[0] > left and top < mouse[1] < top+height:
                rect = self.screen.blit(self.blueButton, [(left), (top)])
                self.screen.blit(text, coordinates_text)
                if event is not None:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.b_press=True
                        if answer.get_correct():
                            self.cor_img = self.init_and_resize_image('checkmark.png', (helpers.normalize(self.size, 300, 'x'), helpers.normalize(self.size, 100, 'y')))
                            self.score+=1
                        else:
                            self.cor_img = self.init_and_resize_image('Wrong.png', (helpers.normalize(self.size, 300, 'x'), helpers.normalize(self.size, 100, 'y')))
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

    def answer_stage(self, image):
        self.timer.stop()
        self.timer2.runTimer(2, 0)
        self.init_screen()
        self.screen.blit(self.cor_img, [helpers.normalize(self.size, 130, 'x'), helpers.normalize(self.size, 390, 'y')])
        self.make_answers()
        pygame.display.flip()
        while self.timer2.running:
            for event in pygame.event.get():
                self.timeoutTimer.currentTime = 90
                if event.type == pygame.QUIT:
                    self.done = True
                    return self.done
                #elif event.type == pygame.MOUSEBUTTONDOWN:
                    #click_sound.play()
                self.back = self.make_back(event)
                if self.back:
                    return self.done
                pygame.display.flip()
        return False


    def init_screen(self):
        self.screen.blit(self.background, self.background.get_rect())
        self.make_score()
        self.make_back()

    #blit background, score, question, make answer buttons and start timer at 20
    def fresh_screen(self):
        self.screen.blit(self.background, self.background.get_rect())
        self.make_back()
        self.make_score()
        self.make_question()
        self.make_answers()
        self.timer.runAndPrintTimer(20, 0)

    def run_screen(self):
        pygame.display.set_caption("Try and pass ECOR 1010, In Mcrae We Trust")
        self.timeout = False
        self.back = False
        self.done = False
        self.timeoutTimer.runTimer(90, 0)
        #first Info Box explaining quiz runInfo(time)
        while self.q_count < len(self.questions):
            self.switch_q=False #TODO: look at changing to local instead of instance
            self.fresh_screen()
            temp = self.q_count
            while not self.switch_q and self.timeoutTimer.running:
                self.clock.tick(60)
                for event in pygame.event.get():
                    self.timeoutTimer.currentTime = 90
                    if event.type == pygame.QUIT:
                        self.done = True
                        return self.done
                    #elif event.type == pygame.MOUSEBUTTONDOWN:
                        #click_sound.play()
                    self.back = self.make_back(event)
                    if self.back:
                        return self.done
                    if not self.timer2.running: self.make_answers(event) #TODO may not need self.timer2.running in there
                    if not self.b_press and not self.timer.running:
                        self.b_press=True
                        self.cor_img = self.init_and_resize_image('wrong.png', (helpers.normalize(self.size, 300, 'x'), helpers.normalize(self.size, 100, 'y')))
                    if self.b_press: break
                    pygame.display.flip()
                #outside For
                if not self.b_press and not self.timer.running:
                    self.b_press=True
                    self.cor_img = self.init_and_resize_image('wrong.png', (helpers.normalize(self.size, 300, 'x'), helpers.normalize(self.size, 100, 'y')))
                if self.b_press:
                    if self.answer_stage(self.cor_img): return self.done
                    #run info blitting the info to the surface that we already have so that we can continue to update back button and pygame quit
                    #self.run_info(self.screen)
                    self.b_press = False
                    self.switch_q = True
                    self.q_count+=1
            if not self.timeoutTimer.running: break
        return self.done

#click_sound = pygame.mixer.Sound("laser5.ogg")
#click_sound.play
