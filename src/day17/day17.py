#import cmath for complex number operations
from abc import abstractproperty
import cmath
from os import path
from pathlib import Path
import hashlib

problemInputTxt = Path("/Users/pergrapatin/Source/AOC2016/src/day17/input.txt").read_text()

exampleInput1 = """aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]"""
exampleResult1 = 1514

openDoor = 'bcdef'
shortestPathSteps = 9999999999 #Very large number 'maxInt'
longestPathSteps = 0 
shortestPath = ''

directions = [[1, 0], [-1, 0], [0, 1],[0, -1]]

def stringWorker(input):
    aSteps = input.split("\n")
    return aSteps

def hashFunction(input, hashCount = 1):
    hash = input
    for i in range(hashCount):
        hash = hashlib.md5((hash).encode("utf-8")).hexdigest()
    return hash

def walker(cX, cY, pathSoFar, seed, longestPath = False):
    tX = 4 
    tY = 4
    global shortestPathSteps, shortestPath, longestPathSteps
    hash = hashFunction(seed + pathSoFar)
    #UDLR
    if hash[0] in openDoor: #UP 
        if (cY - 1) > 0:
            if len(pathSoFar)+1 < shortestPathSteps:
                walker(cX, cY - 1, pathSoFar + 'U', seed, longestPath)
    if hash[2] in openDoor: #LEFT 
        if (cX - 1) > 0:
            if len(pathSoFar)+1 < shortestPathSteps:
                walker(cX - 1, cY, pathSoFar + 'L', seed, longestPath)
    if hash[1] in openDoor: #DOWN
        if (cY + 1) < (tY + 1):
            if ((cY + 1) == tY) and (cX == tX): #Target found
                if len(pathSoFar)+1 < shortestPathSteps and longestPath == False:
                    shortestPathSteps = len(pathSoFar+'D')
                    shortestPath = pathSoFar+'D'
                if longestPath and longestPathSteps < len(pathSoFar + 'D'):
                    longestPathSteps = len(pathSoFar + 'D')
            elif len(pathSoFar) < shortestPathSteps:
                walker(cX, cY + 1, pathSoFar + 'D', seed, longestPath)
    if hash[3] in openDoor: #RIGHT
        if (cX + 1) < (tX + 1):
            if (cY == tY) and ((cX + 1) == tX): #Target found
                if len(pathSoFar)+1 < shortestPathSteps and longestPath == False:
                    shortestPathSteps = len(pathSoFar+'R')
                    shortestPath = pathSoFar+'R'
                if longestPath and longestPathSteps < len(pathSoFar + 'R'):
                    longestPathSteps = len(pathSoFar + 'R')
            elif len(pathSoFar) < shortestPathSteps:
                walker(cX + 1, cY, pathSoFar +'R', seed, longestPath)

def problemA(input, expectedResult, maxPath = False):
    solution = -1
    walkedString = ''
    startX = 1
    startY = 1

    walker(startX, startY, walkedString, input, maxPath)
    if maxPath == False:
        solution = shortestPath
    else:
        solution = longestPathSteps
    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)

problemA('ulqzkmiv', 'DRURDRUDDLLDLUURRDULRLDUUDDDRR')
problemA('dmypynyp', 'RDRDUDLRDR')
print("\n")
shortestPathSteps = 9999999999 #Very large number 'maxInt'
longestPathSteps = 0 
shortestPath = ''
problemA('dmypynyp', 386, True)
