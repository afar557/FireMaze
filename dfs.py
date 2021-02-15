# Function that executes the BFS algorithm and returns the maze with the path
def dfs(maze, start, finish):
    # Create a stack and add the start index to it
    stack = []
    stack.append(start)

    # Create a visited array and make all cells of the maze unvisited
    visited = [[0 for y in range(len(maze))] for x in range(len(maze[0]))]

    row = 0
    col = 0
    while stack:
        # Pop an index from the stack
        curr = stack.pop()
        row = curr[0]
        col = curr[1]

        # If the row and column are in bounds and the cell has been visited or is blocked
        # *****CHECK THIS STATEMENT HERE,, CHECK ORS*****
        if row < 0 or col < 0 or row >= len(maze) or col >= len(maze[0]) or visited[row][col] == 1 or maze[row][col] == 1:
            continue
        
        # Mark the cell as visited
        visited[row][col] = 1

        # Mark the cell as part of the path
        maze[row][col] = 2
        # print('x: ',row,'y:',col)

        # Add all the neighbors of the current cell to the queue
        # Move down
        stack.append([row+1,col])

        # Move up
        stack.append([row-1,col])

        # Move right
        stack.append([row,col+1])

        # Move left
        stack.append([row,col-1])

        # Check if you have reached the goal and if so return the maze
        if row == finish[0] and col == finish[1]:
            print('reached goal')
            return maze
        
    print('did not reach goal')
    return maze