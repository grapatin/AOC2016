#import cmath for complex number operations
from abc import abstractproperty
import cmath
#import Path for file operations
from pathlib import Path
import hashlib

problemInputTxt = Path("/Users/pergrapatin/Source/AOC2016/src/day05/input.txt").read_text()

def stringWorker(input):
    aSteps = input.split("\n")
    return aSteps

charsToSearchFor = '0123456789abcdef'


def hashFunction(input, hashCount):
    hash = input
    for i in range(hashCount):
        hash = hashlib.md5((hash).encode("utf-8")).hexdigest()
    return hash

def findKeys(input, hashCount = 1):
    numberFound = 0
    hashesStrings = []
    for i in range(30000): 
        hash = hashFunction(input+str(i), hashCount)
        hashesStrings.append(hash)

    #First find 3 in a row then check for the next 1000 to see if we can find 5 in a row
    for i in range(30000):
        hash = hashesStrings[i]
        keyUsed = False
        for l in range(len(hash)-2):
                if (hash[l] == hash[l+1] and hash[l] == hash[l+2] and keyUsed == False):
                    keyUsed = True
                    char = hash[l]
                    findString = char + char + char + char + char
                    for k in range(999):
                        newHash = hashesStrings[i + 1 + k]
                        if findString in newHash:
                            numberFound += 1
                            #print('Hit found', numberFound, newHash, i+1+k, "org hash", hash, "at integer", i)
                            if numberFound == 64:
                                return i
                            break
                
def problemA(input, expectedResult):
    solution = -1
    solution = findKeys(input)  
    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)

problemA("abc", 22728)
problemA('yjdafjpo', 25427)
print("\n")

def problemB(input, expectedResult):
    solution = -1
    solution = findKeys(input, 2017)  
    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)

problemB("abc", 22551)
problemB('yjdafjpo', 22045)
print("\n")
