import pygame
from labyrinth import Labyrinth
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
		self.floorImage = []
		self.wallImage = []
		self.queue = []
		lab = Labyrinth()
		lab.make_labyrinth()
		self.array = lab.get_grid()
		self.load_wall_images()

	def make_tile(self, coordinates, backImage, frontImage):
		self.floors.append(Floor(coordinates, backImage))
		wall = Wall(coordinates, frontImage)
		self.walls.append(wall)
		return wall

	def load_wall_images(self):
		for i in range (0,9):
			self.wallImage.append((pygame.transform.rotate(pygame.image.load('mazeAssets/walls/Lines' + str(i) + '.png'), -90)))
			self.floorImage.append(pygame.image.load('mazeAssets/orange.png'))

	def draw_tiles(self):
		for floor in self.floors:
			self.background.blit(floor.image, floor.rect)
		for wall in self.walls:
			self.background.blit(wall.image, wall.rect)

	def draw_rodney(self):
		self.screen.blit(self.player.image, self.player.rect)
		
	def collision(self, wall):
		if pygame.sprite.collide_mask(self.player, wall):
			return True
	def depricollision(self):
		for wall in self.walls:
			if pygame.sprite.collide_mask(self.player, wall):
				return True			
	
	#def collisions(self, wall):
		#while self.player.rect.colliderect(self.wall.rect): 
			#if self.collision(wall):
				#return True
		#if wall.next:
			#self.collisions(wall.next)
		#return
	
	def collisions(self, wall):
		if self.player.rect.colliderect(wall.rect):
			if self.collision(wall):
				print 'mysquare'
				return True
		elif wall.next and self.player.rect.colliderect(wall.next.rect):
			self.player.wall = wall.next
			self.collision(wall.next)
			print 'nextsquare'
			return
		elif wall.prev and self.player.rect.colliderect(wall.prev.rect):
			self.player.wall = wall.prev
			self.collision(wall.prev)
			print 'prevsquare'
			return
		
	def make_tile_from_array_location(self, x, y, number, prev):
		wall = self.make_tile((x*40,y*40), self.floorImage[abs(number)], self.wallImage[abs(number)])
		wall.prev = prev
		
	def tiles_from_queue(self):
		tile = None
		for number, x, y in self.queue:
			if tile:
				tile.next = self.make_tile_from_array_location(x, y, number, tile)
				tile = tile.next
			else:
				tile = self.make_tile_from_array_location(x, y, number, tile)

	def make_number_array(self):
		x = 0
		y = 0
		number = 7
		while 0 <= x <len(self.array) and 0 <= len(self.array[0]) and number != 8:
			number = self.array[y][x]
			self.queue.append([number, x, y])
			if number in (1, -3, 4):
				x -= 1
			elif number in (2, 3, 6, 7):
				y += 1
			elif number in (-1, 5, -6):
				x += 1
			elif number in (-2, -4, -5):
				y-= 1

class Wall(pygame.sprite.Sprite):
	def __init__(self, coordinates, image):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.transform.scale(image, (40, 40))
		self.rect = self.image.get_rect().move(coordinates)
		self.mask = pygame.mask.from_surface(self.image, 20)
		self.next = ''
		self.prev = ''
		
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
		self.image = pygame.transform.scale(pygame.image.load('mazeAssets/RodneytheRaven.png'), (15, 15))
		self.lives = 3
		self.rect = self.image.get_rect()
		self.mask = pygame.mask.from_surface(self.image, 20)
		self.wall = ''

	def move(self, x, y):
		self.rect.x = x
		self.rect.y = y

	def kill(self):
		self.lives -= 1

	def is_dead(self):
		if self.lives == 0:
			return True
		else:
			return False

maze = Maze((560, 840))
maze.make_number_array()
maze.tiles_from_queue()
maze.player.wall = maze.walls[0]

maze.draw_tiles()

going = True
pygame.mouse.set_visible(False)
pygame.mouse.set_pos(20,10)
while going:
	maze.clock.tick(30)
	for event in pygame.event.get():
		pygame.display.flip()
		mouse_position = pygame.mouse.get_pos()
		maze.player.move(mouse_position[0], mouse_position[1])		
		maze.screen.blit(maze.background,maze.background.get_rect())
		maze.draw_rodney()		
		if event.type == pygame.QUIT:
			going = False
		#if maze.depricollisions(maze.player.wall) == 'done':
			#going = False
			#print'You win'
		elif maze.depricollision():
			maze.player.kill()
			if maze.player.is_dead():
				print 'You are dead'
		pygame.display.flip()