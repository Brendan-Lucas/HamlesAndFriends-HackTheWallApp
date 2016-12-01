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
		self.walls = []
		self.floors = []
		self.screen = pygame.display.set_mode(size)
		self.background = pygame.transform.scale(pygame.image.load('mazeAssets/white.png'), (self.screen.get_size()[0], self.screen.get_size()[1]))
		self.clock = pygame.time.Clock()

	def make_tile(self, coordinates, backImage, frontImage):
		self.floors.append(Floor(coordinates, backImage))
		self.walls.append(Wall(coordinates, frontImage))

	def draw_tiles(self):
		for floor in self.floors:
			self.background.blit(floor.image, floor.rect)
		for wall in self.walls:
			self.background.blit(wall.image, wall.rect)

	def collision(self):
		for wall in self.walls:
			if pygame.sprite.collide_mask(self.player, wall):
				return True
		return False

	def draw_rodney(self):
		self.screen.blit(self.player.image, self.player.rect)



class Wall(pygame.sprite.Sprite):
	def __init__(self, coordinates, image):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.transform.scale(image, (40, 40))
		self.rect = self.image.get_rect().move(coordinates)
		self.mask = pygame.mask.from_surface(self.image, 20)

	def move(self, x, y):
		self.rect.move(x, y)

class Floor():
	def __init__(self, coordinates, image):
		self.image = pygame.transform.scale(image, (40,40))
		self.rect = self.image.get_rect().move(coordinates)
	
	def move(self, x, y):
		self.rect.move(x,y)

class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.transform.scale(pygame.image.load('mazeAssets/RodneytheRaven.png'), (40, 40))
		self.lives = 3
		self.rect = self.image.get_rect()
		self.mask = pygame.mask.from_surface(self.image, 20)

	def move(self, x, y):
		self.rect = (x, y)

	def kill(self):
		self.lives -= 1

	def is_dead(self):
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
		pygame.display.flip()
		mouse_position = pygame.mouse.get_pos()
		maze.player.move(mouse_position[0], mouse_position[1])
		maze.draw_tiles()		
		maze.screen.blit(maze.background,maze.background.get_rect())
		maze.draw_rodney()		
		if event.type == pygame.QUIT:
			going = False
			break		
		if maze.collision():
			maze.player.kill()
		if maze.player.is_dead():
			print 'You are dead'
		pygame.display.flip()