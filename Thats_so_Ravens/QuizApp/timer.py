import pygame
import time
pygame.init()

class timer:
    def __init__(self,clockFace,endTime,startTime,display,centerPosX,centerPosY):
        #a surface obj should be passed for clockFace
        self.clockFace = clockFace
        self.endTime = endTime
        self.startTime = startTime 
        self.currentTime = seconds
        self.display = display
        self.centerPos = (centerPosX,centerPosY)
        self.font = pygame.font.SysFont('Calibri', 35, True, False)
        self.disp = pygame.Surface([width,length])
        
        seconds= self.startTime
        while seconds != value:
            self.disp.fill(black)
            time.sleep(1)      
            fontValue = ''
            if seconds<60: fontValue += '0:'
            if seconds<10: fontValue += '0'
            fontValue += str(seconds)
            timeValue = font.render(fontValue,True,white)  
            self.disp.blit(timeValue,[(width/4),(length/2)])
            self.display.blit(self.disp,[x,y])
            pygame.display.flip()
            if self.startTime < self.endTime:
                seconds += 1
            else:
                seconds -=1
            
    
    
    
black=(0,0,0)
white=(255,255,255)

size = [560,840] 
screen = pygame.display.set_mode(size)
going = True
while going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            going = False
        screen.fill(white)
        print("i get here")
        
        print("fuck you")
        pygame.display.flip()

pygame.quit()
    

    
    