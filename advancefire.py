import random
from copy import copy, deepcopy

# Function that returns the maze after the fire advances one step
def advance_fire_one_step(maze, q):
    # Variables used to store the dimensions of the maze
    width = len(maze[0])
    height = len(maze)

    # Variable used to store the copy of the original maze
    newMaze = deepcopy(maze)

    # Explore every cell in the maze
    for x in range(len(maze)):
        for y in range(len(maze[x])):
            # If the current cell is neither on fire nor blocked
            if maze[x][y] != 5 and maze[x][y] != 1:

                # Set K to 0
                k = 0

                # Explore all 4 neighbors of the current cell: up, down, right and left
                for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                    # If the coordinates are in bounds and the neighbor cell is on fire
                    if 0 <= x2 < width and 0 <= y2 < height and maze[x2][y2] == 5:
                        # Increase K (the number of neighbors on fire) by 1
                        k += 1

                # Calculate the probability for the cell to be on fire 
                prob = 1-((1-q)**k)
                rand = random.uniform(0,1)

                if (rand <= prob):
                    # Mark the cell to be on fire
                    newMaze[x][y] = 5
    return newMaze