from queue import PriorityQueue
import math

# Function that returns the euclidean distance between two points on the maze
def heuristic(a,b):
    return math.sqrt(((a[0]-b[0])**2) + ((a[1] - b[1])**2))

# Function that executes the A* algorithm and returns the number of nodes the algorithm visits
def aStar(maze, start, finish):
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
        return len(prev)

    # Mark the path on the maze and return the maze
    node = finish
    maze[node[0]][node[1]]=2

    while node != start:
        node = prev[finish]
        finish = node
        maze[node[0]][node[1]]=2

    return len(prev)

            

