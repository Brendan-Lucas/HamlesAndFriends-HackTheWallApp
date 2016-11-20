import pygame

pygame.init()


def text_object(text, font):
   textsurface = font.reader(text, true, black)
   return textsurface, textsurface.get_rect()


def makebutton(displayFrame,colour, TLx,TLy,BRx,BRy, Answer,action):
   
   mouse = pygame.mouse.get_pos()
   click = pygame.mouse.get_clicked()
   
   for i in colour:
      if colour[i] > 50:
         light_colour = colour[i] - 50
   
   
   if TLx+BRx > mouse[0] > TLx and TLy+BRy > mouse[1] > TLy:
      rect = pygame.draw.rect(displayFrame,light_colour, (TLx,TLy,BRx,BRy))
      if click[0] ==1 and action != None:
         action()
         
   else:
      rect = pygame.draw.rect(displayFrame,colour, (TLx,TLy,BRx,BRy))
      
      
   X = TLx+(BRx/2)
   Y = TLy+(BRy/2)      
   
   
   TextFont = pygame.font.Font("freesansbold.ttf",20)
   TextSurf, TextRect = text_objects(Answer.get_text(),TextFont)
   TextRect.cente = (X,Y)
   gameDisplay.blit(TextSurf,TextRect)
   
   
   
   