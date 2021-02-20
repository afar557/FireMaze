from collections import deque
import random
import sys


sys.path.append("..")
from advancefire import advance_fire_one_step
from bfs import bfs

# Function that executes the BFS algorithm and returns the maze with the path
def bfsPath(maze, start, finish):
    # Variables used to store the dimensions of the maze
    width = len(maze[0])
    height = len(maze)

    # Create a queue and add the start index into the queue
    queue = deque([[start]])

    # Create a visited set and add the start index
    seen = set([start])

    while queue:
        # Pop an index from the queue
        path = queue.popleft()
        x, y = path[-1]

        # If the popped index is the finish index, meaning you have found the shortest path return that path
        if x == finish[0] and y == finish[1]:
            return path
        
        # Explore all 4 neighbors of the current cell: up, down, right and left
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            # If the coordinates are in bounds and the neighbor cell is open
            if 0 <= x2 < width and 0 <= y2 < height and (x2, y2) not in seen and maze[x2][y2] == 0:
                # Add neighbors and its path to the fringe
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
    return None

# Function that executes the BFS algorithm for Strategy 2 and returns the maze with the path
def bfsStrat2(maze, start, finish, q):
    maze[start[0]][start[1]] = 2

    # Keep going while you have not reached the finish index
    while start != finish:
        # Run the BFS algorithm to get the next step in the path from the current index to finish
        path = bfsPath(maze, start, finish)

        # If a path is found
        if path != None:
            # Set the current index to the first index in the path
            start = path[1]

            # Mark the step on the maze as a path
            maze[start[0]][start[1]] = 2

            # Advance the fire
            maze = advance_fire_one_step(maze, q)
        
        else:
            print("Goal Unreachable")
            return maze
    # print(maze)
    print("Success!")
    return maze

# bfs(maze, (0,0), (2,2))
# bfsStrat2(maze, (0,0), (2,2), 0.2)
