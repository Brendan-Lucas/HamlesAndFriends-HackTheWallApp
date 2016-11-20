import pygame
from tunnels import Fuckload

class Tile(pygame.sprite.Sprite):
               def __init__(self, color, width, height):
                              pygame.sprite.Sprite.__init__(self)
                              self.image = pygame.Surface([width,height])
                              self.image.fill(color)
                              self.rect = self.image.get_rect()
                              
                              
class Rodney(pygame.sprite.Sprite):
               def __init__(self):
                              pygame.sprite.Sprite.__init__(self)
                              self.image = pygame.image.load("mazeAssets/RodneySmall.jpg").convert()
                              self.image.set_colorkey(white)
                              self.rect = self.image.get_rect()
                              
array = [[3,0,0,0,0,0,0,0], [3,0,0,0,0,0,0,0], [7,2,5,0,8,2,2,5], [8,2,6,0,3,0,0,4], [3,0,0,0,3,0,0,4], [7,2,2,2,6,0,0,4], [0,0,0,0,0,0,0,4], [0,8,1,1,5,0,0,4], [10,6,0,0,7,1,1,6]]
                              
pygame.init()

black=(0,0,0)
white=(255,255,255)
gold =(255,215,0)
width = 60
height = 60
size = [560,840] 
screen = pygame.display.set_mode(size)

tile_list = pygame.sprite.Group()

#Tile 1

tileUp= Tile(white,width,height)
pygame.draw.line(tileUp.image,black,[0,0],[0,height],10)
pygame.draw.line(tileUp.image,black,[width-1,0],[width-1,height],10)
tile_list.add(tileUp)


#tile 2
tileSide=Tile(white,width,height)
pygame.draw.line(tileSide.image,black,[0,0],[width-1,0],10)
pygame.draw.line(tileSide.image,black,[0,height],[width-1,height],10)
tile_list.add(tileSide)


#tile 3
tileBotLeft= Tile(white,width,height)
pygame.draw.line(tileBotLeft.image,black,[0,0],[0,height],10)
pygame.draw.line(tileBotLeft.image,black,[0,height],[width-1,height],10)
tile_list.add(tileBotLeft)


#tile 4
tileBotRight= Tile(white,width,height)
pygame.draw.line(tileBotRight.image,black,[0,height],[width-1,height],10)
pygame.draw.line(tileBotRight.image,black,[width-1,height],[width-1,0],10)
tile_list.add(tileBotRight)


#tile 5
tileTopRight= Tile(white,width,height)
pygame.draw.line(tileTopRight.image,black,[0,0],[width-1,0],10)
pygame.draw.line(tileTopRight.image,black,[width-1,0],[width-1,height],10)
tile_list.add(tileTopRight)


#tile 6
tileTopLeft= Tile(white,width,height)
pygame.draw.line(tileTopLeft.image,black,[0,0],[width-1,0],10)
pygame.draw.line(tileTopLeft.image,black,[0,0],[0,height],10)
tile_list.add(tileTopLeft)



#tile 7
tileBlank = Tile(black,width,height)
tile_list.add(tileBlank)

#win tile
tileWin = Tile(gold,width,height)


# Rodney
rodney = Rodney()



going = True
clock = pygame.time.Clock()

lives = 3

pygame.mouse.set_visible(False)
while going:
               pygame.mouse.set_pos(20,10)
               alive = True
               while alive:
                              clock.tick(30)
                              for event in pygame.event.get():
                                             if event.type == pygame.QUIT:
                                                            going = False
                                                            
                             
                                             RodPos = pygame.mouse.get_pos()
                                             x = RodPos[0]
                                             y = RodPos[1]
                                             screen.fill(white)
                                             def rodneyhitsblack(x,y):
                                                            if 1 < x < 546 and 1 < y < 819:
                                                                           for i in (0,20):
                                                                                          if screen.get_at((x-1, y+i))==black or screen.get_at((x+13, y+i))==black:
                                                                                                         return True
                                                                           for i in (0,13): 
                                                                                          if screen.get_at((x+i, y-1))==black or screen.get_at((x+i, y+20))==black:
                                                                                                         return True
                                                            return False
                                                            
                                             
                                             #def rodneyhitsblack(x,y):
                                                            #if 1 < x < 546 and 1 < y < 819:
                                                                           #for i in (0,20):
                                                                                          #if screen.get_at((x-1, y+i))==gold or screen.get_at((x+13, y+i))==gold:
                                                                                                         #return True
                                                                           #for i in (0,13): 
                                                                                          #if screen.get_at((x+i, y-1))==gold or screen.get_at((x+i, y+20))==gold:
                                                                                                         #return True
                                                            #return False                                             
                                             
                                             
                                             for i in range(0, len(array)):
                                                            for j in range(0, len(array[i])):
                                                                           if array[i][j] == 0:
                                                                                          screen.blit(tileBlank.image,[40*i,40*j])
                                                                           elif array[i][j] == 1 or array[i][j] == 2:
                                                                                          screen.blit(tileUp.image,[40*i,40*j])
                                                                           elif array[i][j] == 3 or array[i][j] == 4:
                                                                                          screen.blit(tileSide.image,[40*i,40*j])
                                                                           elif array[i][j] == 5:
                                                                                          screen.blit(tileBotLeft.image,[40*i,40*j])
                                                                           elif array[i][j] == 6:
                                                                                          screen.blit(tileBotRight.image,[40*i,40*j])
                                                                           elif array[i][j] == 7:
                                                                                          screen.blit(tileTopRight.image,[40*i,40*j])
                                                                           elif array[i][j] == 8:
                                                                                          screen.blit(tileTopLeft.image,[40*i,40*j])
                                                                           elif array[i][j] == 10:
                                                                                          screen.blit(tileWin.image,[40*i,40*j])
                                                            
                                                                           
                                                                                          
                                             
                                             
                                             
                                             
                                             
                                             if rodneyhitsblack(x,y):
                                                            alive = False
                                                            tempx = x
                                                            tempy = y
                                                            RodPos = [tempx,tempy]
                                                            lives = lives -1                                                           
                                                            clk = False
                                                            while clk == False:
                                                                           for click in pygame.event.get():
                                                                                          if click.type == pygame.MOUSEBUTTONDOWN:
                                                                                                         clk = True
                                                            if lives == 0:
                                                                           going =False
                                             #if rodneygetsgold(x,y):
                                                            
                                             
                                             screen.blit(rodney.image,[x,y])
                                             pygame.display.flip()
pygame.quit()
                        
#screen.blit(tileUp.image,[0,0])