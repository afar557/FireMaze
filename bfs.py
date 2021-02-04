from collections import deque

maze = [[0,0,0],
        [0,0,0],
        [0,0,0]]

# def bfs(maze, start, finish):
#     queue = deque()
#     queue.append([[start]])

#     visited = [[0 for y in range(len(maze))] for x in range(len(maze[0]))]
#     # print(visited)
#     row = 0
#     col = 0
#     while queue:
#         curr = queue.popleft()
#         row, col = curr[-1]
#         if row < 0 or col < 0 or row >= len(maze) or col >= len(maze[0]) or visited[row][col] == 1 or maze[row][col] == 1:
#             continue
        
#         visited[row][col] = 1
#         # maze[row][col] = 2
#         print('x: ',row,'y:',col)
#         queue.append(curr + [(row+1,col)]) # move down
#         queue.append(curr + [(row-1,col)]) # move up
#         queue.append(curr + [(row,col+1)]) # move right
#         queue.append(curr + [(row,col-1)]) # move left
#         # print('x: ',row,'y:',col)

#         if row == finish[0] and col == finish[1]:
#             print('reached goal')
#             return maze
        
#     print('did not reach goal')
#     return maze

def bfs(maze, start, finish):
    width = len(maze[0])
    height = len(maze)
    queue = deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if x == finish[0] and y == finish[1]:
            for position in path:
                maze[position[0]][position[1]] = 2
            print(maze)
            return maze
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < width and 0 <= y2 < height and (x2, y2) not in seen:
                print('inside if in for')
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
    
    return maze

# bfs(maze, (0,0), (2,2))