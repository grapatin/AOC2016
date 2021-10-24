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

def problemA(input, expectedResult):
    solution = -1
    cont = True
    i = 0
    password = ""
    while cont:
        hash = hashlib.md5((input+str(i)).encode("utf-8")).hexdigest()
        if hash[0:5] == '00000': 
#            print("Hash:", hash, "i:", i)
            password += hash[5]
            if len(password) == 8:
                cont = False
        i += 1

    solution = password        
    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)

problemA("abc", "18f47a30")
problemA("abbhdwsy", "801b56a7")
print("\n")

def problemB(input, expectedResult):

    result = list("********")
    solution = -1
    cont = True
    i = 0
    password = ""
    while cont:
        hash = hashlib.md5((input+str(i)).encode("utf-8")).hexdigest()
        if hash[0:5] == '00000': 
#            print("Hash:", hash, "i:", i)
            try:
                pos = int(hash[5])
            except:
                pos = 9
            if pos < 8 and result[pos] == "*":
                result[pos] = hash[6]
#                print("resultString", result)
                if result.count("*") == 0:
                    cont = False
        i += 1

    solution = "".join(result)
    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)

problemB("abc", "05ace8e3")
problemB("abbhdwsy", "424a0197")