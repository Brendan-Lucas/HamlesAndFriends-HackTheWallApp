import pygame
from quiz import Quiz
from maze import Maze
  
def run_app():
    GameStarter = Quad((560, 840))
    GameStarter.run_screen()        


class Quad:
        
        def __init__(self, size):
                self.block = 0
                self.b_press = False
                self.done = False
                self.maze = Maze((560, 840), (10,15))
                self.quiz = Quiz(size)
                self.screen = pygame.display.set_mode(size)
                

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


        def run_screen(self): 
            pygame.display.set_caption("Welcome To Mackenzie Quad")
                                            
            zFrame_background = pygame.transform.scale(pygame.image.load("QuadAdjust.jpg").convert(), self.screen.get_size())
            backgroundRect=zFrame_background.get_rect()
                                                                           
            
            while not self.done: 
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.done=True #true or false value
                    #elif event.type == pygame.MOUSEBUTTONDOWN:
                       # print("wil play sound")
                        #click_sound.play()
                                                    
                self.screen.blit(zFrame_background, backgroundRect) 
                self.make_button(event, self.quiz.normalize(460, 'x'), self.quiz.normalize(0, 'y'), self.quiz.normalize(100, 'x'), self.quiz.normalize(840, 'y'), 1)
                self.make_button(event, self.quiz.normalize(0, 'x'), self.quiz.normalize(480, 'y'), self.quiz.normalize(71, 'x'), self.quiz.normalize(375, 'y'), 4)                            
                pygame.display.flip()
            
            pygame.quit()                                                           

run_app()