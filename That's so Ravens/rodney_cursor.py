Rodney = pygame.image.load("assets/Rodney.png").convert()
RodPos = pygame.mouse.get_pos()
x = RodPos[0]
y = RodPos[1]
white = (255,255,255)
screen.blit(Rodney[x,y])
Rodney.set_colorkey(white)