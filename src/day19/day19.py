#import cmath for complex number operations
from abc import abstractproperty
import cmath
#import Path for file operations
from pathlib import Path

problemInputTxt = Path("/Users/pergrapatin/Source/AOC2016/src/day19/input.txt").read_text()

exampleInput1 = """aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]"""
exampleResult1 = 1514

def stringWorker(input):
    aSteps = input.split("\n")
    return aSteps

def problemA(input, expectedResult):
    solution = -1

    elfCircle = list(range(1,input+1,2))
    currentPos = len(elfCircle) - 1 #start position is last Elf

    numberOfElfs = len(elfCircle)
    
    while(numberOfElfs > 1):
        #Remove next elf in circle 
        removeElf=  currentPos + 1
        if removeElf == numberOfElfs:
            removeElf = 0
        del elfCircle[removeElf]
        numberOfElfs -= 1
        currentPos += 1
        if currentPos >= numberOfElfs:
            currentPos = 0
        
    solution = elfCircle[0]


    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)

def problemB(numberOfElfs, expectedResult):

    elfCircle = list(range(1,numberOfElfs+1))
    currentPos = 0 #Start pos first elf
    
    while(numberOfElfs > 1):
        halfway = int(numberOfElfs/2) 
        #Remove next elf in circle 
        removeElf=  currentPos + halfway
        if removeElf >= numberOfElfs:
            removeElf = removeElf - numberOfElfs 
        #print('Removed:', elfCircle[removeElf])
        del elfCircle[removeElf]
        
        numberOfElfs -= 1

        if (removeElf > currentPos):
            currentPos += 1

        if currentPos >= numberOfElfs:
            currentPos = 0
        
    solution = elfCircle[0]


    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)



problemA(5, 3)
#problemA(3014603, 1834903)
print("\n")

problemB(5, 2)
problemB(9, 9)
problemB(3014603, 1420280)