#import cmath for complex number operations
from abc import abstractproperty
import cmath
#import Path for file operations
from pathlib import Path

problemInputTxt = Path("/Users/pergrapatin/Source/AOC2016/src/day07/input.txt").read_text()

exampleInput1 = """abba[mnop]qrst
abcd[bddb]xyyx
aaaa[qwer]tyui
ioxxoj[asdfgh]zxcvbn"""
exampleResult1 = 2

def stringWorker(input):
    aSteps = input.split("\n")
    return aSteps

def problemA(input, expectedResult):
    solution = 0
    #Algo v2
    #Walk through string disqualify any strings that has a ABBA followed by a ]
    rows = stringWorker(input)
    for row in rows:
        abbaFound = False
        abbaConfirmed = False
        abbaInvalid = False;
        length = len(row)
        for x in range(length):
            if x < (length - 3): #Make sure to stop in time
                if row[x] == row[x+3] and row[x+1] == row[x+2]:
                    if row[x] != row[x+1]:
                        abbaFound = True
                if row[x] == ']' and abbaFound == True:
                    #Abba was within a hypernet sequence abort string
                    abbaInvalid = True
                    abbaConfirmed = False
                    abbaFound = False
                    break
                if row[x] == '[' and abbaFound == True: #abba valid
                    abbaConfirmed = True
                    abbaFound = False    
        if (abbaConfirmed == True or abbaFound == True) and abbaInvalid == False:
            #Valid abba
            solution += 1

    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)

problemA(exampleInput1, exampleResult1)
problemA(problemInputTxt, 115)
print("\n")

def searchForWithinBrackets(row, findMe):
    withingBrackets = False
    for x in range(len(row) - 2):
        if row[x] == "[":
            #within bracket
            withingBrackets = True
        elif row[x] == "]":
            #outside bracket
            withingBrackets = False
        elif withingBrackets == True and findMe[0] == row[x] and findMe[1] == row[x+1] and findMe[2] == row[x+2]:
            #we got a hit
            return True
    #No hit found
    return False    

def problemB(input, expectedResult):
    solution = 0
    #Algo
    #Walk through string find matches, then look inside the brackets for matches

    rows = stringWorker(input)
    for row in rows:
        insideBracket = False
        length = len(row)
        for x in range(length - 2):
            if row[x] == "[":
                insideBracket = True
            elif row[x] == ']':
                insideBracket = False
            elif insideBracket == False and row[x] == row[x+2] and (row[x+1] != "[" or row[x+1] != "]"):
                if row[x] != row[x+1]:
                    #now search through same string trying to find within brackats
                    if searchForWithinBrackets(row, row[x+1]+row[x]+row[x+1]) == True:
                        #proper match found
                        solution += 1
                        break

    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)

problemB("""aba[bab]xyz
xyx[xyx]xyx
aaa[kek]eke
zazbz[bzb]cdb""", 3)
problemB(problemInputTxt, 231)
print("\n")
