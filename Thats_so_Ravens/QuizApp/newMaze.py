import pygame
pygame.init()

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

class Maze():
	def __init__(self, size):
		self.player = Player()
		self.tiles = []
		self.screen = pygame.display.set_mode(size)
		self.background = pygame.transform.scale(pygame.image.load('mazeAssets/white.png'), (self.screen.get_size()[0], self.screen.get_size()[1]))
		self.clock = pygame.time.Clock()

	def make_tile(self, coordinates, backImage, frontImage):
		self.tiles.append(Tile(coordinates, backImage, frontImage))

	def draw_tiles(self):
		for tile in self.tiles:
			tile.mask = pygame.mask.from_surface(tile.frontImage)
			self.background.blit(tile.backImage, tile.rect)
			self.background.blit(tile.frontImage, tile.rect)

	def collision(self):
		for tile in self.tiles:
			if pygame.sprite.collide_mask(self.player, tile):
				return True
		return False

	def draw_rodney(self):
		self.background.blit(self.player.image, self.player.rect)



class Tile(pygame.sprite.Sprite):
	def __init__(self, coordinates, backImage, frontImage):
		pygame.sprite.Sprite.__init__(self)
		self.backImage = pygame.transform.scale(backImage, (40, 40))
		self.backImage.set_colorkey(WHITE)
		self.frontImage = pygame.transform.scale(frontImage, (40, 40))
		self.frontImage.set_colorkey(WHITE)
		self.mask = pygame.mask.from_surface(frontImage)
		self.rect = self.frontImage.get_rect().move(coordinates)
		# self.rectBack = self.backImage.get_rect().move(coordinates)

	def move(self, x, y):
		self.rect.move(x, y)
		# self.rectBack.move(x, y)

class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.transform.scale(pygame.image.load('mazeAssets/RodneySmall.png'), (2, 2))
		self.image.set_colorkey(WHITE)
		self.mask = pygame.mask.from_surface(self.image)
		self.lives = 3
		self.rect = self.image.get_rect()

	def move(self, x, y):
		self.rect = (x, y)

	def kill(self):
		self.lives -= 1

	def is_rodney_dead(self):
		if self.lives == 0:
			return True
		else:
			return False

maze = Maze((560, 840))

orange = pygame.image.load('mazeAssets/orange.png')
twolines = pygame.image.load('mazeAssets/twolines.png')

maze.make_tile((280,420), orange, twolines)

going = True
pygame.mouse.set_visible(False)
pygame.mouse.set_pos(20,10)
while going:
	maze.clock.tick(30)
	for event in pygame.event.get():
		mouse_position = pygame.mouse.get_pos()
		maze.player.move(mouse_position[0], mouse_position[1])
		maze.draw_tiles()
		maze.draw_rodney()
		if event.type == pygame.QUIT:
			going = False
			break		
		if maze.collision():
			print 'collided'
		maze.screen.blit(maze.background,(0, 0))
		pygame.display.flip()