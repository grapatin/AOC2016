#import cmath for complex number operations
from abc import abstractproperty
import cmath
#import Path for file operations
from pathlib import Path

problemInputTxt = Path("/Users/pergrapatin/Source/AOC2016/src/day20-Firewall-Rules/input.txt").read_text()

exampleInput1 = """5-8
0-2
4-7"""
exampleResult1 = 1514

def stringWorker(input):
    aSteps = input.split("\n")
    return aSteps

def problemA(input, expectedResult, maxValue):
    solution = -1
    rows = stringWorker(input)
    numberArray = []

    for row in rows:
        numberArray.append([int(row.split('-')[0]),int(row.split('-')[1])])
    numberArray.sort()
    stop = 0
    for nArray in numberArray:
        if (stop+1) < nArray[0]:
            solution = stop+1
            break;
        if (stop < nArray[1]):
            stop = nArray[1]
    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)

problemA(exampleInput1, 3, 9)
problemA(problemInputTxt, 17348574, 4294967295)
print("\n")

def problemB(input, expectedResult, maxValue):
    solution = -1
    rows = stringWorker(input)
    numberArray = []
    counter = 0

    for row in rows:
        numberArray.append([int(row.split('-')[0]),int(row.split('-')[1])])
    numberArray.sort()
    stop = 0
    for nArray in numberArray:
        if (stop+1) < nArray[0]:
            counter = counter + (nArray[0] - (stop+1))
        if (stop < nArray[1]):
            stop = nArray[1]
    counter += maxValue - stop

    solution = counter
    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)

problemB(exampleInput1, 2, 9)
problemB(problemInputTxt, 104, 4294967295)