import Helpers as helpers
import pygame
from QuizApp.quiz import Quiz
from MazeApp.maze import Maze
from PureMagicApp.PureMagic import PureMagic
  
def run_app():
    GameStarter = Quad((1080, 1920))
    GameStarter.run_screen()

class Quad:
        
        def __init__(self, size):
                self.size = size
                self.block = 0
                self.b_press = False
                self.done = False
                self.maze = Maze(size, (6,10))
                self.quiz = Quiz(size)
                self.screen = pygame.display.set_mode(size)

        def wait_for_click(self):
            pygame.event.set_allowed(None)
            pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
            pygame.event.wait()
            pygame.event.clear()
            pygame.event.set_allowed(pygame.MOUSEMOTION)

        def make_button(self, event, left, top, width, height, blockNum):     
            mouse = pygame.mouse.get_pos()
            
            if not self.b_press:
                if left+width > mouse[0] > left and top < mouse[1] < top+height: 
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.b_press=True
            else: 
                if blockNum==1:        
                    self.done=self.quiz.run_screen()
                    self.b_press=False
                    pygame.display.set_caption("Welcome To Mackenzie Quad")
                    return 
                elif blockNum==4:
                    self.done=self.maze.run_screen()
                    self.b_press=False
                    pygame.display.set_caption("Welcome To Mackenzie Quad")
                    return
                elif blockNum == 2:
                    self.screen.blit(pygame.transform.scale(pygame.image.load("Thats_so_Ravens/assets/InfoAssets/magic_intro_red.png"), self.size), (0, 0))
                    pygame.display.flip()
                    self.wait_for_click()
                    pygame.display.iconify()
                    self.done = PureMagic().run()
                    pygame.display.toggle_fullscreen()
                    self.screen.blit(pygame.transform.scale(pygame.image.load("Thats_so_Ravens/assets/InfoAssets/magic_end_C-_red.png"), self.size), (0, 0))
                    pygame.display.flip()
                    self.b_press=False
                    pygame.display.set_caption("Welcome To Mackenzie Quad")


        def run_screen(self): 
            pygame.display.set_caption("Welcome To Mackenzie Quad")
            pygame.mouse.set_pos(self.screen.get_rect().center)
                                            
            zFrame_background = pygame.transform.scale(pygame.image.load("Thats_so_Ravens/QuizApp/QuadAdjust.jpg").convert(), self.screen.get_size())
            backgroundRect=zFrame_background.get_rect()
                                                                           
            
            while not self.done: 
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.done=True #true or false value
                    #elif event.type == pygame.MOUSEBUTTONDOWN:
                       # print("wil play sound")
                        #click_sound.play()
                                                    
                self.screen.blit(zFrame_background, backgroundRect) 
                self.make_button(event,
                                 helpers.normalize(self.quiz.size, 460, 'x'),
                                 helpers.normalize(self.quiz.size, 0, 'y'),
                                 helpers.normalize(self.quiz.size, 100, 'x'),
                                 helpers.normalize(self.quiz.size, 840, 'y'), 1)
                self.make_button(event, helpers.normalize(self.quiz.size,0, 'x'),
                                 helpers.normalize(self.quiz.size, 480, 'y'),
                                 helpers.normalize(self.quiz.size, 71, 'x'),
                                 helpers.normalize(self.quiz.size, 375, 'y'), 4)
                self.make_button(event, helpers.normalize(self.quiz.size, 50, 'x'),
                                 helpers.normalize(self.quiz.size, 0, 'y'),
                                 helpers.normalize(self.quiz.size, 400, 'x'),
                                 helpers.normalize(self.quiz.size, 100, 'y'), 2)
                pygame.display.flip()
            
            pygame.quit()                                                           

run_app()