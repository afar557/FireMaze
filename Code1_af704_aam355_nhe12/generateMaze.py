import random

# Function that generates the maze
def generateMaze(dimension, p):
    # Initialize maze
    maze=[]

    for i in range(dimension): 
        # Initialize col to set vals
        column = [] 

        for j in range(dimension): 
            # For each square check if random(0,1) is less than or equal to p
            if (random.uniform(0,1)<= p):
                # Set square to blocked
                column.append(1)

            else:
                # Set square to open
                column.append(0)

        # Append col to maze
        maze.append(column)

    # Set start & goal to open & return maze  
    maze[0][0] = 0
    maze[dimension-1][dimension-1]=0
    return maze

# Function that generates a fire maze
def generateFireMaze(dimension, p):
    # Initialize maze
    maze = generateMaze(dimension, p)

    x = 0
    y = 0
    while (x == 0 and y == 0) or (x == dimension-1 and y == dimension-1) or (maze[x][y] == 1):
        x = random.randint(0,dimension-1)
        y = random.randint(0,dimension-1)
    
    maze[x][y] = 5
    return maze