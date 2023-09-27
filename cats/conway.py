# Conways Game of Life
import random, time, copy

WIDTH = 10
HEIGHT = 10
# LIST OF LIST FOR CELLS
nextCells=[]
for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if (x,y) in ((1,0),(0,1),(0,2),(2,0),(0,0)):
            column.append('#')  # add living
        else:
            column.append(' ')  # add dead
    nextCells.append(column)
while True:  # main loop
    print('\n\n\n\n\n\n')
    currentCells = copy.deepcopy(nextCells)
    # print currentCells on screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='')  # print # or space
        print()  # newline at the end of row
    # calc next steps cells based on current steps cells
    for x in range(WIDTH):
        for y in range(HEIGHT):  # get neighbouring coords
            #%Width/%height ensures coord always between 0 and width-1
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT  # count living neighbours
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors+=1
            if currentCells[x][aboveCoord] == '#':
                numNeighbors+=1
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors+=1
            if currentCells[leftCoord][y] == '#':
                numNeighbors+=1
            if currentCells[rightCoord][y] == '#':
                numNeighbors+=1
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors+=1
            if currentCells[x][belowCoord] == '#':
                numNeighbors+=1
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors+=1
            # set cell based on conways game of life
            if currentCells[x][y] == '#' and (numNeighbors == 2 or
            numNeighbors == 3):
                nextCells[x][y]='#'
                # living cells with 2 or 3 alive neigh stay alive
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                nextCells[x][y]='#'
                # dead comes alive when exactly 3 alive neigh
            else:
                nextCells[x][y] = ' '  # others stay dead
    time.sleep(1)  # adds 1 sec pause for reduced flickering
