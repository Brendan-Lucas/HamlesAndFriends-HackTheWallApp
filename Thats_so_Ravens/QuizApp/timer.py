import pygame
import time
import thread
pygame.init()

black=(0,0,0)
white=(255,255,255)

class Timer:

    black=(0,0,0)
    white=(255,255,255)

    def __init__(self, display, centerPosX, centerPosY, background=None):
        #an "image" directory should be passed for clockFace
        self.font = pygame.font.SysFont('Calibri', 35, True, False)
        self.clockFace = pygame.transform.scale(pygame.image.load(background).convert(), (83, 48))
        self.endTime = ''
        self.startTime = ''
        self.currentTime = ''
        self.display = display
        self.centerPosImage = (centerPosX-8, centerPosY-6)
        self.centerPos = (centerPosX, centerPosY)
        self.lock = thread.allocate_lock()
        self.running = False


    def timerCount(self, startTime, endTime):
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

    def printTime(self,):
        fontValue = ''
        if self.currentTime<60: fontValue += '0:'
        if self.currentTime<10: fontValue += '0'
        fontValue += str(self.currentTime)
        timeValue = self.font.render(fontValue, True, black)
        self.display.blit(self.clockFace, self.centerPosImage)
        self.display.blit(timeValue, self.centerPos)

    def synchronizedPrintTime(self):
        while (self.running):
            self.lock.acquire()
            self.printTime()
            self.lock.release()
            pygame.display.flip()

    def runTimer(self, start, end):
        self.running = True
        thread.start_new_thread(self.timerCount, (start, end))
        thread.start_new_thread(self.synchronizedPrintTime, ())

    def stop(self):
        self.running = False


def TestRunning():
    black=(0,0,0)
    white=(255,255,255)
    size = [560,840]
    screen = pygame.display.set_mode(size)
    screen.fill(white)
    pygame.display.flip()
    timer = Timer(screen, 100, 100)
    going = True
    timer.runTimer(20, 0)
    while going:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                going = False
                timer.running = False
        pygame.display.flip()

    timer.lock.acquire()
    pygame.quit()
