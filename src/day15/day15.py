#import cmath for complex number operations
from abc import abstractproperty
import cmath
#import Path for file operations
from pathlib import Path

problemInputTxt = Path("/Users/pergrapatin/Source/AOC2016/src/day15/input.txt").read_text()

exampleInput1 = """Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 2 positions; at time=0, it is at position 1."""
exampleResult1 = 1514

def stringWorker(input):
    aSteps = input.split("\n")
    return aSteps

def problemA(input, expectedResult):
    solution = 0

    discs = []

    rows = stringWorker(input)
    for txt in rows:
        txt = txt.replace('#', ' ')
        txt = txt.replace('=', ' ')
        txt = txt.replace('.', ' ')
        ints = [int(s) for s in txt.split() if s.isdigit()]
        discs.append(ints)

    solutionNotFound = True
    t = 0
    multiplier = 1
    while solutionNotFound:
        solutionNotFound = False
        for disc in discs:
            currentRotation = disc[2] + t + disc[0] + 1 #Start Position, current time, fall time (+1)
            if currentRotation % disc[1] == 0: #Ball will fall through
                continue
            else:
                solutionNotFound = True
                break        
        t += 1*multiplier

    solution = t
    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)

problemA(exampleInput1, 5)
problemA(problemInputTxt, 16824)
print("\n")

def problemB(input, expectedResult):
    solution = 0

    discs = []

    input += '\nDisc #7 has 11 positions; at time=0, it is at position 0.'
    rows = stringWorker(input)
    for txt in rows:
        txt = txt.replace('#', ' ')
        txt = txt.replace('=', ' ')
        txt = txt.replace('.', ' ')
        ints = [int(s) for s in txt.split() if s.isdigit()]
        discs.append(ints)

    solutionNotFound = True
    t = 0
    multiplier = 1
    while solutionNotFound:
        solutionNotFound = False
        for disc in discs:
            currentRotation = disc[2] + t + disc[0] + 1 #Start Position, current time, fall time (+1)
            if currentRotation % disc[1] == 0: #Ball will fall through
                continue
            else:
                solutionNotFound = True
                break        
        t += 1*multiplier

    solution = t
    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)

problemB(problemInputTxt, 3543984)


