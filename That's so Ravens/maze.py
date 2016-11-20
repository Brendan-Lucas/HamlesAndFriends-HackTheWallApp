import pygame

class Tile(pygame.sprite.Sprite):
               def __init__(self, color, width, height):
                              pygame.sprite.Sprite.__init__(self)
                              self.image = pygame.Surface([width,height])
                              self.image.fill(color)
                              self.reck = self.image.get_rect()
                              
pygame.init()

black=(0,0,0)
white=(255,255,255)
width = 200
height = 200
size = [700,700]
screen = pygame.display.set_mode(size)

tile_list = pygame.sprite.Group()

#Tile 1

tile1= Tile(white,width,height)
pygame.draw.line(tile1.image,black,[0,0],[0,height],50)
pygame.draw.line(tile1.image,black,[0,0],[width-1,0],50)
tile_list.add(tile1)


going = True
clock = pygame.time.Clock()

while going:
               clock.tick(10)
               
               for event in pygame.event.get():
                              if event.type == pygame.QUIT:
                                             going = False
               screen.fill(white)
               pygame.Surface.blit(tile1.image,[100,100])
               
               
               ##maze tile 1 and 2
               #image1 = pygame.Surface([width,height])
               #image1.fill(white)
               #pygame.draw.line(image1,black,[0,0],[0,height])
               #pygame.draw.line(image1,black,[width,0],[width,height])

               pygame.display.flip()
pygame.quit()
                        
##maze tile 3 and 4
#image2 = pygame.Surface([width,height])
#image1.fill(white)
#pygame.draw.line(image2,color,[0,0],[width,0])
#pygame.draw.line(image2,color,[0,height],[width,height])

##maze tiel 5
#image3 = pygame.Surface([width,height])
#image1.fill(white)
#pygame.draw.lines(image3,color,[[0,0],[0,height],[width,height]])

##maze tile 6
#image4 = pygame.Surface([width,height])
#image1.fill(white)
#pygame.draw.lines(image4,color,[[width,0],[witdh,height],[0,height]])

##maze tile 7
#image5 = pygame.Surface([width,height])
#image1.fill(white)
#pygame.draw.lines(image5,color,[[0,0],[width,0],[width,length]])

##maze tile 8
#image6 = pygame.Surface([width,height])
#image1.fill(white)
#pygame.draw.lines(image6,color,[[width,0],[0,0],[0,length]])




#class Block(pygame.sprite.Sprite):
               #def __init__(self, color, width, height):
                       #super().__init__()
                       
                       #for event in pygame.event.get():
                               #if event.type == pygame.QUIT:
                                       #done == True