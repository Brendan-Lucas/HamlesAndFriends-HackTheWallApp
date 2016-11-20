# Drax Lindgren
# Maze program
# Language Python 3.2
import random
import time

global grid
 
 #path going down/up left/right, and 4 corners sprites
#also same sprites


#PLOTSIZE = 20
#WIDTH = 500
#HEIGHT = 500



#make maze


grid = []
for i in range (0,10):
    grid.append([])
    for j in range (0,10):
        grid[i].append(0)
     
#instantiate and create the 25x25 grid with all 0
     
cursor = [0,0]
grid[0][0] = 1

#cursor for tracking path building


dvar = 0 #random gen from 1 to 5 to decide to go towards end goal
gvar = 0 #random gen from 1 to 4 to decide to go different directions, cant be backwards

win = False


def topcheck():
    if cursor[1] == 0 or cursor[0] ==len(grid) -1:
        return 9
    else:
        return grid[cursor[0]][cursor[1]-1]
 
def rightcheck():
    if cursor[0] == len(grid) - 1:
        return 9
    else:
        return grid[cursor[0] +1][cursor[1]]
    
def downcheck():
    if cursor[1] == len(grid) - 1:
        return 9
    else:
        return grid[cursor[0]][cursor[1]+1]
 
def leftcheck():
    if cursor[0] == 0 or cursor[1] == len(grid) -1:
        return 9
    else:
        return grid[cursor[0] -1][cursor[1]]    

def findMatch(direction):
    print(direction)
    print(cursor[0])
    print(cursor[1])
    if direction == 'top':
         if grid[cursor[0]][cursor[1]]  == 2:
             return 2
         elif grid[cursor[0]][cursor[1]]  == 3:
             return 6
         elif grid[cursor[0]][cursor[1]]  == 4:
             return 5
         else :
             return 'error,in topfindMatch'
    elif direction == 'right':
         if grid[cursor[0]][cursor[1]] == 3:
             return 3
         elif grid[cursor[0]][cursor[1]] == 1:
             return 5
         elif grid[cursor[0]][cursor[1]] == 2:
             return 8
         else:
             return 'error,in rightfindMatch'
    elif direction == 'down':
         if grid[cursor[0]][cursor[1]] == 1:
             return 1
         elif grid[cursor[0]][cursor[1]]  == 3:
             return 7
         elif grid[cursor[0]][cursor[1]]  == 4:
             return 8
         else:
             return 'error,in downfindMatch'  
    elif direction == 'left':
         if grid[cursor[0]][cursor[1]]  == 2:
             return 7
         elif grid[cursor[0]][cursor[1]]  == 4:
             return 4
         elif grid[cursor[0]][cursor[1]]  == 1:
             return 6
         else:
              return 'error,in leftfindMatch'  
    else:  
        return 'could not find direction'
    
   
#method checks for already set blocks and bounds and puts them in
def fillSpace(path):
    print(path)
    print(cursor[0])
    print(cursor[1])    
    #change value of block to matching type
    if path == 'top':
     if topcheck() == 0:
         grid[cursor[0]][cursor[1]] = findMatch('top')
         grid[cursor[0]][cursor[1] -1] = 2
         cursor[1] -= 1
     elif rightcheck() == 0:
         grid[cursor[0]][cursor[1]] = findMatch('right')
         grid[cursor[0]+1][cursor[1]] = 3
         cursor[0] += 1
     elif downcheck() == 0:
         grid[cursor[0]][cursor[1]] = findMatch('down')
         grid[cursor[0]][cursor[1]+1] = 1
         cursor[1] += 1
     elif leftcheck() == 0:
         grid[cursor[0]][cursor[1]] = findMatch('left')
         grid[cursor[0]-1][cursor[1]] = 4
         cursor[0] -= 1
     else:
         print('no spaces trying to go top')        
     
      
      
    elif path == 'right':
         if rightcheck() == 0:
              grid[cursor[0]][cursor[1]] = findMatch('right')
              grid[cursor[0]+1][cursor[1]] = 3
              cursor[0] += 1
         elif topcheck() == 0:
              grid[cursor[0]][cursor[1]] = findMatch('top')
              grid[cursor[0]][cursor[1] -1] = 2
              cursor[1] -= 1
         elif downcheck() == 0:
              grid[cursor[0]][cursor[1]] = findMatch('down')
              grid[cursor[0]][cursor[1]+1] = 1
              cursor[1] += 1
         elif leftcheck() == 0:
              grid[cursor[0]][cursor[1]] = findMatch('left')
              grid[cursor[0]-1][cursor[1]] = 4
              cursor[0] -= 1
         else:
             print ('no spaces trying to go right')
                  
        
    elif path == 'down':
         if downcheck() == 0:
              grid[cursor[0]][cursor[1]] = findMatch('down')
              grid[cursor[0]][cursor[1]+1] = 1
              cursor[1] += 1
         elif topcheck() == 0:
              grid[cursor[0]][cursor[1]] = findMatch('top')
              grid[cursor[0]][cursor[1] -1] = 2
              cursor[1] -= 1
         elif rightcheck() == 0:
              grid[cursor[0]][cursor[1]] = findMatch('right')
              grid[cursor[0]+1][cursor[1]] = 3
              cursor[0] += 1
         elif leftcheck() == 0:
              grid[cursor[0]][cursor[1]] = findMatch('left')
              grid[cursor[0]-1][cursor[1]] = 4
              cursor[0] -= 1
         else:
             print ('no spaces trying to go down')              
        
    elif path == 'left':
     if leftcheck() == 0:
         grid[cursor[0]][cursor[1]] = findMatch('left')
         grid[cursor[0]-1][cursor[1]] = 4
         cursor[0] -= 1
     elif downcheck() == 0:
         grid[cursor[0]][cursor[1]] = findMatch('down')
         grid[cursor[0]][cursor[1]+1] = 1
         cursor[1] += 1
     elif topcheck() == 0:
         grid[cursor[0]][cursor[1]] = findMatch('top')
         grid[cursor[0]][cursor[1] -1] = 2
         cursor[1] -= 1
     elif rightcheck() == 0:
         grid[cursor[0]][cursor[1]] = findMatch('right')
         grid[cursor[0]+1][cursor[1]] = 3
         cursor[0] += 1
     else:
         print ('no spaces trying to go left')         

while win != True:
    if cursor[0] == len(grid)-1 and cursor[1] == len(grid)-1:
        win = True
    dvar = random.randint(1,5)
    gvar = random.randint(1,4)
     
    #chance to make path influenced go towards end goal
    if dvar == 1:
     if grid[cursor[0]] > grid[cursor[1]]:  
         path = 'down'
     else: 
         path = 'right'
    else:
       #deciding direction for path 

     if gvar == 1:
         path = 'top'               
     if gvar == 2:
         path = 'right'                  
     if gvar == 3:
         path = 'down'               
     if gvar == 4:
         path = 'left'
   
    fillSpace(path)
    for i in range (0,10):
        print(grid[9-i])