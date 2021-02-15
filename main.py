import random
import pygame
from bfs import bfs
from dfs import dfs
from collections import deque
from advancefire import advance_fire_one_step 
from generateMaze import generateMaze, generateFireMaze
from aStar import aStar
from strategy1 import bfsStrat1
from strategy2 import bfsStrat2
from time import time


def main():
    # dimension = 5000
    # p = 0.1
    # q = 0.1
    # start = (0,0)
    # finish = (9,9)
    # grid = generateFireMaze(dimension,p)
    # grid = advance_fire_one_step(grid, 1)
    # grid = generateMaze(dimension,p)
    # print(grid)
    # grid = aStar(grid, (0,0), (9,9))
    # grid = bfs(grid, (0,0), (9,9))
    # grid = bfsStrat1(grid, start, finish, q)
    # grid = bfsStrat2(grid, start, finish, q)

    # # FOR PROBLEM 4
    # p = 0.3
    # diff = 0
    # dimension = 5000
    # print("starting")
    # while diff<60:
    #     dimension+=100
    #     grid = generateMaze(dimension,p)
    #     start = time()
    #     grid = dfs(grid, (0,0), (dimension-1,dimension-1))
    #     end = time()

    #     diff = end-start
    #     print(diff , "for dim --> " , dimension)
        

    # print(dimension)
    # return


    # Define colors for maze
    BLACK = (0, 0, 0)
    GRAY = (105, 105, 105)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    
    # sets the WIDTH and HEIGHT of each grid spot
    WIDTH = 20
    HEIGHT = 20
    # sets the margin between each cell
    MARGIN = 3

    # Initialize pygame
    pygame.init()
    
    # Set size of screen
    WINDOW_SIZE = [(MARGIN * dimension+2) + (dimension*WIDTH), (MARGIN * dimension+2) + (dimension*WIDTH)]
    screen = pygame.display.set_mode(WINDOW_SIZE)
    # Set title of screen
    pygame.display.set_caption("Fire Maze")
    
    # Loop until the user clicks the close button.
    done = False
    
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    
    # sets up maze
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
    
        # Set the screen background
        screen.fill(BLACK)
    
        # Draw the grid
        for row in range(dimension):
            for column in range(dimension):
                # if area is blocked then set color to gray
                if grid[row][column] == 1:
                    color = GRAY
                # set cell to green to display the path
                elif grid[row][column] == 2:
                    color = GREEN
                # if the cell is on fire, set color to red
                elif grid[row][column] == 5:
                    color = RED
                # if this area is open set color to white
                elif grid[row][column] == 0:
                    color = WHITE
                # draw the maze
                pygame.draw.rect(screen,
                                color,
                                [(MARGIN + WIDTH) * column + MARGIN,
                                (MARGIN + HEIGHT) * row + MARGIN,
                                WIDTH,
                                HEIGHT])
    
        # Limit to 60 frames per second
        clock.tick(60)
    
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
         
    # on exit.
    pygame.quit()
if __name__ == "__main__":
    main()