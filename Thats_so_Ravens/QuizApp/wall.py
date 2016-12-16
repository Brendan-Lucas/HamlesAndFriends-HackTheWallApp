import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, coordinates, image, tile_size):
        pygame.sprite.Sprite.__init__(self)
        self.tile_size = tile_size
        self.image = pygame.transform.scale(image, (self.tile_size, self.tile_size))
        self.rect = self.image.get_rect().move(coordinates)
        self.mask = pygame.mask.from_surface(self.image, 20)

    def move(self, x, y):
        self.rect.move(x, y)