#import cmath for complex number operations
from abc import abstractproperty
import cmath
import copy
from os import curdir
import sys
import itertools
#import Path for file operations
from pathlib import Path

problemInputTxt = Path("/Users/pergrapatin/Source/AOC2016/src/day24-Air-Duct-Spelunking/input.txt").read_text()

exampleInput1 = """###########
#0.1.....2#
#.#######.#
#4.......3#
###########"""
exampleResult1 = 14

def stringWorker(input):
    aSteps = input.split("\n")
    return aSteps

def create2dArrayFromString(input):
    input = input + '\n'
    x = 0
    y = 0
    maze = []
    row = []
    for char in input:
        if char != '\n':
            row.append(char)
        else:
            maze.append(row)
            row = []
    return maze



class mazeWalker:
    def __init__(self, maze2d):
        self.maze2d = copy.deepcopy(maze2d)
        self.directions = [1, 0], [0, -1], [0, 1], [-1, 0]
        self.bestDistance = 300 #We know the longest distance is about 282

    def checkDistance(self, X, Y, distance):
        if isinstance(self.maze2d[Y][X], str): #First time visiting
            self.maze2d[Y][X] = distance
            return True
        else:                
            if self.maze2d[Y][X] > distance:
                #new shortest path found
                self.maze2d[Y][X] = distance
                return True
            else:
                #Longer than previous attempt
                return False


    def walkMaze(self, startX, startY, reachX, reachY):
        self.nextStep(
            startX, startY, reachX, reachY, 0
        )
        return self.maze2d[reachY][reachX]
    
    def nextStep(self, currX, currY, reachX, reachY, distanceTraveled):
        for i in range(4):
            tX = currX + self.directions[i][0]
            tY = currY + self.directions[i][1]
            newDistanceTravaled = distanceTraveled + 1

            if tX == reachX and tY == reachY:
                if self.checkDistance(tX, tY, newDistanceTravaled) == True:
                    self.bestDistance = newDistanceTravaled
            elif self.maze2d[tY][tX] != '#': #Not a wall continue
                if self.checkDistance(tX, tY, newDistanceTravaled) == True:
                    if newDistanceTravaled < (self.bestDistance - 1): 
                        self.nextStep(tX, tY, reachX, reachY, newDistanceTravaled)


def positionOfIn(findChar, maze2d):
    for indxY, row in enumerate(maze2d):
        for indxX, char in enumerate(row):
            if char == findChar:
                return indxX, indxY
    assert(True) #should not happen

        
def problemA(input, expectedResult, itemToFind, problemB = False):
    steps = 0
    storage = {}
    #1. create 2-array from input
    maze = create2dArrayFromString(input)

    #2. calculate min distance from each number to other numbers within reach
    for i in itemToFind:
        for l in itemToFind:
            if l != i:
                startX, startY = positionOfIn(i, maze)
                findX, findY = positionOfIn(l, maze)
                mWalker = mazeWalker(maze)
                distance = mWalker.walkMaze(startX, startY, findX, findY)
                storage[i+'-'+l] = distance
                print('Found distance between', i,'and', l,':', distance)
    
    differentCombinations = list(itertools.permutations(itemToFind[1:]))

    if problemB == True:
        differentCombinations = [('').join(comb)+'0' for comb in differentCombinations]



    shortestDistance = 90000000 #maxInt fake
    for order in differentCombinations:
        current = '0'
        distance = 0
        for next in order:
            distance += storage[current+'-'+next]
            current = next
        if distance < shortestDistance:
            shortestDistance = distance

    #3. Find shortest path to visit all
    solution = shortestDistance

    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)

print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
problemA(exampleInput1, exampleResult1, '01234')
problemA(problemInputTxt, 430, '01234567')

problemA(exampleInput1, 20, '01234', True)
problemA(problemInputTxt, 430, '01234567', True)
print("\n")

