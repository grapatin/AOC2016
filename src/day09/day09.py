#import cmath for complex number operations
from abc import abstractproperty
import cmath
#import Path for file operations
from pathlib import Path

problemInputTxt = Path("/Users/pergrapatin/Source/AOC2016/src/day09/input.txt").read_text()

def stringWorker(input):
    aSteps = input.split("\n")
    return aSteps

def problemA(input, expectedResult):
    solution = ""

    leftP = -1
    rightP = -1
    withinP = False
    done = False
    i = 0
    while (not done):
        #Algo
        #Copy char to new string until ( found then parse that command and continue at correct pos and repeat until done
        if input[i] == '(':
            leftP = i
            withinP = True;
        elif input[i] == ')':
            rightP = i
            withinP = False;
            #process command!
            commandString = input[leftP+1:rightP] #remove ()
            params = commandString.split('x')
            numberOfChars = int(params[0])
            multiTimes = int(params[1])
            for x in range(multiTimes):
                solution += input[rightP+1:rightP+1+numberOfChars]
            i = i + numberOfChars
        elif withinP == False:
            solution += input[i]
        if (i >= len(input) - 1):
            done = True
        i += 1

    if len(solution) == expectedResult:
        print("Correct solution found:", len(solution))
    else:
        print("Incorrect solution, we got:", len(solution), "expected:", expectedResult)

problemA("X(8x2)(3x3)ABCY", 18)
problemA(problemInputTxt, 123908)
print("\n")

def countCharsRecursive(input):
    count = 0
    i = 0
    leftP = -1
    rightP = -1
    done = False
    withinP = False
    while (not done):
        #Algo
        #Copy char to new string until ( found then parse that command and continue at correct pos and repeat until done
        if input[i] == '(':
            leftP = i
            withinP = True
        elif input[i] == ')':
            rightP = i
            withinP = False;
            #process command!
            commandString = input[leftP+1:rightP] #remove ()
            params = commandString.split('x')
            numberOfChars = int(params[0])
            multiTimes = int(params[1])
            count += multiTimes*countCharsRecursive(input[i+1:i+numberOfChars+1])
            i += numberOfChars
        elif withinP == False:
            #ordinary char
            count += 1 
        if (i >= len(input) - 1):
            done = True
        i += 1
    return count
    
def problemB(input, expectedResult):
    count = 0
    count = countCharsRecursive(input)
    
    if count == expectedResult:
        print("Correct solution found:", count)
    else:
        print("Incorrect solution, we got:", count, "expected:", expectedResult)

problemB("X(8x2)(3x3)ABCY", 20)
problemB(problemInputTxt, 0)
print("\n")
