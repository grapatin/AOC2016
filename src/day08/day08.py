#import cmath for complex number operations
from abc import abstractproperty
import cmath
import copy
#import Path for file operations
from pathlib import Path

problemInputTxt = Path("/Users/pergrapatin/Source/AOC2016/src/day08/input.txt").read_text()

exampleInput1 = """rect 3x2
rotate column x=1 by 1
rotate row y=0 by 4
rotate column x=1 by 1"""
exampleResult1 = 6

def stringWorker(input):
    aSteps = input.split("\n")
    return aSteps

def performColumnC(command, matrix):
    #rotate column x=1 by 1
    parts = [s for s in command.split() if (s.isdigit() or "=" in s)]
    column = [int(s) for s in parts[0].split("=") if s.isdigit()][0]
    numberOfShifts = int(parts[1])

    for x in range(numberOfShifts):
        temp = matrix[-1][column]
        for i in range(len(matrix)):
            temp2 = matrix[i][column]
            matrix[i][column] = temp
            temp = temp2
    
    return matrix

def performRectC(command, matrix):
    # example "rect 3x2"
    commandParts = command.split();
    values = [int(s) for s in commandParts[1].split("x") if s.isdigit()]
    for w in range(values[1]):
        for h in range(values[0]):
            matrix[w][h] = 1
    return matrix

def performRowC(command, matrix):
    #rotate row x=1 by 1
    parts = [s for s in command.split() if (s.isdigit() or "=" in s)]
    row = [int(s) for s in parts[0].split("=") if s.isdigit()][0]
    numberOfShifts = int(parts[1])

    for x in range(numberOfShifts):
        temp = matrix[row][-1]
        for i in range(len(matrix[row])):
            temp2 = matrix[row][i]
            matrix[row][i] = temp
            temp = temp2
        
    return matrix

def countNumberOf1(matrix):

    count = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            print(matrix[x][y], end = '')
            if matrix[x][y] == 1:
                count += 1
        print('') #new line
    return count

def problemA(input, expectedResult, w, h):
    solution = 0
    matrix = [[0 for x in range(w)] for y in range(h)] 

    commands = stringWorker(input)
    for command in commands:
        if "rect" in command:
            matrix = performRectC(command, matrix)
        elif "row" in command:
            performRowC(command, matrix)
        elif "column" in command:
            performColumnC(command, matrix)
        else:
            print("Error unexpected command")

    solution = countNumberOf1(matrix)

    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)

problemA(exampleInput1, exampleResult1, 7, 3)
problemA(problemInputTxt, 0, 50, 6)
print("\n")

