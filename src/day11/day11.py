#import cmath for complex number operations
from abc import abstractproperty
import cmath
#import Path for file operations
from pathlib import Path

problemInputTxt = Path("/Users/pergrapatin/Source/AOC2016/src/day11/input.txt").read_text()

exampleInput1 = """The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant."""
exampleResult1 = 11

#start
#F4   
#F3  
#F2      PM           PRM            
#F1 E PG    TG TM PRG     RG RM CG CM 


#didn't solve in code was simplier to simulate on the board
#Basicall 11 steps for the first P and RPM and then 12 for each other par

def stringWorker(input):
    aSteps = input.split("\n")
    return aSteps


#Chip
#RTG
#microhhip cannot be alone with another Generator on same floor


def problemA(input, expectedResult):
    solution = 11 + 12 + 12 + 12 

    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)

problemA(exampleInput1, exampleResult1)
problemA(problemInputTxt, 47)
print("\n")

problemA(exampleInput1, exampleResult1)
problemA(problemInputTxt, 71)
print("\n")