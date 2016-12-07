import pygame

class Floor():
    def __init__(self, coordinates, image, tile_size):
        self.tile_size = tile_size
        self.image = pygame.transform.scale(image, (self.tile_size, self.tile_size))
        self.rect = self.image.get_rect().move(coordinates)

    def move(self, x, y):
        self.rect.move(x, y)
