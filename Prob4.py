from time import time
from generateMaze import generateMaze, generateFireMaze
from dfs import dfs
from bfs import bfs
from aStar import aStar

# FOR PROBLEM 4
def prob4dfs():
    p = 0.3
    diff = 0
    dimension = 4000
    print("starting DFS")
    while diff<60:
        dimension+=100
        grid = generateMaze(dimension,p)
        start = time()
        grid = dfs(grid, (0,0), (dimension-1,dimension-1))
        end = time()

        diff = end-start
        print(diff , "for dim --> " , dimension)

    print(dimension)
    return

def prob4bfs():
    p = 0.3
    diff = 0
    dimension = 5000
    print("starting BFS")
    while diff<60:
        dimension+=100
        grid = generateMaze(dimension,p)
        start = time()
        grid = bfs(grid, (0,0), (dimension-1,dimension-1))
        end = time()

        diff = end-start
        print(diff , "for dim --> " , dimension)
        
    print(dimension)
    return

def prob4Astar():
    p = 0.3
    diff = 0
    dimension = 5000
    print("starting A*")
    while diff<60:
        dimension+=100
        grid = generateMaze(dimension,p)
        start = time()
        grid = aStar(grid, (0,0), (dimension-1,dimension-1))
        end = time()

        diff = end-start
        print(diff , "for dim --> " , dimension)
        
    print(dimension)
    return
prob4dfs()