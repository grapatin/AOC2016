#import cmath for complex number operations
import cmath


exampleInput1 = """ULL
RRDDD
LURDL
UUUUD"""
exampleResult1 = "1985"

realInput = """LURLDDLDULRURDUDLRULRDLLRURDUDRLLRLRURDRULDLRLRRDDULUDULURULLURLURRRLLDURURLLUURDLLDUUDRRDLDLLRUUDURURRULURUURLDLLLUDDUUDRULLRUDURRLRLLDRRUDULLDUUUDLDLRLLRLULDLRLUDLRRULDDDURLUULRDLRULRDURDURUUUDDRRDRRUDULDUUULLLLURRDDUULDRDRLULRRRUUDUURDULDDRLDRDLLDDLRDLDULUDDLULUDRLULRRRRUUUDULULDLUDUUUUDURLUDRDLLDDRULUURDRRRDRLDLLURLULDULRUDRDDUDDLRLRRDUDDRULRULULRDDDDRDLLLRURDDDDRDRUDUDUUDRUDLDULRUULLRRLURRRRUUDRDLDUDDLUDRRURLRDDLUUDUDUUDRLUURURRURDRRRURULUUDUUDURUUURDDDURUDLRLLULRULRDURLLDDULLDULULDDDRUDDDUUDDUDDRRRURRUURRRRURUDRRDLRDUUULLRRRUDD
DLDUDULDLRDLUDDLLRLUUULLDURRUDLLDUDDRDRLRDDUUUURDULDULLRDRURDLULRUURRDLULUDRURDULLDRURUULLDLLUDRLUDRUDRURURUULRDLLDDDLRUDUDLUDURLDDLRRUUURDDDRLUDDDUDDLDUDDUUUUUULLRDRRUDRUDDDLLLDRDUULRLDURLLDURUDDLLURDDLULLDDDRLUDRDDLDLDLRLURRDURRRUDRRDUUDDRLLUDLDRLRDUDLDLRDRUDUUULULUDRRULUDRDRRLLDDRDDDLULURUURULLRRRRRDDRDDRRRDLRDURURRRDDULLUULRULURURDRRUDURDDUURDUURUURUULURUUDULURRDLRRUUDRLLDLDRRRULDRLLRLDUDULRRLDUDDUUURDUDLDDDUDL
RURDRUDUUUUULLLUULDULLLDRUULURLDULULRDDLRLLRURULLLLLLRULLURRDLULLUULRRDURRURLUDLULDLRRULRDLDULLDDRRDLLRURRDULULDRRDDULDURRRUUURUDDURULUUDURUULUDLUURRLDLRDDUUUUURULDRDUDDULULRDRUUURRRDRLURRLUUULRUDRRLUDRDLDUDDRDRRUULLLLDUUUULDULRRRLLRLRLRULDLRURRLRLDLRRDRDRLDRUDDDUUDRLLUUURLRLULURLDRRULRULUDRUUURRUDLDDRRDDURUUULLDDLLDDRUDDDUULUDRDDLULDDDDRULDDDDUUUURRLDUURULRDDRDLLLRRDDURUDRRLDUDULRULDDLDDLDUUUULDLLULUUDDULUUDLRDRUDLURDULUDDRDRDRDDURDLURLULRUURDUDULDDLDDRUULLRDRLRRUURRDDRDUDDLRRLLDRDLUUDRRDDDUUUDLRRLDDDUDRURRDDUULUDLLLRUDDRULRLLLRDLUDUUUUURLRRUDUDDDDLRLLULLUDRDURDDULULRDRDLUDDRLURRLRRULRL
LDUURLLULRUURRDLDRUULRDRDDDRULDLURDDRURULLRUURRLRRLDRURRDRLUDRUUUULLDRLURDRLRUDDRDDDUURRDRRURULLLDRDRDLDUURLDRUULLDRDDRRDRDUUDLURUDDLLUUDDULDDULRDDUUDDDLRLLLULLDLUDRRLDUUDRUUDUDUURULDRRLRRDLRLURDRURURRDURDURRUDLRURURUUDURURUDRURULLLLLUDRUDUDULRLLLRDRLLRLRLRRDULRUUULURLRRLDRRRDRULRUDUURRRRULDDLRULDRRRDLDRLUDLLUDDRURLURURRLRUDLRLLRDLLDRDDLDUDRDLDDRULDDULUDDLLDURDULLDURRURRULLDRLUURURLLUDDRLRRUUDULRRLLRUDRDUURLDDLLURRDLRUURLLDRDLRUULUDURRDULUULDDLUUUDDLRRDRDUDLRUULDDDLDDRUDDD
DRRDRRURURUDDDRULRUDLDLDULRLDURURUUURURLURURDDDDRULUDLDDRDDUDULRUUULRDUDULURLRULRDDLDUDLDLULRULDRRLUDLLLLURUDUDLLDLDRLRUUULRDDLUURDRRDLUDUDRULRRDDRRLDUDLLDLURLRDLRUUDLDULURDDUUDDLRDLUURLDLRLRDLLRUDRDUURDDLDDLURRDDRDRURULURRLRLDURLRRUUUDDUUDRDRULRDLURLDDDRURUDRULDURUUUUDULURUDDDDUURULULDRURRDRDURUUURURLLDRDLDLRDDULDRLLDUDUDDLRLLRLRUUDLUDDULRLDLLRLUUDLLLUUDULRDULDLRRLDDDDUDDRRRDDRDDUDRLLLDLLDLLRDLDRDLUDRRRLDDRLUDLRLDRUURUDURDLRDDULRLDUUUDRLLDRLDLLDLDRRRLLULLUDDDLRUDULDDDLDRRLLRDDLDUULRDLRRLRLLRUUULLRDUDLRURRRUULLULLLRRURLRDULLLRLDUUUDDRLRLUURRLUUUDURLRDURRDUDDUDDRDDRUD"""

def stringWorker(input):
    aSteps = input.split("\n")
    return aSteps


def createDict():
    dDict = {}

    iCurrentPos = complex(0,0)
    complexString = str(iCurrentPos.real)+"+"+str(iCurrentPos.imag)
    dDict[complexString] = "5"

    iCurrentPos = complex(1,0)
    complexString = str(iCurrentPos.real)+"+"+str(iCurrentPos.imag)
    dDict[complexString]=  "6"
    
    iCurrentPos = complex(-1,0)
    complexString = str(iCurrentPos.real)+"+"+str(iCurrentPos.imag)
    dDict[complexString]=  "4"

    iCurrentPos = complex(0,1)
    complexString = str(iCurrentPos.real)+"+"+str(iCurrentPos.imag)
    dDict[complexString] = "2"

    iCurrentPos = complex(1,1)
    complexString = str(iCurrentPos.real)+"+"+str(iCurrentPos.imag)
    dDict[complexString]=  "3"
    
    iCurrentPos = complex(-1,1)
    complexString = str(iCurrentPos.real)+"+"+str(iCurrentPos.imag)
    dDict[complexString]=  "1"

    iCurrentPos = complex(0,-1)
    complexString = str(iCurrentPos.real)+"+"+str(iCurrentPos.imag)
    dDict[complexString] = "8"

    iCurrentPos = complex(1,-1)
    complexString = str(iCurrentPos.real)+"+"+str(iCurrentPos.imag)
    dDict[complexString]=  "9"
    
    iCurrentPos = complex(-1,-1)
    complexString = str(iCurrentPos.real)+"+"+str(iCurrentPos.imag)
    dDict[complexString]=  "7"

    return dDict

def walker(input, expected):
    #We start at origo
 

    #create dictionary
    dDict = createDict()

    iR = complex(1,0)
    iL = complex(-1,0)
    iD = complex(0, -1)
    iU = complex(0, 1)
    keyString = ""
    currentKey = "5"
    x = 0
    y = 0
    iCurrentPos = complex(x,y)

    aSteps = stringWorker(input)
    for step in aSteps:
        for char in step:
            if char == "R":
                direction = iR
            elif char == "L":
                direction = iL
            elif char == "U":
                direction = iU
            elif char == "D":
                direction = iD

            iPreviosPos = iCurrentPos
            iCurrentPos = iCurrentPos + direction
            complexString = str(iCurrentPos.real)+"+"+str(iCurrentPos.imag)

            if complexString in dDict:
                currentKey = dDict[complexString]
                continue
            else:
                #we are outside keyboard, abort and use "pervious" key and pos (ignore it)
                iCurrentPos = iPreviosPos
                


        #Row finished
        keyString += currentKey

    if keyString == expected:
        print("Correct keycode: ", keyString)
    else:
        print("Expected: ", expected, "but got: ", keyString)


walker(exampleInput1, exampleResult1)
walker(realInput, "97289")
print("\n")


def createDict2():
    dDict = {}

    iCurrentPos = complex(-2,0)
    complexString = str(iCurrentPos.real)+"+"+str(iCurrentPos.imag)
    dDict[complexString] = "5"

    iCurrentPos = complex(-1,0)
    complexString = str(iCurrentPos.real)+"+"+str(iCurrentPos.imag)
    dDict[complexString]=  "6"
    
    iCurrentPos = complex(1,1)
    complexString = str(iCurrentPos.real)+"+"+str(iCurrentPos.imag)
    dDict[complexString]=  "4"

    iCurrentPos = complex(-1,1)
    complexString = str(iCurrentPos.real)+"+"+str(iCurrentPos.imag)
    dDict[complexString] = "2"

    iCurrentPos = complex(0,1)
    complexString = str(iCurrentPos.real)+"+"+str(iCurrentPos.imag)
    dDict[complexString]=  "3"
    
    iCurrentPos = complex(0,2)
    complexString = str(iCurrentPos.real)+"+"+str(iCurrentPos.imag)
    dDict[complexString]=  "1"

    iCurrentPos = complex(1,0)
    complexString = str(iCurrentPos.real)+"+"+str(iCurrentPos.imag)
    dDict[complexString] = "8"

    iCurrentPos = complex(2,0)
    complexString = str(iCurrentPos.real)+"+"+str(iCurrentPos.imag)
    dDict[complexString]=  "9"
    
    iCurrentPos = complex(0,0)
    complexString = str(iCurrentPos.real)+"+"+str(iCurrentPos.imag)
    dDict[complexString]=  "7"

    iCurrentPos = complex(-1,-1)
    complexString = str(iCurrentPos.real)+"+"+str(iCurrentPos.imag)
    dDict[complexString]=  "A"

    iCurrentPos = complex(0,-1)
    complexString = str(iCurrentPos.real)+"+"+str(iCurrentPos.imag)
    dDict[complexString] = "B"

    iCurrentPos = complex(1,-1)
    complexString = str(iCurrentPos.real)+"+"+str(iCurrentPos.imag)
    dDict[complexString]=  "C"

    iCurrentPos = complex(0,-2)
    complexString = str(iCurrentPos.real)+"+"+str(iCurrentPos.imag)
    dDict[complexString]=  "D"


    return dDict

def walker2(input, expected):
    #We start at 5, (-2, 0)
    x = -2
    y = 0
    iCurrentPos = complex(x,y)

    #create dictionary
    dDict = createDict2()

    iR = complex(1,0)
    iL = complex(-1,0)
    iD = complex(0, -1)
    iU = complex(0, 1)
    keyString = ""
    currentKey = "5"

    aSteps = stringWorker(input)
    for step in aSteps:
        for char in step:
            if char == "R":
                direction = iR
            elif char == "L":
                direction = iL
            elif char == "U":
                direction = iU
            elif char == "D":
                direction = iD

            iPreviosPos = iCurrentPos
            iCurrentPos = iCurrentPos + direction
            complexString = str(iCurrentPos.real)+"+"+str(iCurrentPos.imag)

            if complexString in dDict:
                currentKey = dDict[complexString]
                continue
            else:
                #we are outside keyboard, abort and use "pervious" key and pos (ignore it)
                iCurrentPos = iPreviosPos
        #Row finished
        keyString += currentKey

    if keyString == expected:
        print("Correct keycode: ", keyString)
    else:
        print("Expected: ", expected, "but got: ", keyString)

walker2(exampleInput1, "5DB3")
walker2(realInput, "9A7DC")
print("\n")