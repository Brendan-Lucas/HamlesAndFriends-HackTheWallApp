import Helpers as helpers
import pygame
from QuizApp.quiz import Quiz
from MazeApp.maze import Maze
from PureMagicApp.PureMagic import PureMagic
  
def run_app():
    GameStarter = Quad((560, 840))
    GameStarter.run_screen()        


class Quad:
        
        def __init__(self, size):
                self.b_press = False
                self.done = False
                self.maze = Maze(size, (10,15))
                self.quiz = Quiz(size)
                self.screen = pygame.display.set_mode(size)
                

        def make_button(self, event, left, top, width, height, blockNum):
            if event == pygame.MOUSEBUTTONDOWN:
                if left+width > event.pos[0] > left and top < event.pos[1] < top+height:
                    if blockNum == 4:
                        print event
                        print("running quiz")
                        self.done = self.quiz.run_screen()
                        self.b_press = False
                        pygame.display.set_caption("Welcome To Mackenzie Quad")
                        print("fiished running quiz")
                        return
                    elif blockNum == 1:
                        self.done = self.maze.run_screen()
                        self.b_press = False
                        pygame.display.set_caption("Welcome To Mackenzie Quad")
                        return
                    elif blockNum == 2:
                        pygame.display.iconify()
                        self.done = PureMagic().run()
                        pygame.display.toggle_fullscreen()
                        self.b_press = False
                        pygame.display.set_caption("Welcome To Mackenzie Quad")

            # if not self.b_press:
            #     if left+width > mouse[0] > left and top < mouse[1] < top+height:
            #         if event.type == pygame.MOUSEBUTTONDOWN:
            #             self.b_press=True
            # else:
            #     if blockNum==1:
            #         self.done=self.quiz.run_screen()
            #         self.b_press=False
            #         pygame.display.set_caption("Welcome To Mackenzie Quad")
            #         return
            #     elif blockNum==4:
            #         self.done=self.maze.run_screen()
            #         self.b_press=False
            #         pygame.display.set_caption("Welcome To Mackenzie Quad")
            #         return
            #     elif blockNum == 2:
            #         pygame.display.iconify()
            #         self.done = PureMagic().run()
            #         pygame.display.toggle_fullscreen()
            #         self.b_press=False
            #         pygame.display.set_caption("Welcome To Mackenzie Quad")


        def run_screen(self): 
            pygame.display.set_caption("Welcome To Mackenzie Quad")
            pygame.mouse.set_pos(self.screen.get_rect().center)
                                            
            zFrame_background = pygame.transform.scale(pygame.image.load("QuizApp/QuadAdjust.jpg").convert(), self.screen.get_size())
            backgroundRect=zFrame_background.get_rect()
                                                                           
            
            while not self.done: 
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.done=True #true or false value
                    #elif event.type == pygame.MOUSEBUTTONDOWN:
                       # print("wil play sound")
                        #click_sound.play()

                    self.screen.blit(zFrame_background, backgroundRect)
                    self.make_button(event, helpers.normalize(self.quiz.size, 522, 'x'),
                                     helpers.normalize(self.quiz.size, 210, 'y'),
                                     helpers.normalize(self.quiz.size, 34, 'x'),
                                     helpers.normalize(self.quiz.size, 589, 'y'), 1)
                    self.make_button(event,
                                     helpers.normalize(self.quiz.size, 65, 'x'),
                                     helpers.normalize(self.quiz.size, 0, 'y'),
                                     helpers.normalize(self.quiz.size, 387, 'x'),
                                     helpers.normalize(self.quiz.size, 95, 'y'), 2)
                    self.make_button(event, helpers.normalize(self.quiz.size, 0, 'x'),
                                     helpers.normalize(self.quiz.size, 368, 'y'),
                                     helpers.normalize(self.quiz.size, 71, 'x'),
                                     helpers.normalize(self.quiz.size, 468, 'y'), 4)
                    pygame.display.flip()
                    # pygame.event.clear()
            
            pygame.quit()                                                           

run_app()