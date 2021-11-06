#import cmath for complex number operations
from abc import abstractproperty
import cmath
#import Path for file operations
from pathlib import Path

problemInputTxt = Path("/Users/pergrapatin/Source/AOC2016/src/day25-Clock-Signal/input.txt").read_text()

exampleInput1 = """cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a"""
exampleResult1 = 1514

class bunnyMC:
    def __init__(self, codeArray):
        self.regDict = {
            'a': 7,
            'b': 0,
            'c': 0,
            'd': 0
        }
        self.pc = 0
        self.codeArray = codeArray
        self.length = len(codeArray)
        self.output = 1

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
        if rel in self.regDict:
            rel = self.regDict[rel]
        if check in self.regDict:
            if (self.regDict[check] == 0):
                self.pc += 1
                return  # No jump since 0
        else:
            if int(check) == 0:
                self.pc += 1
                return  # No jump since 0
        self.pc += int(rel)

    def tgl(self, codeString):
        codeparts = codeString.split(' ')
        rel = self.regDict[codeparts[1]]
        lineNumber = self.pc + rel
        if (lineNumber >= 0) and (lineNumber < self.length):
            #valid lineNumber
            commandAtLine = self.codeArray[lineNumber]
            if 'cpy' in commandAtLine:
                #2 param command
                self.codeArray[lineNumber] = self.codeArray[lineNumber].replace('cpy', 'jnz')
            elif 'inc' in commandAtLine:
                self.codeArray[lineNumber] = self.codeArray[lineNumber].replace('inc', 'dec')
            elif 'dec' in commandAtLine:
                self.codeArray[lineNumber] = self.codeArray[lineNumber].replace('dec', 'inc')
            elif 'jnz' in commandAtLine:
                self.codeArray[lineNumber] = self.codeArray[lineNumber].replace('jnz', 'cpy')
            elif 'tgl' in commandAtLine:
                self.codeArray[lineNumber] = self.codeArray[lineNumber].replace('tgl', 'inc')
            else:
                assert False  # Unexpected command recivied
        self.pc += 1

    def out(self, codeString):
        codeparts = codeString.split(' ')
        clock = self.regDict[codeparts[1]]
        if (clock == self.output) or (clock > 1) or clock < 0:
            #Not correct clock
            assert(False)
        self.output = clock 
        #print('clock:', clock) 
        self.pc += 1

    def execute(self, codeString):
        #print('PC:', self.pc, 'Command:', codeString, end='')
        if 'cpy' in codeString:
            self.cpy(codeString)
        elif 'inc' in codeString:
            self.inc(codeString)
        elif 'dec' in codeString:
            self.dec(codeString)
        elif 'jnz' in codeString:
            self.jnz(codeString)
        elif 'tgl' in codeString:
            self.tgl(codeString)
        elif 'nop' in codeString:
            self.pc += 1
        elif 'out' in codeString:
            self.out(codeString)
        else:
            assert False  # Unexpected command recivied
        #print(' a:', self.regDict['a'],'b:', self.regDict['b'], 'c:', self.regDict['c'], 'd', self.regDict['d'])

def stringWorker(input):
    aSteps = input.split("\n")
    return aSteps

def problemA(input, expectedResult):
    
    codeArray = stringWorker(input)
    microController = bunnyMC(codeArray)
    solution = 0

    for i in range(100, 1000):
        microController = bunnyMC(codeArray)
        microController.regDict['a'] = i
        try:
            k = 0
            while microController.pc < len(codeArray):
                microController.execute(microController.codeArray[microController.pc])
                k += 1
                if k > 100000:
                    solution = i
                    if solution == expectedResult:
                        print("Correct solution found:", solution)
                    else:
                        print("Incorrect solution, we got:", solution, "expected:", expectedResult)
                    return
        except:
            pass
            #print('not valid:', i)

problemA(problemInputTxt, 180)
print("\n")

