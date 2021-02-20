from collections import deque
import random
import sys

sys.path.append("..")

from advancefire import advance_fire_one_step


# Function that executes the BFS algorithm for Strategy 1 and returns the maze with the path
def bfsStrat1(maze, start, finish, q):
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

        # If the popped index is the finish index, meaning you have found the shortest path
        if x == finish[0] and y == finish[1]:
            # Mark the path and return the maze
            for position in path:
                maze = advance_fire_one_step(maze, q)

                # If you encounter a fire, return
                if maze[position[0]][position[1]] == 5:
                    print("Ran into fire oops :P")
                    return maze
                
                # Mark the path on the maze
                maze[position[0]][position[1]] = 2
            return maze
        
        # Explore all 4 neighbors of the current cell: up, down, right and left
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            # If the coordinates are in bounds and the neighbor cell is open
            if 0 <= x2 < width and 0 <= y2 < height and (x2, y2) not in seen and maze[x2][y2] != 1:             
                # Add neighbors and its path to the fringe
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
    print("Goal unreachable")
    return maze
