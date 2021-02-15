from collections import deque
from advancefire import advance_fire_one_step
import random

maze = [[0,0,5],
        [0,0,0],
        [0,0,0]]

def bfsStrat1(maze, start, finish, q):
    width = len(maze[0])
    height = len(maze)
    queue = deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if x == finish[0] and y == finish[1]:
            for position in path:
                maze = advance_fire_one_step(maze, q)
                if maze[position[0]][position[1]] == 5:
                    print("Ran into fire oops :P")
                    return maze
                maze[position[0]][position[1]] = 2 # mark the shortest path to finish in the maze as 2
            # print(maze)
            return maze
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)): # explore all neighbors up, down, right, left
            if 0 <= x2 < width and 0 <= y2 < height and (x2, y2) not in seen and maze[x2][y2] != 1: # check if neighbors are in bounds and not visited and not blocked                
                queue.append(path + [(x2, y2)]) # add neighbors and its path to the fringe
                seen.add((x2, y2))
    print("Goal unreachable")
    return maze

# bfsStrat1(maze, (0,0), (2,2), .5)