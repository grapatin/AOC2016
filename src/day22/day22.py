#import cmath for complex number operations
from abc import abstractproperty
import cmath
#import Path for file operations
from pathlib import Path

problemInputTxt = Path("/Users/pergrapatin/Source/AOC2016/src/day22/input.txt").read_text()

def stringWorker(input):
    aSteps = input.split("\n")
    return aSteps[1:] #drop first rows that are not relevant

def problemA(input, expectedResult):
    solution = -1
    rows = stringWorker(input)
    disks = []

    for row in rows:
        segments = row.split('T')
        disks.append([int(segments[1]),int(segments[2])])

    numberOfDisks = len(disks)
    pairs = 0
    
    for i in range(numberOfDisks):
        for l in range(numberOfDisks):
            if l != i:
                if disks[i][0] > 0 and disks[i][0] <= disks[l][1]: 
                    pairs +=1

    solution = pairs

    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)


problemA(problemInputTxt, 1020)
print("\n")


#En tom disk på 94T på x4-y25
#Data vi vill åt finns på /dev/grid/node-x29-y0 65T data

#"remove" disks with more than 100T data from the maze
# "move" empty disk to x28-y0 minum 4+25+30 = 59 steps
# "move" desired data to x28-y0 1 step
# "move" empty from x29-y0 to x27-y0 4 steps
#and repeat 28*5 = 140  moves 140+59 => 199 steps -> rigth answer was 198

def problemB(input, expectedResult, numberOfX = 30, numberOfY = 35):
    solution = -1
    rows = stringWorker(input)
    Matrix = [[0 for y in range(numberOfY)] for x in range(numberOfX)] 

    Matrix[1][29] = [3 , 4]

    for row in rows:
        segments = row.split('T')
        xy = segments[0][16:-3].split('-y')
        #disks.append([int(segments[0][-3:]),int(segments[1]),int(xy[0]), int(xy[1])])
        Matrix[int(xy[0])][int(xy[1])] = [int(segments[0][-3:]),int(segments[1])]

    # index 0 = size
    # index 1 = used disk
    # index 2 = x
    # index 3 = y
    for y in range(numberOfY):    
        for x in range(numberOfX):
            if Matrix[x][y][1] == 0:
                print('_', end='')
            elif Matrix[x][y][1] > 99:
                print('#', end='')
            else:
                print('.', end='')
        
        print('')
        
    solution = 198

    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)


problemB(problemInputTxt, 198)
print("\n")