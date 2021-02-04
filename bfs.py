from collections import deque

maze = [[0,0,0],
        [0,0,0],
        [0,0,0]]

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