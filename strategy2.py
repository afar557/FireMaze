from collections import deque
from advancefire import advance_fire_one_step
import random
from bfs import bfs

maze = [[0,0,5],
        [0,0,5],
        [0,0,0]]

def bfsPath(maze, start, finish):
    width = len(maze[0])
    height = len(maze)
    queue = deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if x == finish[0] and y == finish[1]:
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)): # explore all neighbors up, down, right, left
            if 0 <= x2 < width and 0 <= y2 < height and (x2, y2) not in seen and maze[x2][y2] == 0: # check if neighbors are in bounds and not visited
                queue.append(path + [(x2, y2)]) # add neighbors and its path to the fringe
                seen.add((x2, y2))
    return None

def bfsStrat2(maze, start, finish, q):
    # count = 1
    # print(start)
    maze[start[0]][start[1]] = 2
    while start != finish:
        path = bfsPath(maze, start, finish)
        # print(path)
        if path != None:
            start = path[1]
            # print(start)
            maze[start[0]][start[1]] = 2
            maze = advance_fire_one_step(maze, q)
            # count += 1
        else:
            print("Goal Unreachable")
            return maze
    # print(maze)
    return maze

# bfs(maze, (0,0), (2,2))
# bfsStrat2(maze, (0,0), (2,2), 0.2)