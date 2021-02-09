from queue import PriorityQueue
import math

# maze = [[0,0,0],
#         [0,0,0],
#         [0,0,0]]

def heuristic(a,b):
    #returns euclidean distance between two points
    return math.sqrt(((a[0]-b[0])**2) + ((a[1] - b[1])**2))


def aStar(maze, start, finish):
    fringe = PriorityQueue()

    fringe.put((0, start))

    prev= {}
    currentDistance = {}

    # insert into dicts
    prev[start] = None
    currentDistance[start] = 0

    x,y = start

    while not fringe.empty():
        current = fringe.get()[1]

        if current == finish:
            break     
        x,y = current
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)): # explore all neighbors up, down, right, left 
            # check if within bounds & unblocked
            if 0 <= x2 < len(maze[0]) and 0 <= y2 < len(maze) and maze[x2][y2]==0:
                # each step is 1 distance from another
                newDistance = currentDistance[current] + 1
                if (x2,y2) not in currentDistance or newDistance < currentDistance[(x2,y2)]:
                    currentDistance[(x2,y2)] = newDistance
                    priority = newDistance + heuristic(finish,(x2,y2))
                    fringe.put((priority, (x2,y2)))
                    prev[(x2,y2)] = current
    
    
    if finish not in prev:
        print("goal unreachable")
        return maze

    node = finish
    maze[node[0]][node[1]]=2

    while node != start:
        node = prev[finish]
        finish = node
        maze[node[0]][node[1]]=2
    return maze

            

