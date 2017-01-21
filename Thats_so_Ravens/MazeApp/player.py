import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('MazeApp/mazeAssets/RodneytheRaven.png'), (size, size))
        self.lives = 3
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image, 20)
        self.alive = True

    def move(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def kill(self):
        self.lives -= 1
        self.alive = False

    def is_dead(self):
        if self.lives == 0:
            return True
        else:
            return False