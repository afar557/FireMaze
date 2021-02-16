import matplotlib.pyplot as plt
import numpy as np
import sys, os
sys.path.append("..")

from generateMaze import generateMaze
from Problem3.bfs import bfs
from Problem3.aStar import aStar
from dfs import dfs

    dimension = 100
    start = (0,0)
    finish = (dimension-1,dimension-1)

    bfsNodes =[]
    aStarNodes = []
    obstacleDensity = []

    for x in np.arange(0, 1, 0.001):
        p = x.item()
        obstacleDensity.append(p)
        bfsSum=0
        aStarSum=0

        grid = generateMaze(dimension,p)
