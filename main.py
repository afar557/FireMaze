import random

def generateMaze(dimension, p):
    maze=[]
    for i in range(dimension): 
        column = [] 
        for j in range(dimension): 
            if (random.uniform(0,1)<= p):
                column.append("blocked")
            else:
                column.append("open") 
        maze.append(column)  
    return maze 

def main():
    print(generateMaze(10,0.5))

if __name__ == "__main__":
    main()