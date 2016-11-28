import pygame
from quiz import Quiz
import maze as mz
  
def run_app():
    GameStarter = Quad((540, 860))
    GameStarter.run_screen()        


class Quad:
        
        def __init__(self, size):
                self.block =0
                self.b_press=False
                self.done=False
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
                    self.done=mz.maze()
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
                self.make_button(event, 460, 0, 100, 840, 1)
                self.make_button(event, 0, 480, 71, 375, 4)                            
                pygame.display.flip()
            
            pygame.quit()                                                           

run_app()