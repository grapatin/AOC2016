#import cmath for complex number operations
import cmath


exampleInput1 = "R2, L3"
exampleResult1 = 5
exampleInput2 = "R2, R2, R2"
exampleResult2 = 2
exampleInput3 = "R5, L5, R5, R3"
exampleResult3 = 12

realInput = "R3, L5, R1, R2, L5, R2, R3, L2, L5, R5, L4, L3, R5, L1, R3, R4, R1, L3, R3, L2, L5, L2, R4, R5, R5, L4, L3, L3, R4, R4, R5, L5, L3, R2, R2, L3, L4, L5, R1, R3, L3, R2, L3, R5, L194, L2, L5, R2, R1, R1, L1, L5, L4, R4, R2, R2, L4, L1, R2, R53, R3, L5, R72, R2, L5, R3, L4, R187, L4, L5, L2, R1, R3, R5, L4, L4, R2, R5, L5, L4, L3, R5, L2, R1, R1, R4, L1, R2, L3, R5, L4, R2, L3, R1, L4, R4, L1, L2, R3, L1, L1, R4, R3, L4, R2, R5, L2, L3, L3, L1, R3, R5, R2, R3, R1, R2, L1, L4, L5, L2, R4, R5, L2, R4, R4, L3, R2, R1, L4, R3, L3, L4, L3, L1, R3, L2, R2, L4, L4, L5, R3, R5, R3, L2, R5, L2, L1, L5, L1, R2, R4, L5, R2, L4, L5, L4, L5, L2, L5, L4, R5, R3, R2, R2, L3, R3, L2, L5"

def stringWorker(input):
    aSteps = input.split(", ")
    return aSteps


def walker(input, expected):
    #We start at origo
    x = 0
    y = 0
    iCurrentPos = complex(x,y)
    #Direction we are facing is north
    direction = complex(0,1)
    iR = complex(0,-1)
    iL = complex(0, 1)

    aSteps = stringWorker(input)
    for step in aSteps:
        if step[0] == "R":
            direction = direction * iR
        else:
            direction = direction * iL
        iCurrentPos = iCurrentPos + direction*int(step[1:])

    dist = abs(iCurrentPos.imag) + abs(iCurrentPos.real)
    if dist == expected:
        print("Correct total distance: ", dist)
    else:
        print("Expected: ", expected, "but got: ", dist)


walker(exampleInput1, exampleResult1)
walker(exampleInput2, exampleResult2)
walker(exampleInput3, exampleResult3)
walker(realInput, 236)

print("\n")

def walker2(input, expected):
    #We start at origo
    x = 0
    y = 0
    iCurrentPos = complex(x,y)
    complexString = str(iCurrentPos.real)+"+"+str(iCurrentPos.imag)
    dDict = {complexString: 1}
    #Direction we are facing is north
    direction = complex(0,1)
    iR = complex(0,-1)
    iL = complex(0, 1)

    aSteps = stringWorker(input)
    for step in aSteps:
        if step[0] == "R":
            direction = direction * iR
        else:
            direction = direction * iL
        
        numberOfSteps = int(step[1:])
        i = 0
        while i < numberOfSteps:
            iCurrentPos = iCurrentPos + direction
            complexString = str(iCurrentPos.real)+"+"+str(iCurrentPos.imag)

            if complexString in dDict:
                break #same position visited twice
            dDict[complexString] = 1
            i += 1
        if i < numberOfSteps:
            break #Break also the other of loop

    dist = abs(iCurrentPos.imag) + abs(iCurrentPos.real)
    if dist == expected:
        print("B: Correct total distance: ", dist)
    else:
        print("B: Expected: ", expected, "but got: ", dist)

walker2("R8, R4, R4, R8", 4)
walker2(realInput, 182)







