import matplotlib.pyplot as plt
from dfs import dfs
from generateMaze import generateMaze, generateFireMaze
import numpy as np

# Befor running this code, change dfs code to return 1 if success and 0 if fail

def getPlot():
    dimension = 100
    start = (0,0)
    finish = (dimension-1,dimension-1)
    ps = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
    # ps = []
    # for i in np.arange(0,1.01,0.01):
    #     ps.append(i)
    # print(ps[-1])
    # ps = [0.9]
    successProb = []
    for p in ps:
        successProb.append(0)
        for i in range(50):
            grid = generateMaze(dimension,p)
            goalReached = dfs(grid, start, finish)
            # print(goalReached)
            successProb[-1] += goalReached
        successProb[-1] /= 50
    # print(successProb)
    plt.plot(ps, successProb)
    plt.show()
getPlot()