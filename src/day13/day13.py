# import cmath for complex number operations
from abc import abstractproperty
import cmath
from os import X_OK
# import Path for file operations
from pathlib import Path

problemInputTxt = Path(
    "/Users/pergrapatin/Source/AOC2016/src/day13/input.txt").read_text()


def stringWorker(input):
    aSteps = input.split("\n")
    return aSteps


def checkIfWallOrOpenSpace(x, y, input):
    formula = x*x + 3*x + 2*x*y + y + y*y
    sum = formula + input
    binaryString = bin(sum)[2:]
    NumberOfOnes = binaryString.count('1')
    if NumberOfOnes % 2 == 0:
        return '.'  # Even => Openspace
    else:
        return '#'  # Odd => Wall


storageXY = {}
storageFastestWay = {}
directions = [1, 0], [0, -1], [0, 1], [-1, 0]


def cordString(x, y):
    return str(x)+','+str(y)


def mazeCrawler(currX, currY, reachX, reachY, distanceTraveled):
    for i in range(4):
        tX = currX + directions[i][0]
        tY = currY + directions[i][1]
        newDistanceTravaled = distanceTraveled + 1
        #if currX == reachX and currY == reachY:
        #target found
        if cordString(tX, tY) in storageXY and storageXY[cordString(tX,tY)] == '.':            
            if cordString(tX, tY) not in storageFastestWay or storageFastestWay[cordString(tX,tY)] > newDistanceTravaled:
                #new possible position found
                storageFastestWay[cordString(tX, tY)] = newDistanceTravaled
                mazeCrawler(tX, tY, reachX, reachY, newDistanceTravaled)

            

def problemA(input, expectedResult, reachX, reachY):
    solution = -1

    for y in range(100):
        for x in range(100):
            storageXY[cordString(x, y)] = checkIfWallOrOpenSpace(x, y, input)
    
    # Maze crawler start at 1,1
    mazeCrawler(1,1,reachX, reachY, 0)

    solution = storageFastestWay[cordString(reachX, reachY)]
    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:",
              solution, "expected:", expectedResult)


problemA(10, 11, 7, 4)
storageXY = {}
storageFastestWay = {}
problemA(1364, 86, 31, 39)

count = 0
for visitedPos in storageFastestWay.values():
    if visitedPos < 51:
        count += 1

print("Soution for Part B is", count)
