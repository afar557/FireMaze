from queue import PriorityQueue
import math
from advancefire import advance_fire_one_step


maze = [[0,5,0],
        [0,0,0],
        [0,0,0]]

# Function that returns the euclidean distance between two points on the maze
def fireHeuristic(maze, q, currentPos):
    sum = 0
    for i in range(10):
        tempMaze = advance_fire_one_step(maze, q)
        if tempMaze[currentPos[0]][currentPos[1]] == 5:
            sum+=1
    return sum/10

def heuristic(a,b):
    return math.sqrt(((a[0]-b[0])**2) + ((a[1] - b[1])**2))
            
# Function that executes the A* algorithm and returns the maze with the path
def aStarF(maze, start, finish, q):
    global prev
    global fringe
    global currentDistance


    # Initialize x,y values to start
    x,y = start
    current = start
    
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

                fireProb = fireHeuristic(maze, q, (x2,y2))


                # Add the neighbor into the queue
                fringe.put(((fireProb, priority), (x2,y2)))

                # Add the neighbor into prev
                prev[(x2,y2)] = current


def driver(maze, start, finish, q):
    global prev
    global fringe
    global currentDistance
    
    currentDistance[start] = 0

    prev[start] = None

    # Add in the starting index (0,0) to the queue
    # tuple[0]= fireHeurisitc, tuple[1] = euclidean distance
    fringe.put(((0,0), start))
    count=0
    current = start
    while not fringe.empty():
        # Get the first index in the queue
        current = fringe.get()[1]

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
    # Return if a path was not found
    if finish not in prev:
        print("goal unreachable")
        return None

    return prev

def driver(maze, start, finish, q):

    prev = aStarF(maze, start, finish, q)
    tempfin = finish
    if prev!=None:
        # Appending path to the stack
        stack = []
        stack.append(finish)
        while stack[-1] != start:
            stack.append(prev[finish])
            finish = stack[-1]
        while stack:
            node = stack.pop()
            maze[node[0]][node[1]]=2
            maze = advance_fire_one_step(maze, q)

            # check if any of the cells are on fire
            for i in range(len(stack)-1, -1, -1):
                if maze[stack[i][0]][stack[i][1]] == 5:
                    # recall A*
                    prev = aStarF(maze, node, tempfin, q)
                    if prev!=None:
                        stack = []
                        finish = tempfin
                        stack.append(finish)
                        while stack[-1] != node:
                            stack.append(prev[finish])
                            finish = stack[-1]
                        break
                    else:
                        print("no path found")
                        return maze
    else:
        print("no path found")
        return maze
    return maze

            

# print(driver(maze, (0,0), (2,2), .2))

            
# getMazeWhen q = 1 (q, maze, timesteps)
# 3dMaze = [maze]
# for i in range(timesteps)
#   newMaze = advance_fire(3DMaze[-1])
#   3dMaze.append(newMaze)

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

# fucntuon that gets distance to fire

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
