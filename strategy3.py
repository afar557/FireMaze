from queue import PriorityQueue
import math
from advancefire import advance_fire_one_step
from copy import deepcopy
from st3DFS import dfs

Maze3D = []

# Function used to produce the 3D deterministic maze at q=1
def deterministicMaze(maze, timesteps):
    global Maze3D
    q = 1
    Maze3D = [maze]
    for i in range(timesteps):
        newMaze = advance_fire_one_step(Maze3D[-1], q)
        Maze3D.append(newMaze)

# Function used to produce the fire probability maze
# We simulate the fire 10 times on the maze in order to get the average probability of each cell being on fire
def getProbMaze(maze, q, timesteps):
    # Advance the fire in the actual maze to the current timestep
    for y in range(timesteps):
        maze = advance_fire_one_step(maze, q)
    # Create a copy of the current maze in order to get the average probability
    newMaze = deepcopy(maze)
    # Simulate 10 fire mazes for the current time step
    for x in range(10):
        tempMaze = advance_fire_one_step(maze, q)
        for i in range(len(newMaze)):
            for j in range(len(newMaze)):
                if tempMaze[i][j] == 5:
                    newMaze[i][j] += 5
    # Divide each cell by 10 to get the average and by 5 in order to get a probability from 0-1
    for i in range(len(newMaze)):
        for j in range(len(newMaze)):
            if newMaze[i][j] != 1 and newMaze[i][j] != 2:
                newMaze[i][j] /= 50
    return newMaze

# Function that gets the distance from the current position to nearest fire
def disttoFire(maze, currentpos):
    mindist = len(maze)**2
    for i in range(len(maze)):
        for j in range(len(maze)):
            if maze[i][j] == 5 and manDist(currentpos, (i,j))<mindist:
                mindist = manDist(currentpos, (i,j))
    if mindist==0:
        mindist+=1
    return mindist

# Function that calculates the Manhattan distance from one point to the other
def manDist(a,b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Function that calculates the Eclidean distance from one point to the other
def heuristic(a,b):
    return math.sqrt(((a[0]-b[0])**2) + ((a[1] - b[1])**2))
            
# Function that executes the A* algorithm and returns a path
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

    # Create a dictionary to store the current probabilities of the cells traveresed
    currentProb = {}
    currentProb[start] = maze[start[0]][start[1]]

    # Initialize x,y values to start
    x,y = start
    timestep = 0
    while not fringe.empty():
        # Get the first index in the queue
        current = fringe.get()[1]

        # If you get to the finish index, break out of the loop
        if current == finish:
            break     
        
        # Set x,y to the current index
        x,y = current

        # If you have finished all the time steps, finish the path in the first maze
        node = current
        if timestep >= len(Maze3D)-1:
            maze = Maze3D[0]
        
        else:
            # Caalculate which timestep you're on in order to access the correct maze in the 3D Maze
            timestep = 0
            while(node != start):
                node = prev[node]
                timestep += 1
            if timestep >= len(Maze3D)-1:
                maze = Maze3D[0]
            else:
                maze = Maze3D[timestep+1]
            
        # Explore all 4 neighbors of the current cell: up, down, right and left
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            # If the coordinates are in bounds and the neighbor cell is open
            if 0 <= x2 < len(maze[0]) and 0 <= y2 < len(maze) and maze[x2][y2] != 1 and maze[x2][y2] != 5 and maze[x2][y2] != 2:
                # Calculate the new distance from current cell to neighbor by adding 1
                newDistance = currentDistance[current] + 1
                # Calculate the new probability by adding the probability from current cell to the probability of the current neighbor
                newProb = currentProb[current] + maze[x2][y2]
                # If the neighbor has not been previously visited or the new distance to the neighbor is less than the currently stored distance to the neighbor
                if (x2,y2) not in currentProb or newProb < currentProb[(x2,y2)] or (x2,y2) not in currentDistance or newDistance < currentDistance[(x2,y2)]:
                    # Update the current distance for the current neighbor
                    currentDistance[(x2,y2)] = newDistance
                    # Update the current probability for the current neighbor
                    currentProb[(x2,y2)] = newProb

                    # Calculate the priority of the neighbor using the heuristic
                    priority = newDistance + heuristic(finish,(x2,y2))

                    fringe.put(((newProb, priority), (x2,y2)))

                    # Add the neighbor into prev
                    prev[(x2,y2)] = current

    # If finish is not in prev, there is no path through the maze
    if finish not in prev:
        return None
    
    # If prev only has one element, there is not path through the maze
    if len(prev) == 1:
        return None

    # Calculate the path using prev
    path = []
    path.append(finish)
    while(path[-1] != start):
        path.append(prev[finish])
        finish = path[-1] 

    # Return the path for the timesteps in Maze3D
    path = path[-len(Maze3D):]
    return path

def driver(maze, start, finish, q):
    global Maze3D

    # Check if a path is possible through the maze
    test = deepcopy(maze)
    if dfs(test, start, finish) == 0:
        print("Maze unsolvable!")
        return maze

    timesteps = disttoFire(maze, start)
    current = start
    while current != finish:

        # If the goal is on fire, there is no path to finish the maze
        if maze[finish[0]][finish[1]]==5:
            print("No path found!")
            return maze

        # Create the deterministic 3D Maze to try to solve the maze for q=1  
        deterministicMaze(maze, timesteps)
        # Run the A* algorithm on the deterministic 3D maze
        path = aStarF(maze, current, finish)
        # If a path was found 
        if path != None:
            # Reset current to the last position in the path
            current = path[0]
            
            # Mark your path on the maze
            while path:
                # Pop the first step from path
                node = path.pop()
                # Mark the step on the maze if it is not on fire
                if maze[node[0]][node[1]] != 5:
                    maze[node[0]][node[1]] = 2
                # If step is on fire in the maze
                else:
                    # If that step is the goal cell, there is no path through the maze
                    if node == finish:
                        print("No path found!")
                        return maze
                    else:
                        print("This should not happen")
                        return maze
                # Advance the fire in the maze after taking one step
                maze = advance_fire_one_step(maze,q)
            # Recalculate timesteps based on the closest fire to the current position
            timesteps = disttoFire(maze, current)

        # If  path was not found, you have to use the probability maze with the actual value of q to see if it is possible to find a path
        else:
            # Reset the 3D Maze
            Maze3D = [maze]
            # Create your 3D Maze by creating a probability maze for each timestep
            for i in range(timesteps):
                tempMaze = getProbMaze(maze, q, timesteps)
                Maze3D.append(tempMaze)

            # Call the A* algorithm on the probability 3D maze
            path = aStarF(maze, current, finish)
            # If a path was found
            if path != None:
                # Reset current to the last position in the path
                current = path[0]
                
                # Mark your path on the maze
                while path:
                    # Pop the first step from path
                    node = path.pop()
                    # Mark the step on the maze if it is not on fire
                    if maze[node[0]][node[1]] != 5:
                        maze[node[0]][node[1]] = 2
                    # If step is on fire in the maze
                    else:
                        # If the step is the goal cell, there is no path through the maze
                        if node == finish:
                            print("No path found!")
                            return maze
                        else:
                            print("No path found!")
                            return maze
                    # Advance the fire in the maze after taking one step
                    maze = advance_fire_one_step(maze,q)
                # Recalculate timesteps based on the closest fire to the current position
                timesteps = disttoFire(maze, current)

            # If a path was not found using the actual value of q then there is no path through the maze
            else:
                print("No path found!")
                return maze
    # You are out of the loop and have reached your goal
    print("CONGRATULATIONS! YOU HAVE REACHED YOUR DESTINATION!")
    return maze