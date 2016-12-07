import pygame
import threading
from labyrinth import Labyrinth
pygame.init()

BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (0, 255,   0)
RED = (255,   0,   0)
BLUE = (0,   0, 255)

# class Collider(threading.Thread):
#     def __init__(self, maze):
#         super(Collider, self).__init__()
#         self.maze = maze
#         self.current = maze.walls[0]
#
#     def run(self):
#         while not self.maze.player.is_dead():
#             self.collision()
#         print 'rodney is dead'


class Maze():
    def __init__(self, size, dimensions):
        self.tile_size = min(size[0]/dimensions[0], size[1]/dimensions[1])
        self.player = Player(self.tile_size/3)
        self.walls = []
        self.floors = []
        self.screen = pygame.display.set_mode(size)
        self.background = pygame.transform.scale(pygame.image.load('mazeAssets/white.png'), (self.screen.get_size()[0], self.screen.get_size()[1]))
        self.clock = pygame.time.Clock()
        self.floorImage = []
        self.wallImage = []
        lab = Labyrinth(dimensions)
        lab.make_labyrinth()
        self.array = lab.get_grid()
        self.load_wall_images()
        self.init_floors_and_walls()
        self.two_d_tiles()


    def collision(self):
        x_coords = [self.player.rect.x / self.tile_size]
        y_coords = [self.player.rect.y / self.tile_size]
        # checking the squares around it as well
        if x_coords < len(self.floors)-1:
            x_coords.append(x_coords[0]+1)
        if x_coords > 0:
            x_coords.append(x_coords[0] - 1)
        if y_coords < len(self.floors)-1:
            y_coords.append(x_coords[0] + 1)
        if y_coords > 0:
            x_coords.append(x_coords[0] - 1)
        for x in x_coords:
            for y in y_coords:
                if pygame.sprite.collide_mask(self.player, self.walls[x][y]):
                    print 'kill rod'
                    self.player.kill()
                    if self.player.is_dead():
                        return 'dead'

    def init_floors_and_walls(self):
        for i in range(0, len(self.array)):
            self.walls.append([])
            self.floors.append([])
            for j in range(0, len(self.array[0])):
                self.walls[i].append(0)
                self.floors[i].append(0)

    def two_d_tiles(self):
        for x in range(0, len(self.array)):
            for y in range(0, len(self.array[0])):
                number = self.array[x][y]
                tile = self.make_wall_from_array_location(x, y, number)
                self.walls[x][y] = tile[0]
                self.floors[x][y] = tile[1]

    def load_wall_images(self):
        for i in range(0, 9):
            self.wallImage.append(pygame.image.load('mazeAssets/walls/Lines' + str(i) + '.png'))
            self.floorImage.append(pygame.image.load('mazeAssets/floors/Floor' + str(i) + '.png'))

    def draw_tiles(self):
        for x in range(0, len(self.floors)):
            for y in range(0, len(self.floors[0])):
                self.background.blit(self.floors[x][y].image, self.floors[x][y].rect)
                self.background.blit(self.walls[x][y].image, self.walls[x][y].rect)

    def draw_rodney(self):
        self.screen.blit(self.player.image, self.player.rect)
        
    def make_wall_from_array_location(self, x, y, number):
        tile = self.make_tile((x*self.tile_size, y*self.tile_size), self.floorImage[abs(number)], self.wallImage[abs(number)])
        wall = tile[0]
        floor = tile[1]
        return [wall, floor]

    def make_tile(self, coordinates, backImage, frontImage):
        floor = Floor(coordinates, backImage, self.tile_size)
        wall = Wall(coordinates, frontImage, self.tile_size)
        return [wall, floor]

    def run_screen(self):
        pygame.display.set_caption("Try and find your way to Architecture 5001 before your lab starts")

        timeout = False
        back = False
        done = False
        maze.draw_tiles()

        maze.player.alive = True
        pygame.mouse.set_visible(False)
        while not (back or done or timeout):
            # while not maze.player.is_dead() and maze.player.alive:
            maze.clock.tick(30)
            maze.player.alive = True
            if not maze.player.is_dead():
                pygame.time.wait(1000)
                pygame.mouse.set_pos(self.tile_size/2, self.tile_size/4)
            while not maze.player.is_dead() and maze.player.alive:
                for event in pygame.event.get():
                    mouse_position = pygame.mouse.get_pos()
                    maze.player.move(mouse_position[0], mouse_position[1])
                    maze.screen.blit(maze.background, maze.background.get_rect())
                    maze.draw_rodney()
                    if maze.player.rect.x / self.tile_size == (len(maze.floors) - 1) and maze.player.rect.y / self.tile_size == (len(maze.floors[0]) - 1):
                        done = True
                    if event.type == pygame.QUIT:
                        done = True
                    if maze.collision() == 'dead':
                        done = True
                    pygame.display.flip()
        pygame.mouse.set_visible(True)
        if done:
            return done
        elif back:
            return done
        else:
            return done



class Wall(pygame.sprite.Sprite):
    def __init__(self, coordinates, image, tile_size):
        pygame.sprite.Sprite.__init__(self)
        self.tile_size = tile_size
        self.image = pygame.transform.scale(image, (self.tile_size, self.tile_size))
        self.rect = self.image.get_rect().move(coordinates)
        self.mask = pygame.mask.from_surface(self.image, 20)

    def move(self, x, y):
        self.rect.move(x, y)


class Floor():
    def __init__(self, coordinates, image, tile_size):
        self.tile_size = tile_size
        self.image = pygame.transform.scale(image, (self.tile_size,self.tile_size))
        self.rect = self.image.get_rect().move(coordinates)
    
    def move(self, x, y):
        self.rect.move(x,y)


class Player(pygame.sprite.Sprite):
    def __init__(self, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('mazeAssets/RodneytheRaven.png'), (size, size))
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
            self.done = True
            return True
        else:
            return False


maze = Maze((560, 840), (10,15))
maze.run_screen()

