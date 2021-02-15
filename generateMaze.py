import random

def generateMaze(dimension, p):
    # initialize maze
    maze=[]

    for i in range(dimension): 
        # initialize col to set vals
        column = [] 
        for j in range(dimension): 
            # for each square check if random(0,1) is less than or equal to p
            if (random.uniform(0,1)<= p):
                # set square to blocked
                column.append(1)
            else:
                # set square to open
                column.append(0) 
        # append col to maze
        maze.append(column)

    # set start & goal to open  
    maze[0][0] = 0
    maze[dimension-1][dimension-1]=0

    return maze

def generateFireMaze(dimension, p):
    maze = generateMaze(dimension, p)
    x = 0
    y = 0
    while (x == 0 and y == 0) or (x == dimension-1 and y == dimension-1) or (maze[x][y] == 1):
        x = random.randint(0,dimension-1)
        y = random.randint(0,dimension-1)
    
    # print(x,y)
    maze[x][y] = 5
    # print(maze)
    return maze

# generateFireMaze(4,1)