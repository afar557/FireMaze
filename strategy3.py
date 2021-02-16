from queue import PriorityQueue
import math
from advancefire import advance_fire_one_step


maze = [[0,5,0],
        [0,0,0],
        [0,0,0]]

# Create a dictionary to store previously visited indices that you can use to trace a path
prev= {}
# Create fringe using a priority queue - prioritizes fire prob
fringe = PriorityQueue()
# Create a dictionary to store the current distance traveresed
currentDistance = {}

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

        aStarF(maze, current, finish, q)
        maze = advance_fire_one_step(maze, q)
        count+=1

    print(count)
    if finish not in prev:
        print("goal unreachable")
        return maze

    stack = []
    stack.append(finish)
    while stack[-1] != start:
        stack.append(prev[finish])
        finish = stack[-1]
    while stack:
        node = stack.pop()
        maze[node[0]][node[1]]=2
    return maze

            

# final = driver(maze, (0,0), (2,2), .2)
# for row in final:
#     print(row)


# fireHeuristic(maze, 1, (0,0))


