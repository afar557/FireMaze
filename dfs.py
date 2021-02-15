# use tuples instead of arrays
maze = [[0,0,0],
        [0,0,0],
        [0,0,0]]

def dfs(maze, start, finish):
    stack = []
    stack.append(start)

    visited = [[0 for y in range(len(maze))] for x in range(len(maze[0]))]
    # print(visited)
    row = 0
    col = 0
    while stack:
        curr = stack.pop()
        row = curr[0]
        col = curr[1]
        if row < 0 or col < 0 or row >= len(maze) or col >= len(maze[0]) or visited[row][col] == 1 or maze[row][col] == 1:
            continue
        
        visited[row][col] = 1
        maze[row][col] = 2
        stack.append([row+1,col]) # move down
        stack.append([row-1,col]) # move up
        stack.append([row,col+1]) # move right
        stack.append([row,col-1]) # move left
        # print('x: ',row,'y:',col)

        if row == finish[0] and col == finish[1]:
            print('reached goal')
            return maze
        
    print('did not reach goal')
    return maze

# dfs(maze, [0,0], [2,2])