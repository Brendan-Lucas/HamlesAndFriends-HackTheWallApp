import pygame
import time
import thread
pygame.init()

class Timer:
    black=(0,0,0)
    white=(255,255,255)
    def __init__(self,clockFace,display,centerPosX,centerPosY):
        #an "image" directory should be passed for clockFace
        self.font = pygame.font.SysFont('Calibri', 35, True, False)
        self.clockFace = pygame.transform.scale(pygame.image.load(clockFace).convert(), (50,50))
        self.endTime = ''
        self.startTime = ''
        self.currentTime = ''
        self.display = display
        self.centerPos = (centerPosX,centerPosY)
        self.lock = thread.allocate_lock()
        self.running = False


    def runTimer(self, startTime, endTime):
        self.startTime = startTime
        self.endTime = endTime
        self.currentTime = self.startTime
        self.running = True
        while self.currentTime != self.endTime and self.running:
            self.lock.acquire()
            time.sleep(1)
            if self.startTime < self.endTime:
                self.currentTime += 1
                print(self.currentTime)
            else:
                self.currentTime -=1
            self.lock.release()
        self.running = False

    def printTime(self):
        fontValue = ''
        if self.currentTime<60: fontValue += '0:'
        if self.currentTime<10: fontValue += '0'
        fontValue += str(self.currentTime)
        timeValue = self.font.render(fontValue, True, black)
        self.display.fill(white)
        self.display.blit(timeValue, self.centerPos)
        # self.display.blit(self.clockFace,self.centerPos)

    def synchronizedPrintTime(self):
        while (self.running):
            self.lock.acquire()
            self.printTime()
            self.lock.release()

def TestRunning():
    black=(0,0,0)
    white=(255,255,255)
    size = [560,840]
    screen = pygame.display.set_mode(size)
    screen.fill(white)
    pygame.display.flip()
    timer = Timer('quizAssets/ImagesForQuizApp/Button_purple.png', screen, 100, 100)
    going = True
    thread.start_new_thread(timer.runTimer, (20, 0))
    thread.start_new_thread(timer.synchronizedPrintTime, ())
    while going:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                going = False
                timer.running = False
        pygame.display.flip()

    timer.lock.acquire()
    pygame.quit()
