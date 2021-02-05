import random
from copy import copy, deepcopy

maze = [[0,0,0],
        [5,0,0],
        [0,0,0]]
# is q randomly generated or is it a parameter?

def advance_fire_one_step(maze, q):
    width = len(maze[0])
    height = len(maze)
    newMaze = deepcopy(maze)
    for x in range(len(maze)):
        for y in range(len(maze[x])):
            if maze[x][y] != 5 and maze[x][y] != 1:
                k = 0
                for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)): # explore all neighbors up, down, right, left
                    if 0 <= x2 < width and 0 <= y2 < height and maze[x2][y2] == 5:
                        k += 1
                prob = 1-((1-q)**k)
                rand = random.uniform(0,1)
                if (rand <= prob):
                    newMaze[x][y] = 5
                    print(x,',',y)
    print(newMaze)
    return newMaze

advance_fire_one_step(maze, 1)

            
