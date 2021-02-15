import matplotlib.pyplot as plt
import numpy as np
from strategy1 import bfsStrat1
from generateMaze import generateMaze, generateFireMaze

def st1plot():
    p = 0.3
    q = 0
    dim = 100
    start = (0,0)
    finish = (dim-1, dim-1)
    # For each strategy, for as large a dimension as your system can handle, and obstacle density p = 0:3, 
    # generate a plot of average successes vs fammability q'.
    # For each test value of q, generate and solve at least 10 mazes, restarting each 10 times with new initial re locations. 
    # Note: Please discard any maze where there is no path from the start to the goal node. 
    # Please discard any maze where there is no path from the initial position of the agent to the initial position of the fire
st1plot()