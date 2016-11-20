import pygame
pygame.init()


BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

size = (560, 840)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Quiz App")

done = False



clock = pygame.time.Clock()
greenButton = pygame.image.load("quizAssets/ImagesForQuizApp/Button_greenAdjust.jpg")
greenButton.set_colokey(BLACK)
redButton = pygame.image.load("quizAssets/ImagesForQuizApp/Button_redAdjust.jpg")
redButton.set_colorkey(BLACK)
whiteButton = pygame.image.load("quizAssets/ImagesForQuizApp/Button_silverAdjust.jpg")
blueButton = pygame.image.load("quizAssets/ImagesForQuizApp/Button_purpleAdjust.jpg")

def makebutton(displayFrame, left, top, width, height, Answer):

    mouse = pygame.mouse.get_pos()
    
    
    
    if left+width > mouse[0] > left and top < mouse[1] < top+height:
        
        rect = displayFrame.blit(blueButton, [(left), (top)])       
        if event.type == pygame.MOUSEBUTTONDOWN:
            print 'button' + str(mouse)
    else:
        rect = displayFrame.blit(whiteButton, [(left), (top)])  

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
        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]
        if event.type == pygame.QUIT:
            done = True
        #elif event.type == p
        
        screen.blit(zFrame_background, backgroundRect)
        makebutton(screen, 60, 520, 220, 132, 'plop')
        makebutton(screen, 290, 520, 220, 132, 'plop')
        makebutton(screen, 60, 657, 220, 132, 'plop')
        makebutton(screen, 290, 657, 220, 132, 'plop')
        pygame.display.flip()
        
        clock.tick(60)

pygame.quit()