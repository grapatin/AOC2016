#import cmath for complex number operations
import cmath
#import Path for file operations
from pathlib import Path
import re
from typing import Counter

problemInputTxt = Path("/Users/pergrapatin/Source/AOC2016/src/day04/input.txt").read_text()

exampleInput1 = """aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]"""
exampleResult1 = 1514
regexNumbers = r"[0-9]{3}"
regexChecksum = r"[a-z]{5}]"
regexCryptoString = r"[a-z]+-"

def stringWorker(input):
    aSteps = input.split("\n")
    return aSteps

def ifValidReturnId(test_str):

    matchNumberForString = re.findall(regexNumbers, test_str)
    matchChecksum = re.findall(regexChecksum, test_str)
    matchCryptoStrings = re.findall(regexCryptoString, test_str)

    allChars = ""
    for matchNum, match in enumerate(matchCryptoStrings, start=1):
        #print ("Match {matchNum} was {match}".format(matchNum = matchNum, match = match[:-1]))
        allChars += match[:-1]

    sortedListOfAllChars = sorted(allChars)
    countDict = Counter(sortedListOfAllChars)

    #print("All chars sorted:", sortedListOfAllChars)
    #print("countDict", countDict)

    count = 0
    for x in range(5):
        maxChar = max(countDict, key = countDict.get)
        if maxChar != matchChecksum[0][x]:
            #Checksum not correct return 0
            return 0
        del countDict[maxChar]
    
    return int((matchNumberForString)[0])


def problemA(input, expectedResult):
    solution = 0

    rows = stringWorker(input)

    for row in rows:
        solution += ifValidReturnId(row)

    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)

problemA(exampleInput1, exampleResult1)
problemA(problemInputTxt, 185371)
print("\n")

def decryptRow(row):
    sectorIdArray = re.findall(regexNumbers, row)
    matchCryptoStrings = re.findall(regexCryptoString, row)

    allChars = ""
    for matchNum, match in enumerate(matchCryptoStrings, start=1):
        #print ("Match {matchNum} was {match}".format(matchNum = matchNum, match = match[:-1]))
        allChars += match[:-1]

    #Find out how many times we should rotate
    sectorId = int(sectorIdArray[0])
    rotate = sectorId % 26

    decryptedString = ""

    for char in allChars:
        aschii = ord(char) + rotate
        if aschii > ord('z'):
            aschii = ord('a') + (aschii - ord('z')-1)
        decryptedString += chr(aschii)
    return [decryptedString, sectorId]


def problemB(input, expectedResult):
    solution = 0
    rows = stringWorker(input)

    for row in rows:
        decryptedString = decryptRow(row)

        if decryptedString[0] == expectedResult:
            print("Correct solution found:", decryptedString[0], "with id:", decryptedString[1])
        #else:
        #    print("Incorrect solution, we got:", decryptedString[0])

problemB("qzmt-zixmtkozy-ivhz-343", "veryencryptedname")
problemB(problemInputTxt, "northpoleobjectstorage")
