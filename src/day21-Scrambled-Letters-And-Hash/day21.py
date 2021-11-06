# import cmath for complex number operations
from abc import abstractproperty
import cmath
# import Path for file operations
from pathlib import Path
from collections import deque
import itertools

problemInputTxt = Path(
    "/Users/pergrapatin/Source/AOC2016/src/day21-Scrambled-Letters-And-Hash/input.txt").read_text()

exampleInput1 = """swap position 4 with position 0
swap letter d with letter b
reverse positions 0 through 4
rotate left 1 step
move position 1 to position 4
move position 3 to position 0
rotate based on position of letter b
rotate based on position of letter d"""
exampleResult1 = 1514


def stringWorker(input):
    aSteps = input.split("\n")
    return aSteps


def swapPositions(command, scramblePasscode):
    commandParts = command.split(' ')
    pos1 = int(commandParts[2])
    pos2 = int(commandParts[-1])
    temp1 = scramblePasscode[pos1]
    temp2 = scramblePasscode[pos2]
    scramblePasscode = scramblePasscode[:pos1] + \
        temp2 + scramblePasscode[pos1+1:]
    scramblePasscode = scramblePasscode[:pos2] + \
        temp1 + scramblePasscode[pos2+1:]
    return scramblePasscode


def swapLetters(command, scramblePasscode):
    commandParts = command.split(' ')
    letter1 = commandParts[2]
    letter2 = commandParts[-1]
    letterTemp = '*'
    scramblePasscode = scramblePasscode.replace(letter1, letterTemp)
    scramblePasscode = scramblePasscode.replace(letter2, letter1)
    scramblePasscode = scramblePasscode.replace(letterTemp, letter2)

    return scramblePasscode


def reversePos(command, scramblePasscode):
    commandParts = command.split(' ')
    pos1 = int(commandParts[2])
    pos2 = int(commandParts[-1])

    temp = scramblePasscode[:pos1]

    for i in range(pos2, pos1 - 1, -1):
        temp += scramblePasscode[i]

    temp += scramblePasscode[pos2+1:]

    return temp

def rotate(command, scramblePasscode, direction):
    commandParts = command.split(' ')
    steps = int(commandParts[-2])


    items = deque(scramblePasscode)
    items.rotate(steps*direction)

    return ''.join(items) 

def movePos(command, scramblePasscode):
    commandParts = command.split(' ')
    pos1 = int(commandParts[2])
    pos2 = int(commandParts[-1])

    char = scramblePasscode[pos1]
    scramblePasscode = scramblePasscode[:pos1] + scramblePasscode[pos1+1:]


    temp = scramblePasscode[:pos2] + char + scramblePasscode[pos2:]
    return temp

def rotateBased(command, scramblePasscode):
    commandParts = command.split(' ')
    char = commandParts[-1]

    index = scramblePasscode.index(char)
    if index > 3:
        index += 1 #If index 4 or larger rotate one additional time

    items = deque(scramblePasscode)
    items.rotate(index + 1)

    return ''.join(items) 


def problemA(input, expectedResult, passcode):

    scramblingCommands = stringWorker(input)
    scramblePasscode = passcode

    for command in scramblingCommands:
        if 'swap posi' in command:
            scramblePasscode = swapPositions(command, scramblePasscode)
        elif 'swap letter' in command:
            scramblePasscode = swapLetters(command, scramblePasscode)
        elif 'reverse position' in command:
            scramblePasscode = reversePos(command, scramblePasscode)
        elif 'rotate left' in command:
            scramblePasscode = rotate(command, scramblePasscode, -1)
        elif 'rotate right' in command:
            scramblePasscode = rotate(command, scramblePasscode, 1)
        elif 'move position' in command:
            scramblePasscode = movePos(command, scramblePasscode)
        elif 'rotate based' in command:
            scramblePasscode = rotateBased(command, scramblePasscode)

    solution = scramblePasscode

    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:",
              solution, "expected:", expectedResult)


problemA(exampleInput1, 'decab', 'abcde')
problemA(problemInputTxt, 'ghfacdbe', 'abcdefgh')
print("\n")


def problemB(input, expectedResult, hashed):

    scramblingCommands = stringWorker(input)

    passcode = 'abcdefgh'

    candidates = list(itertools.permutations(passcode))
    scramblePasscode = ''
    #Try every combination abcdefgh and see what produces hashed string -> that is the password
    i = 0

    while scramblePasscode != hashed:
        scramblePasscode = ('').join(candidates[i])
        for command in scramblingCommands:
            if 'swap posi' in command:
                scramblePasscode = swapPositions(command, scramblePasscode)
            elif 'swap letter' in command:
                scramblePasscode = swapLetters(command, scramblePasscode)
            elif 'reverse position' in command:
                scramblePasscode = reversePos(command, scramblePasscode)
            elif 'rotate left' in command:
                scramblePasscode = rotate(command, scramblePasscode, -1)
            elif 'rotate right' in command:
                scramblePasscode = rotate(command, scramblePasscode, 1)
            elif 'move position' in command:
                scramblePasscode = movePos(command, scramblePasscode)
            elif 'rotate based' in command:
                scramblePasscode = rotateBased(command, scramblePasscode)
        i += 1
    
    solution = ('').join(candidates[i-1])

    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:",
              solution, "expected:", expectedResult)


#problemB(exampleInput1, 'abcde', 'decab')
problemB(problemInputTxt, 'abcdefgh', 'ghfacdbe')
problemB(problemInputTxt, 'fhgcdaeb', 'fbgdceah')
