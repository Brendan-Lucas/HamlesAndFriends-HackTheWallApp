import pygame
import time
pygame.init()

class Timer:
    def __init__(self,clockFace,display,centerPosX,centerPosY):
        #an "image" directory should be passed for clockFace
        self.font = pygame.font.SysFont('Calibri', 35, True, False)
        self.clockFace = pygame.transform.scale(pygame.image.load(clockFace).convert(), (50,50))
        self.endTime = '' 
        self.startTime = '' 
        self.currentTime = ''
        self.display = display
        self.centerPos = (centerPosX,centerPosY)
        
        
    def runTimer(self, startTime, endTime):
        self.startTime = startTime   
        self.currentTime = self.startTime
        while self.currentTime != self.endTime:
            time.sleep(1)      
            if self.startTime < self.endTime:
                self.currentTime += 1
            else:
                self.currentTime -=1
            
    def printTime(self):
        fontValue = ''
        if self.currentTime<60: fontValue += '0:'
        if self.currentTime<10: fontValue += '0'
        fontValue += str(self.currentTime)
        timeValue = self.font.render(fontValue,True,black)  
        self.display.blit(timeValue,self.centerPos)
        # self.display.blit(self.clockFace,self.centerPos)
    
    
    
black=(0,0,0)
white=(255,255,255)

size = [560,840] 
screen = pygame.display.set_mode(size)
time = Timer('quizAssets/ImagesForQuizApp/Button_purple.png', screen, 100, 100)
time.runTimer(20,0)
going = True
while going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            going = False
        screen.fill(white)
        print("i get here")
        time.printTime()
        print("fuck you")

        pygame.display.flip()

pygame.quit()
    

    
    