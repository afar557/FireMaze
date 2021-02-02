import random
import pygame


def generateMaze(dimension, p):
    # initialize maze
    maze=[]

    for i in range(dimension): 
        # initialize col to set vals
        column = [] 
        for j in range(dimension): 
            # for each square check if random(0,1) is less than or equal to p
            if (random.uniform(0,1)<= p):
                # set square to blocked
                column.append(1)
            else:
                # set square to open
                column.append(0) 
        # append col to maze
        maze.append(column)

    # set start & goal to open  
    maze[0][0] = 0
    maze[dimension-1][dimension-1]=0

    return maze 

def main():
    dimension = 10
    p = 0.5
    grid = generateMaze(dimension,p)
    print(grid)

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