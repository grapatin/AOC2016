#import cmath for complex number operations
from abc import abstractproperty
import cmath
#import Path for file operations
from pathlib import Path

problemInputTxt = Path("/Users/pergrapatin/Source/AOC2016/src/day03/input.txt").read_text()

exampleInput1 = """5   10     25
23    66 78
993 003 42342"""
exampleResult1 = 1

def stringWorker(input):
    aSteps = input.split("\n")
    return aSteps

def triangle_problemA(input, expectResult):
    numberOfTriangelsFound = 0
    rows = stringWorker(input)

    for row in rows:
        #remove all white-space and get the number-strings
        numbers = row.split()
        #convert to numbers so that we can sort them
        desired_array = [int(numeric_string) for numeric_string in numbers]

        #sort array
        desired_array.sort()

        sum = desired_array[0] + desired_array[1]
        if sum > desired_array[2]:
            #This is a triange
            numberOfTriangelsFound += 1

    if numberOfTriangelsFound == expectResult:
        print("Correct number found:", numberOfTriangelsFound)
    else:
        print("Incorrect number found:", numberOfTriangelsFound, "expected:", expectResult)


triangle_problemA(exampleInput1, exampleResult1)
triangle_problemA(problemInputTxt, 862)
print("\n")


def countTriang(list):
    numberOfTriangelsFound = 0
    length = len(list)
    for x in range(int(length / 3)):
        tempArray = []
        tempArray.append(list[3*x])
        tempArray.append(list[3*x+1])
        tempArray.append(list[3*x+2])
        tempArray.sort()
        sum = tempArray[0] + tempArray[1]
        if sum > tempArray[2]:
            #This is a triange
            numberOfTriangelsFound += 1


    return numberOfTriangelsFound


def triangle_problemB(input, expectResult):
    numberOfTriangelsFound = 0
    rows = stringWorker(input)

    #create 3 new arrays an push all values into them, one by one and then to the check
    row1 = []
    row2 = []
    row3 = []

    for row in rows:
        numbers = row.split()
        row1.append(int(numbers[0]))
        row2.append(int(numbers[1]))
        row3.append(int(numbers[2]))

    numberOfTriangelsFound += countTriang(row1)
    numberOfTriangelsFound += countTriang(row2)
    numberOfTriangelsFound += countTriang(row3)

    if numberOfTriangelsFound == expectResult:
        print("Correct number found:", numberOfTriangelsFound)
    else:
        print("Incorrect number found:", numberOfTriangelsFound, "expected:", expectResult)

triangle_problemB(problemInputTxt, 1577)