#import cmath for complex number operations
from abc import abstractproperty
import cmath
#import Path for file operations
from pathlib import Path

problemInputTxt = Path("/Users/pergrapatin/Source/AOC2016/src/day10/input.txt").read_text()

exampleInput1 = """value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2"""
exampleResult1 = 2

storageDict = {}

def stringWorker(input):
    aSteps = input.split("\n")
    return aSteps

class microBot:
    def __init__(self, botId):
        self.botId = botId
        self.chipA = None
        self.chipB = None
        self.giveLowToId = None
        self.giveLowToOutput = False
        self.giveHighToId = None
        self.giveHighToOutput = False

    def addChip(self, chipId):
        if self.chipA == None:
            self.chipA = chipId
        elif self.chipB == None:
            self.chipB = chipId
        else:
            assert False, 'Unexped value'

    def setLowRule(self, botId):
        self.giveLowToId = botId
    
    def setHighRule(self, botId):
        self.giveHighToId = botId


    def performAction(self, valueA, valueB):
        if self.chipA != None and self.chipB != None:
            #2 values exist
            if (self.chipA == valueA and self.chipB == valueB) or (self.chipA == valueB and self.chipB == valueA):
                print('Solution is found: ', self.botId)
            if self.chipA < self.chipB:
                if self.giveLowToOutput != True:
                    storageDict[self.giveLowToId].addChip(self.chipA)
                else:
                    print('output:', self.giveLowToId, 'has value:', self.chipA)
                self.chipA = None

                if self.giveHighToOutput != True:
                    storageDict[self.giveHighToId].addChip(self.chipB)
                else:
                    print('output:', self.giveHighToId, 'has value:', self.chipB)
                self.chipB = None
            else:
                if self.giveLowToOutput != True:
                    storageDict[self.giveLowToId].addChip(self.chipB)
                else:
                    print('output:', self.giveLowToId, 'has value:', self.chipB)
                
                self.chipB = None
                if self.giveHighToOutput != True:
                    storageDict[self.giveHighToId].addChip(self.chipA)
                else:
                    print('output:', self.giveHighToId, 'has value:', self.chipA)                    
                self.chipA = None
 

def problemA(input, expectedResult, valueA, valueB):
    solution = -1

    rows = stringWorker(input)
    #Algo
    #Create class, that can store 2 values and a command, when storing check if we have a target match
    #if we have print a match
    #Store class in a dict based in id
    #Alwas check in dict if class exists before creating a new class
    #Go through each input line and add to classes
    for row in rows:
        if 'value' in row:
            #parse out value (first value) and botId second value
            parsedInts = [int(s) for s in row.split() if s.isdigit()]
            mBotId = parsedInts[1]
            value = parsedInts[0]

            if mBotId in storageDict:
                mBot = storageDict[mBotId]
                mBot.addChip(value)
            else:
                mBot = microBot(mBotId)
                mBot.addChip(value)
                storageDict[mBotId] = mBot
        else:
            #parse output botId, whereLow and whereHigh but we need to find out if
            #target is another bot or a output
            parsedInts = [int(s) for s in row.split() if s.isdigit()]
            mBotId = parsedInts[0]    
            whereLow = parsedInts[1]
            whereHigh = parsedInts[2]
            if mBotId in storageDict:
                mBot = storageDict[mBotId]
                if 'output' in row[:30]:
                    mBot.giveLowToOutput = True
                if 'output' in row[-15:]:
                    mBot.giveLowToOutput = True
                mBot.setLowRule(whereLow)
                mBot.setHighRule(whereHigh)
            else:
                mBot = microBot(mBotId)
                if 'output' in row[:30]:
                    mBot.giveLowToOutput = True
                if 'output' in row[-15:]:
                    mBot.giveLowToOutput = True
                mBot.setLowRule(whereLow)
                mBot.setHighRule(whereHigh)
                storageDict[mBotId] = mBot


    for i in range(100):
        for mBot in storageDict.values():
            mBot.performAction(valueA, valueB)

    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)

problemA(exampleInput1, exampleResult1, 5, 2)
problemA(problemInputTxt, 0, 61, 17)
print("\n")

