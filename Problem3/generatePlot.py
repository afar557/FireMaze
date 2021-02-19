import matplotlib.pyplot as plt
import numpy as np
import sys, os

sys.path.append("..")

from generateMaze import generateMaze
from Problem3.bfs import bfs
from Problem3.aStar import aStar
from dfs import dfs

# maze = [[0,0,0,0,0,1],
#         [0,0,0,0,1,0],
#         [0,0,0,1,0,0],
#         [0,0,1,0,0,1],
#         [0,1,0,0,0,0],
#         [1,0,0,0,0,0]]
def getPlot():
    dimension = 100
    start = (0,0)
    finish = (dimension-1,dimension-1)

    bfsNodes =[]
    aStarNodes = []
    obstacleDensity = []

    for x in np.arange(0, 1, 0.01):
        p = x.item()
        obstacleDensity.append(p)
        bfsSum=0
        aStarSum=0

        grid = generateMaze(dimension,p)

        for i in range(50):
            grid = generateMaze(dimension,p)
            bfsSum += bfs(grid, start, finish)
            aStarSum += aStar(grid, start, finish)

        bfsNodes.append(bfsSum/50)
        aStarNodes.append(aStarSum/50)

    plt.plot(obstacleDensity, bfsNodes, label = "bfs")
    plt.plot(obstacleDensity, aStarNodes, label = "a*")
    plt.xlabel('obstacle density p')
    plt.ylabel('avg # of nodes explored')
    plt.title('# of nodes explored by BFS - # of nodes explored by A*  VS  obstacle density p ')
    plt.legend()
    plt.show()

getPlot()
dimension = 15
maze = generateMaze(dimension,0.4)
print(maze)
print("num of nodes explored by bfs", bfs(maze,(0,0), (dimension-1,dimension-1)))
print("num of nodes explored by a*", aStar(maze,(0,0), (dimension-1,dimension-1)))