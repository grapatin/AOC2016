#import cmath for complex number operations
from abc import abstractproperty
import cmath
#import Path for file operations
from pathlib import Path
from typing import Counter

problemInputTxt = Path("/Users/pergrapatin/Source/AOC2016/src/day06/input.txt").read_text()

exampleInput1 = """eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar"""
exampleResult1 = "easter"

def stringWorker(input):
    aSteps = input.split("\n")
    return aSteps

def problemA(input, expectedResult):
    rows = stringWorker(input)

    numberCollumns = len(rows[0])
    message = ""

    for i in range(numberCollumns):
        tempArray = []
        for row in rows:
            tempArray.append(row[i])
        dDict = Counter(tempArray)
        temp = max(dDict, key = dDict.get)
        message += temp

    if message == expectedResult:
        print("Correct solution found:", message)
    else:
        print("Incorrect solution, we got:", message, "expected:", expectedResult)

def problemB(input, expectedResult):
    rows = stringWorker(input)

    numberCollumns = len(rows[0])
    message = ""

    for i in range(numberCollumns):
        tempArray = []
        for row in rows:
            tempArray.append(row[i])
        dDict = Counter(tempArray)
        temp = min(dDict, key = dDict.get)
        message += temp

    if message == expectedResult:
        print("Correct solution found:", message)
    else:
        print("Incorrect solution, we got:", message, "expected:", expectedResult)


problemA(exampleInput1, exampleResult1)
problemA(problemInputTxt, "mlncjgdg")

problemB(exampleInput1, "advent")
problemB(problemInputTxt, "bipjaytb")
print("\n")

