import pygame
import time
pygame.init()

class timer:
    def __init__(self,clockFace,display,centerPosX,centerPosY):
        #an "image" directory should be passed for clockFace
        self.font = pygame.font.SysFont('Calibri', 35, True, False)
        self.clockFace = pygame.image.load(clockFace).convert()
        self.endTime = '' 
        self.startTime = '' 
        self.currentTime = seconds
        self.display = display
        self.centerPos = (centerPosX,centerPosY)
        
        
    def runTimer(self, starTime, endTime):   
        seconds= self.startTime
        while seconds != self.endTime:
            time.sleep(1)      
            fontValue = ''
            if seconds<60: fontValue += '0:'
            if seconds<10: fontValue += '0'
            fontValue += str(seconds)
            timeValue = font.render(fontValue,True,white)  
            self.clockFace.blit(timeValue,[self.centerPos])
            self.display.blit(self.clockFace,[self.centerPos])
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
    

    
    