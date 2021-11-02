#import cmath for complex number operations
from abc import abstractproperty
import cmath
#import Path for file operations
from pathlib import Path

problemInputTxt = Path("/Users/pergrapatin/Source/AOC2016/src/day18/input.txt").read_text()

exampleInput1 = """.^^.^.^^^^"""
exampleResult1 = 38

def stringWorker(input):
    aSteps = input.split("\n")
    return aSteps

def problemA(input, expectedResult, numberOfRows):
    solution = -1

    rows = input
    previousRow = input
    currentRow = ''
    for rowNumber in range(1, numberOfRows):
        center = '.'
        for l in range(len(input)):
            left = center
            center = previousRow[l]
            if l + 1 < len(input):
                right = previousRow[l+1]
            else:
                right = '.'

            if left == '^' and center == '^' and right == '.':
                currentRow += '^'
            elif left == '.' and center == '^' and right == '^':
                currentRow += '^'
            elif left == '^' and center == '.' and right == '.':
                currentRow += '^'
            elif left == '.' and center == '.' and right == '^':
                currentRow += '^'
            else:
                currentRow += '.'
        previousRow = currentRow
        rows = rows + '\n' + currentRow
        currentRow = ''

    solution = rows.count('.')

    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)

problemA(exampleInput1, exampleResult1, 10)
problemA(problemInputTxt, 1939, 40)
print("\n")

problemA(problemInputTxt, 19999535, 400000)
