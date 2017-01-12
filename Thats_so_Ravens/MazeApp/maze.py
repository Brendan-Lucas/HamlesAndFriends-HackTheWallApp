import pygame
import Thats_so_Ravens.Helpers as helpers
from labyrinth import Labyrinth
from player import Player
from wall import Wall
from floor import Floor
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
        self.size = size
        self.tile_size = min(size[0]/dimensions[0], size[1]/dimensions[1])
        self.player = Player(self.tile_size/3)
        self.walls = []
        self.floors = []
        self.screen = pygame.display.set_mode(size)
        self.background = pygame.transform.scale(pygame.image.load('MazeApp/mazeAssets/white.png'), (self.screen.get_size()[0], self.screen.get_size()[1]))
        self.clock = pygame.time.Clock()
        self.floorImage = []
        self.wallImage = []
        self.load_life_images()

        self.tile_setup(dimensions)

    def load_life_images(self):
        self.life_images = []
        for i in range(1, 4):
            image = pygame.transform.scale(pygame.image.load("MazeApp/mazeAssets/lives_" + str(i) + ".png"), (helpers.normalize(self.size, 120, 'x'), helpers.normalize(self.size, 40, 'y')))
            self.life_images.append(image)

    def print_lives(self):
        lives = self.player.lives - 1
        self.screen.blit(self.life_images[lives], (helpers.normalize(self.size, 430, 'x'), helpers.normalize(self.size, 10, 'y')))

    def get_grid_from_labyrinth(self, dimensions):
        lab = Labyrinth(dimensions)
        lab.make_labyrinth()
        return lab.get_grid()

    def tile_setup(self, dimensions):
        array = self.get_grid_from_labyrinth(dimensions)
        self.load_wall_images()
        self.init_floors_and_walls(array)
        self.two_d_tiles(array)

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

    def init_floors_and_walls(self, array):
        for i in range(0, len(array)):
            self.walls.append([])
            self.floors.append([])
            for j in range(0, len(array[0])):
                self.walls[i].append(0)
                self.floors[i].append(0)

    def two_d_tiles(self, array):
        for x in range(0, len(array)):
            for y in range(0, len(array[0])):
                number = array[x][y]
                tile = self.make_wall_from_array_location(x, y, number)
                self.walls[x][y] = tile[0]
                self.floors[x][y] = tile[1]

    def load_wall_images(self):
        for i in range(0, 9):
            self.wallImage.append(pygame.image.load('MazeApp/mazeAssets/walls/Wall' + str(i) + '.png'))
            self.floorImage.append(pygame.image.load('MazeApp/mazeAssets/floors/Floor' + str(i) + '.png'))

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
        self.draw_tiles()

        self.player.alive = True
        pygame.mouse.set_visible(False)
        while not (back or done or timeout):
            # while not maze.player.is_dead() and maze.player.alive:
            self.clock.tick(60)
            self.player.alive = True
            if not self.player.is_dead():
                pygame.time.wait(1000)
                pygame.mouse.set_pos(self.tile_size/2, self.tile_size/4)
            while not (self.player.is_dead() or done) and self.player.alive:
                for event in pygame.event.get():
                    mouse_position = pygame.mouse.get_pos()
                    self.player.move(mouse_position[0], mouse_position[1])
                    self.screen.blit(self.background, self.background.get_rect())
                    self.draw_rodney()
                    if self.player.rect.x / self.tile_size == (len(self.floors) - 1) and self.player.rect.y / self.tile_size == (len(self.floors[0]) - 1):
                        done = True
                    if self.player.rect.x / self.tile_size == 0 and self.player.rect.y / self.tile_size == 0 and event.type == pygame.MOUSEBUTTONDOWN:
                        done = True
                        break
                    if event.type == pygame.QUIT:
                        done = True
                        break
                    if self.collision() == 'dead':
                        done = True
                        break
                    self.print_lives()
                    pygame.display.flip()
        pygame.mouse.set_visible(True)
        if done:
            return done
        elif back:
            return done
        else:
            return done





# maze = Maze((560, 840), (10,15))
# maze.run_screen()
