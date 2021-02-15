from time import time
from generateMaze import generateMaze, generateFireMaze
from dfs import dfs

# FOR PROBLEM 4
def prob4():
    p = 0.3
    diff = 0
    dimension = 5000
    print("starting")
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
prob4()