import pygame
import Thats_so_Ravens.Helpers as helpers

pygame.init()

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

class Info:
#This is assuming a box size of 500*650
    def __init__(self, screen_size, background_image, info_text = None, info_image = None):
        self.calibri_35 = pygame.font.SysFont('Calibri',
                                              helpers.normalize(screen_size, 35, 'x'),
                                              True,
                                              False)
        self.background = pygame.transform.scale(pygame.image.load(background_image),
                                                 (helpers.normalize(screen_size, 500, 'x'), helpers.normalize(screen_size, 650, 'y')))
        self.start = [helpers.normalize(screen_size, 60, 'x'), helpers.normalize(screen_size, 150, 'y')]
        self.gap = helpers.normalize(screen_size, 32, 'y')
        self.image_size = [helpers.normalize(screen_size, 450, 'x'), helpers.normalize(screen_size, 450, 'y')]
        self.background.set_colorkey(WHITE)
        if info_text:
            self.info_text = helpers.split_question_print_text(info_text, [], self.calibri_35)
            if len(self.info_text)>3:
                self.image_size[0] = self.image_size[1] = (300 - (self.gap*(len(self.info_text)-2)))
        else:
            self.info_text = None
        if info_image:
            self.info_image = pygame.transform.scale(pygame.image.load("MazeApp/mazeAssets/" + info_image + ".png"), self.image_size)
            self.info_image.set_colorkey(WHITE)
        else:
            self.info_image = None

        self.draw()

######DO NOT NEED TO NORMALIZE THIS IS ALL RELATIVE TO THE INFO OBJECT
    def draw(self):
        if self.info_image and self.info_text:
            for i in range(0, len(self.info_text)):
                self.background.blit(self.info_text[i], [self.start[0], self.start[1] + self.gap * i])
            self.background.blit(self.info_image, ((500-self.image_size[0])/2, self.start[1] + len(self.info_text) * self.gap))
        elif self.info_image:
            self.background.blit(self.info_image, ((500-self.image_size[0])/2), self.start[1])
        elif self.info_text:
            for i in range(0, len(self.info_text)):
                self.background.blit(self.info_text[i], [self.start[0], self.start[1] + self.gap * i])
        else:
            "There is no text or image argument sent to info box"

    def get_surface(self):
        return self.background
