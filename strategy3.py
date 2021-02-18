from queue import PriorityQueue
import math
from advancefire import advance_fire_one_step
from copy import deepcopy

maze = [[0,0,5],
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
    for i in range(timesteps):
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
    return newMaze

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
def aStarF(maze, start, finish):
    global Maze3D

    # Create fringe using a priority queue
    fringe = PriorityQueue()

    # Add in the starting index (0,0) to the queue
    fringe.put(((0,0), start))

    # Create a dictionary to store previously visited indices that you can use to trace a path
    prev= {}
    prev[start] = None

    # Create a dictionary to store the current distance traveresed
    currentDistance = {}
    currentDistance[start] = 0

    # Initialize x,y values to start
    x,y = start
    while not fringe.empty():
        # Get the first index in the queue
        current = fringe.get()[1]

        # If you get to the finish index, break out of the loop
        if current == finish:
            break     
        
        # Set x,y to the current index
        x,y = current

        timestep = 0
        node = current
        while(node != start):
            node = prev[node]
            timestep += 1
        if timestep >= len(Maze3D)-1:
            path = []
            path.append(current)
            if len(prev) == 1:
                return None
            while(path[-1] != start):
                path.append(prev[current])
                current = path[-1] 
            return path
        else:
            maze = Maze3D[timestep+1]

        # Explore all 4 neighbors of the current cell: up, down, right and left
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            # If the coordinates are in bounds and the neighbor cell is open
            if 0 <= x2 < len(maze[0]) and 0 <= y2 < len(maze) and maze[x2][y2] != 1 and maze[x2][y2] != 5 and maze[x2][y2] != 2:
                # Calculate the new distance from current cell to neighbor by adding 1
                newDistance = currentDistance[current] + 1
                # If the neighbor has not been previously visited or the new distance to the neighbor is less than the currently stored distance to the neighbor
                if (x2,y2) not in currentDistance or newDistance < currentDistance[(x2,y2)]:
                    # Update the current distance for the current neighbor
                    currentDistance[(x2,y2)] = newDistance
                    # Calculate the priority of the neighbor using the heuristic
                    priority = newDistance + heuristic(finish,(x2,y2))

                    fireProb = maze[x2][y2]
                    fringe.put(((fireProb, priority), (x2,y2)))
                    
                    # Add the neighbor into the queue
                    # fringe.put((priority, (x2,y2)))

                    # Add the neighbor into prev
                    prev[(x2,y2)] = current
    path = []
    path.append(current)
    if len(prev) == 1:
        return None
    while(path[-1] != start):
        path.append(prev[current])
        current = path[-1] 
    return path

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
    count=0
    current = start
    while current != finish:
        if count==200:
            return

        deterministicMaze(maze, timesteps)
        # print("Printing deterministic maze for timestep, ",timesteps)
        # for maze1 in Maze3D:
        #     for row in maze1:
        #         print(row)
        #     print("---------")
        path = aStarF(maze, current, finish)
        print()
        print()
        if path != None:
            # print("Path in deterministic is, ",path)
            # print()

            current = path[0]
            # print("Printing maze after path")
            # for row in maze:
            #     print(row)
            # print()
            while path:
                node = path.pop()
                if maze[node[0]][node[1]] != 5:
                    maze[node[0]][node[1]] = 2
                    # print("Printing maze after path")
                    # for row in maze:
                    #     print(row)
                    # print()
                else:
                    # for row in maze:
                    #     print(row)
                    # print()
                    if node == finish:
                        print("No path found!")
                        return maze
                    else:
                        print("This should not happen")
                maze = advance_fire_one_step(maze,q)
            timesteps = disttoFire(maze, current)

        else:
            Maze3D = []
            tempMaze = deepcopy(maze)
            for i in range(timesteps):
                tempMaze = getProbMaze(tempMaze, q)
                Maze3D.append(tempMaze)
            # for maze2 in Maze3D:
            #     for row in maze2:
            #         print(row)
            #     print("---------")
            path = aStarF(maze, current, finish)
            
            if path != None:
                # print("Path in probability is, ",path)
                # print()
                current = path[0]
                # print("Printing maze after path")
                # for row in maze:
                #     print(row)
                # print()
                while path:
                    node = path.pop()
                    # print("Node in prod ",node)
                    if maze[node[0]][node[1]] != 5:
                        maze[node[0]][node[1]] = 2
                        # print("Printing maze after path")
                        # for row in maze:
                        #     print(row)
                        # print()
                    else:
                        # for row in maze:
                        #     print(row)
                        # print()
                        if node == finish:
                            print("No path found!")
                            return maze
                        else:
                            print("This should not happen")
                    maze = advance_fire_one_step(maze,q)
                timesteps = disttoFire(maze, current)
            else:
                print("Path in probability is none")
        count+=1
    print("CONGRATULATIONS! YOU HAVE REACHED YOUR DESTINATION!")
    return maze

driver(maze, (0,0), (2,2), .2)