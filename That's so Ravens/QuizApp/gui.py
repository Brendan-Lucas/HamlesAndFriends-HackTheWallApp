import pygame
pygame.init()


BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

size = (600, 900)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Quiz App")

done = False

clock = pygame.time.Clock()


def makebutton(displayFrame, colour, left, top, width, height, Answer):

    mouse = pygame.mouse.get_pos()
    
    #blueButton = pygame.image.load("Button_purple.jpg").convert()
    #greenButton = pygame.image.load("ImagesForQuizApp/Button_green.png").convert()
    #redButton = pygame.image.load("ImagesForQuizApp/Button_red.png").convert()    
    whiteButton = pygame.image.load("quizAssets/ImagesForQuizApp/Button_silver.jpg")
    if left+width > mouse[0] > left and top < mouse[1] < top+height:

                
        if event.type == pygame.MOUSEBUTTONDOWN:
            print 'button' + str(mouse)
    else:
        rect = pygame.draw.rect(displayFrame, colour, (left, top, width, height))  

    X = left+(width/2)
    Y = top+(height/2)      


    TextFont = pygame.font.Font("freesansbold.ttf",20)
    #TextSurf, TextRect = text_objects(Answer,TextFont)
    #TextRect.cente = (X,Y)
    #gameDisplay.blit(TextSurf,TextRect)


zFrame_background = pygame.image.load("quizAssets\ImagesForQuizApp\QuizBackgroundAdjust.jpg")
backgroundRect=zFrame_background.get_rect()  

while not done:
    for event in pygame.event.get():
        whiteButton = pygame.image.load("quizAssets/ImagesForQuizApp/Button_silver.jpg")
        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]
        if event.type == pygame.QUIT:
            done = True
        #elif event.type == p
        
        
        screen.blit(zFrame_background, backgroundRect)
        makebutton(screen, WHITE, 100, 400, 300, 200, 'plop')
        
        pygame.display.flip()
        
        clock.tick(60)

pygame.quit()