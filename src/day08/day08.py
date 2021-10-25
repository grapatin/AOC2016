#import cmath for complex number operations
from abc import abstractproperty
import cmath
#import Path for file operations
from pathlib import Path

problemInputTxt = Path("/Users/pergrapatin/Source/AOC2016/src/day08/input.txt").read_text()

exampleInput1 = """rect 3x2
rotate column x=1 by 1
rotate row y=0 by 4
rotate column x=1 by 1"""
exampleResult1 = 1514

def stringWorker(input):
    aSteps = input.split("\n")
    return aSteps

def problemA(input, expectedResult):
    solution = -1

    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)

problemA(exampleInput1, exampleResult1)
problemA(problemInputTxt, 0)
print("\n")

