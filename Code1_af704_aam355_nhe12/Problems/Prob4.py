from time import time
import sys


sys.path.append("..")
from generateMaze import generateMaze, generateFireMaze
from dfs import dfs
from bfs import bfs
from aStar import aStar

# FOR PROBLEM 4
def prob4dfs():
    p = 0.3
    dimension = 4450
    print("starting DFS")
    while True:
        print(dimension)
        avgdiff = 0
        for i in range(10):
            grid = generateMaze(dimension,p)
            start = time()
            grid = dfs(grid, (0,0), (dimension-1,dimension-1))
            end = time()

            avgdiff += end-start
            print("Diff is -> ", end-start)

        avgdiff /= 10
        print(avgdiff , "for dim --> " , dimension)
        if avgdiff>60:
            dimension-=5
            continue
        dimension+=10    
    return

def prob4bfs():
    p = 0.3
    dimension = 3000
    print("starting BFS")
    while True:
        print(dimension)
        avgdiff = 0
        for i in range(10):
            grid = generateMaze(dimension,p)
            start = time()
            grid = bfs(grid, (0,0), (dimension-1,dimension-1))
            end = time()

            avgdiff += end-start
            print("Diff is -> ", end-start)

        avgdiff /= 10
        print(avgdiff , "for dim --> " , dimension)
        if avgdiff>60:
            dimension-=5
            continue
        dimension+=10
    return

def prob4Astar():
    p = 0.3
    dimension = 2500
    print("starting A*")
    while True:
        print(dimension)
        avgdiff = 0
        for i in range(10):
            grid = generateMaze(dimension,p)
            start = time()
            grid = aStar(grid, (0,0), (dimension-1,dimension-1))
            end = time()

            avgdiff += end-start
            # print("Diff is -> ", end-start)

        avgdiff /= 10
        print(avgdiff , "for dim --> " , dimension)
        if avgdiff>60:
            dimension-=5
            continue
        dimension+=10
    return
prob4Astar()