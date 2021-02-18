from queue import PriorityQueue
import math
from advancefire import advance_fire_one_step


maze = [[0,5,0],
        [0,0,0],
        [0,0,0]]
    
Maze3D = []

# getMazeWhen q = 1 (q, maze, timesteps)
# 3dMaze = [maze]
# for i in range(timesteps)
#   newMaze = advance_fire(3DMaze[-1])
#   3dMaze.append(newMaze)

def deterministicMaze(maze, timesteps):
    global Maze3D
    q = 1
    Maze3D = [maze]
    for i in range(timestops):
        newMaze = advance_fire_one_step(Maze3D[-1], q)
        Maze3D.append(newMaze)

# get Maze for 1 timestep when q = actual q
# newMaze = dimxdim of zeroes
# for x in range(10)
#   tempMaze = advance_fire(maze)
#   for i in range(len(newMaze))
#       for j in range(len(newMaze[0]))
#           if tempMaze[i][j] == 5
#               newMaze[i][j] += 5
# for i in range(len(newMaze))
#   for j in range(len(newMaze[0]))
#       if newMaze[i][j] != 1
#           newMaze[i][j] /= 10
def getProbMaze(maze, q):
    dim = len(maze[0])
    newMaze = [[0 for x in range(dim)] for y in range(dim)]
    for x in range(10):
        tempMaze = advance_fire_one_step(maze, q)
        for i in range(len(newMaze)):
            for j in range(len(newMaze)):
                if tempMaze[i][j] == 5:
                    newMaze[i][j] += 5
    for i in range(len(newMaze)):
        for j in range(len(newMaze)):
            if newMaze[i][j] != 1:
                newMaze[i][j] /= 10

# fucntuon that gets distance to fire
def disttoFire(maze, currentpos):
    mindist = len(maze)**2
    for i in range(len(maze)):
        for j in range(len(maze)):
            if maze[i][j] == 5 and manDist(currentpos, (i,j))<mindist:
                mindist = manDist(currentpos, (i,j))
    return mindist

# Man distance
def manDist(a,b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# # Function that returns the euclidean distance between two points on the maze
# def fireHeuristic(maze, q, currentPos):
#     sum = 0
#     for i in range(10):
#         tempMaze = advance_fire_one_step(maze, q)
#         if tempMaze[currentPos[0]][currentPos[1]] == 5:
#             sum+=1
#     return sum/10

def heuristic(a,b):
    return math.sqrt(((a[0]-b[0])**2) + ((a[1] - b[1])**2))
            
# Function that executes the A* algorithm and returns the maze with the path
def aStarF(maze, start, finish, q):
    global Maze3D

    # Create fringe using a priority queue
    fringe = PriorityQueue()

    # Add in the starting index (0,0) to the queue
    fringe.put((0, start))

    # Create a dictionary to store previously visited indices that you can use to trace a path
    prev= {}
    prev[start] = None

    # Create a dictionary to store the current distance traveresed
    currentDistance = {}
    currentDistance[start] = 0

    # Initialize x,y values to start
    x,y = start
    timestep = 0
    while not fringe.empty() and timestep<len(Maze3D):

        # Get the first index in the queue
        current = fringe.get()[1]

        # Increment timestep
        timestep+=1
        maze = Maze3D[timestep]

        # If you get to the finish index, break out of the loop
        if current == finish:
            break     
        
        # Set x,y to the current index
        x,y = current
        
        # Explore all 4 neighbors of the current cell: up, down, right and left
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            # If the coordinates are in bounds and the neighbor cell is open
            if 0 <= x2 < len(maze[0]) and 0 <= y2 < len(maze) and maze[x2][y2]==0:
                # Calculate the new distance from current cell to neighbor by adding 1
                newDistance = currentDistance[current] + 1

                # If the neighbor has not been previously visited or the new distance to the neighbor is less than the currently stored distance to the neighbor
                if (x2,y2) not in currentDistance or newDistance < currentDistance[(x2,y2)]:
                    # Update the current distance for the current neighbor
                    currentDistance[(x2,y2)] = newDistance

                    # Calculate the priority of the neighbor using the heuristic
                    priority = newDistance + heuristic(finish,(x2,y2))

                    # Add the neighbor into the queue
                    fringe.put((priority, (x2,y2)))

                    # Add the neighbor into prev
                    prev[(x2,y2)] = current
    # # Return if a path was not found
    # if finish not in prev:
    #     print("goal unreachable")
    #     return None

    return prev

# strat3()
# timesteps = get how far we are from the fire (mathattan distance)
# while current != finish
    # get 3d maze when q=1  & on the number of timesteps that we need
    # traverse through each maze in 3dMaze 
    #   do astar 3dMaze
    #   go through timesteps w each step
    #   if path has fire, set last possible step to current
    #       break
    #timesteps = get how far we are from the fire (mathattan distance)
    # get maze(s) for timesteps w/ q= actual q
    # aStar for that 3D maze
def driver(maze, start, finish, q):
    global Maze3D
    timesteps = disttoFire(maze, start)

    current = start
    while current != finish:
        deterministicMaze(maze, timesteps)
        prev = aStarF(maze, current, finish, q)
        if prev == None:
            
    # prev = aStarF(maze, start, finish, q)
    # tempfin = finish
    # if prev!=None:
    #     # Appending path to the stack
    #     stack = []
    #     stack.append(finish)
    #     while stack[-1] != start:
    #         stack.append(prev[finish])
    #         finish = stack[-1]
    #     while stack:
    #         node = stack.pop()
    #         maze[node[0]][node[1]]=2
    #         maze = advance_fire_one_step(maze, q)

    #         # check if any of the cells are on fire
    #         for i in range(len(stack)-1, -1, -1):
    #             if maze[stack[i][0]][stack[i][1]] == 5:
    #                 # recall A*
    #                 prev = aStarF(maze, node, tempfin, q)
    #                 if prev!=None:
    #                     stack = []
    #                     finish = tempfin
    #                     stack.append(finish)
    #                     while stack[-1] != node:
    #                         stack.append(prev[finish])
    #                         finish = stack[-1]
    #                     break
    #                 else:
    #                     print("no path found")
    #                     return maze
    # else:
    #     print("no path found")
    #     return maze
    # return maze

         

# print(driver(maze, (0,0), (2,2), .2))