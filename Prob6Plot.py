import matplotlib.pyplot as plt
import numpy as np
from strategy1 import bfsStrat1
from strategy2 import bfsStrat2
from generateMaze import generateMaze, generateFireMaze

def st1plot():
    # For each strategy, for as large a dimension as your system can handle, and obstacle density p = 0:3, 
    # generate a plot of average successes vs flammability q'.
    # For each test value of q, generate and solve at least 10 mazes, restarting each 10 times with new initial fire locations. 
    # Note: Please discard any maze where there is no path from the start to the goal node. 
    # Please discard any maze where there is no path from the initial position of the agent to the initial position of the fire
    p = 0.3
    qvals = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
    dim = 100
    start = (0,0)
    finish = (dim-1, dim-1)

    avgSuccesses = []
    for q in qvals:
        print(q)
        count = 0
        success = 0
        i = 0
        while i<50:
            count+=1
            grid = generateFireMaze(dim,p)
            # 0 for ran into fire
            # 1 for got to goal
            # 2 for no path found
            ans = bfsStrat1(grid, start, finish, q)
            if ans == 2:
                continue
            i+=1
            success+=ans
        success/=50
        avgSuccesses.append(success)
    plt.plot(qvals, avgSuccesses)
    plt.xlabel('Flammability q')
    plt.ylabel('Average Successes')  
    plt.show()

def st2plot():
    p = 0.3
    qvals = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
    dim = 100
    start = (0,0)
    finish = (dim-1, dim-1)

    avgSuccesses = []
    for q in qvals:
        print("q is: ",q)
        count = 0
        success = 0
        i = 0
        while i<50:
            count+=1
            grid = generateFireMaze(dim,p)
            # 0 for ran into fire
            # 1 for got to goal
            # 2 for no path found
            ans = bfsStrat2(grid, start, finish, q)
            if ans == 2:
                continue
            i+=1
            success+=ans
        success/=50
        avgSuccesses.append(success)
    plt.plot(qvals, avgSuccesses)
    plt.xlabel('Flammability q')
    plt.ylabel('Average Successes')  
    plt.show()
st2plot()