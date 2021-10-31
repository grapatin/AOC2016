# import cmath for complex number operations
from abc import abstractproperty
import cmath
# import Path for file operations
from pathlib import Path

problemInputTxt = Path(
    "/Users/pergrapatin/Source/AOC2016/src/day12/input.txt").read_text()

exampleInput1 = """cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a"""
exampleResult1 = 42


class bunnyMC:
    def __init__(self, problemB=False):
        self.regDict = {
            'a': 0,
            'b': 0,
            'c': 0,
            'd': 0
        }
        self.pc = 0
        if (problemB == True):
            self.regDict['c'] = 1

    def cpy(self, codeString):
        codeparts = codeString.split(' ')
        src = codeparts[1]
        dst = codeparts[2]
        if src in self.regDict:
            self.regDict[dst] = self.regDict[src]
        else:
            self.regDict[dst] = int(src)
        self.pc += 1

    def inc(self, codeString):
        codeparts = codeString.split(' ')
        reg = codeparts[1]
        self.regDict[reg] += 1
        self.pc += 1

    def dec(self, codeString):
        codeparts = codeString.split(' ')
        reg = codeparts[1]
        self.regDict[reg] -= 1
        self.pc += 1

    def jnz(self, codeString):
        codeparts = codeString.split(' ')
        check = codeparts[1]
        rel = codeparts[2]
        if check in self.regDict:
            if (self.regDict[check] == 0):
                self.pc += 1
                return  # No jump since 0
        else:
            if check == 0:
                self.pc += 1
                return  # No jump since 0
        self.pc += int(rel)

    def execute(self, codeString):
        if 'cpy' in codeString:
            self.cpy(codeString)
        elif 'inc' in codeString:
            self.inc(codeString)
        elif 'dec' in codeString:
            self.dec(codeString)
        elif 'jnz' in codeString:
            self.jnz(codeString)
        else:
            assert False  # Unexpected command recivied


def stringWorker(input):
    aSteps = input.split("\n")
    return aSteps


def problemA(input, expectedResult):
    solution = 0

    linesOfCode = stringWorker(input)

    microController = bunnyMC()

    while microController.pc < len(linesOfCode):
        microController.execute(linesOfCode[microController.pc])

    solution = microController.regDict['a']

    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:",
              solution, "expected:", expectedResult)


problemA(exampleInput1, exampleResult1)
problemA(problemInputTxt, 318083)
print("\n")

def problemB(input, expectedResult):
    solution = 0

    linesOfCode = stringWorker(input)

    microController = bunnyMC(True)

    while microController.pc < len(linesOfCode):
        microController.execute(linesOfCode[microController.pc])

    solution = microController.regDict['a']

    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:",
              solution, "expected:", expectedResult)

problemB(problemInputTxt, 9227737)
