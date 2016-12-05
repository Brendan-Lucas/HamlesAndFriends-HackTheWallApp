import random

#top = [0, (-1, 5, -6)]
#bottom = [1, (2, 1, -3, 4)]
#left = [2, (2, 3, 6)]
#right = [3, (-2, -5, -4)]
#direct = [top, bottom, left, right]
#Direction Top Bottom Left Right
#Top        0     1     4    -3
#Bottom     -1    0     5    -6
#Left       4     -5    0    -2
#Right      3     6     2     0
#inAndout = [[0, -1, -4, 3],[1, 0, -5, 6],[4, 5, 0, 2],[-3, -6, -2, 0]]  
#def find_tile(self, inp, outp):
    #for direction in direct:
        #if inp in direction[1]:
            #return direction[0] 

class Labyrinth():
    def __init__(self):
        self.grid = []
        self.cursor = [1,0]
        self.cursorStack = [[0,0]]
        self.done = False
        
        self.init_grid(12, 20)
        
    def make_labyrinth(self):  
        while not self.done:
            if not self.check():
                self.pop()
            else:
                self.fill(self.check())
                
    def pop(self):
        self.grid[self.cursor[0]][self.cursor[1]] = 9
        self.cursor[0] = self.cursorStack[-1][0]
        self.cursor[1] = self.cursorStack[-1][1]
        del self.cursorStack[-1]
        
        
    
    def move_cursor(self, direction):
        if direction == 'top':
            self.cursor[1] -= 1
        elif direction == 'right':
            self.cursor[0] += 1
        elif direction == 'down':
            self.cursor[1] += 1
        elif direction == 'left':
            self.cursor[0] -= 1
        else:
            print('error in move_cursor')        
                
    def fill(self, directionArray):
        dvar = random.randint(0,len(directionArray)-1)
        direction = directionArray[dvar]
        tileNumber = self.find_match(direction)
        self.grid[self.cursor[0]][self.cursor[1]] = tileNumber
        self.cursorStack.append([self.cursor[0], self.cursor[1]])
        self.move_cursor(direction)
            
    def find_match(self, direction):
        pingpong = self.grid[self.cursorStack[-1][0]][self.cursorStack[-1][1]]
        if direction == 'top':
            if pingpong in (1, 4, -3):
                return 1
            elif pingpong in (-2, -4, -5):
                return -3
            elif pingpong in (2, 3, 6):
                return 4
            else :
                return 'error,in topfindMatch'
        elif direction == 'right':
            if pingpong in (1, 4, -3):
                return 6
            elif pingpong in (-1, 5, -6):
                return 3
            elif pingpong in (2, 3, 6, 7):
                return 2
            else:
                return 'error,in rightfindMatch'
        elif direction == 'down':
            if pingpong in (-1, 5, -6):
                return -1
            elif pingpong in (-2, -4, -5):
                return -6
            elif pingpong in (2, 3, 6, 7):
                return 5
            else:
                return 'error,in downfindMatch'  
        elif direction == 'left':
            if pingpong in (1, 4, -3):
                return -5
            elif pingpong in (-1, 5, -6):
                return -4
            elif pingpong in (-2, -4, -5):
                return -2
            else:
                return 'error,in leftfindMatch'  
        else:  
            return 'could not find direction'      
    
    def check(self): 
        directionArray = []
        if self.cursor[1] != 0:
            if self.grid[self.cursor[0]][self.cursor[1]-1] == 0:
                directionArray.append('top')
            elif self.grid[self.cursor[0]][self.cursor[1]-1] == 8:
                self.done = True
                return ['top']
        if self.cursor[0] != len(self.grid) - 1:
            if self.grid[self.cursor[0]+1][self.cursor[1]] == 0:
                directionArray.append('right')
            elif self.grid[self.cursor[0]+1][self.cursor[1]] == 8:
                self.done = True
                return ['right']
        if self.cursor[1] != len(self.grid[0]) - 1:
            if self.grid[self.cursor[0]][self.cursor[1]+1] == 0:
                directionArray.append('down')
            elif self.grid[self.cursor[0]][self.cursor[1]+1] == 8:
                self.done = True
                return ['down']
        if self.cursor[0] != 0:
            if self.grid[self.cursor[0]-1][self.cursor[1]] == 0:
                directionArray.append('left')
            elif self.grid[self.cursor[0]-1][self.cursor[1]] == 8:
                self.done = True
                return ['left']
        if len(directionArray) > 0:
            return directionArray
        else:
            return False
        
        
    def get_grid(self):
        return self.grid
    
    
    def init_grid(self, width, length):
        self.grid = []
        for i in range (0,width):
            self.grid.append([])
            for j in range (0,length):
                self.grid[i].append(0) 
        self.grid[0][0] = 7
        self.grid[-1][-1] = 8
        