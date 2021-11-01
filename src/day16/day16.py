#import cmath for complex number operations
from abc import abstractproperty
import cmath
#import Path for file operations
from pathlib import Path

problemInputTxt = Path("/Users/pergrapatin/Source/AOC2016/src/day16/input.txt").read_text()

exampleInput1 = """10000"""
exampleResult1 = '01100'

def dragonCurveBinary(binaryN, length):
    lengthOfString = len(binaryN)
    compS = '1'*lengthOfString
    binaryInv = int(binaryN,2) ^ int(compS,2)
    newString = binaryN + '0' + bin(binaryInv)
    return newString[:length]
    

def dragonCurve(stringA, length):
    print('Length:', len(stringA), 'left is', 35651584 - len(stringA))
    stringB = ''
    for char in stringA:
        if char == '0':
            stringB = '1' + stringB
        else:
            stringB = '0' + stringB
    
    newString = stringA + '0' + stringB

    if len(newString) < length:
        newString = dragonCurve(newString, length)

    newString = newString[:length]
    return newString

def calcChecksum(stringToCheck):
    checkSum = ''
    for i in range(int(len(stringToCheck)/2)):
        if stringToCheck[2*i] == stringToCheck[2*i+1]:
            checkSum += '1'
        else:
            checkSum += '0'

    if len(checkSum) % 2 == 0:
        checkSum = calcChecksum(checkSum) #even do a recursive call
    
    return checkSum

def problemA(input, expectedResult, length):
    solution = -1

    fullString = dragonCurve(input, length)
    solution = calcChecksum(fullString)

    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)

problemA(exampleInput1, exampleResult1, 20)
problemA(problemInputTxt, '10011010010010010', 272)
problemA(problemInputTxt, '10101011110100011', 8704) #Due to the way checksum is calculated not the full number is needed 8704 is a factor of the full length
print("\n")

