def getNewPattern(pattern):
    """
    if patter is given in yyxyyx instead of x first, we gotta reverse in interms to make x first
    yyxyyx becomes xxyxxy
    xxyxxy will stay the same
    :return:
    """
    patternLetters =  list(pattern)

    if pattern[0] == "x":
        return patternLetters
    else:
        return list(map(lambda char : "x" if char == "y" else "y" , patternLetters))

def getCountAndFirstYPos(pattern, counts):

    """
    count overall x and y count
    and know where the y starts
    here x=4
    and first y is at index 2
    :return:
    """
    firstYPos = None

    for i, char in enumerate(pattern):
        counts[char] += 1

        if char == "y" and firstYPos == None:
            firstYPos = i

    return firstYPos # and update counts
    pass

def patternMatching(pattern, string):
    """
    space = O(n+m) (n= len of inputstring, m= lenght of pattern)
    Time = O(n^2 + m)
    :param pattern:
    :param string:
    :return:
    """
    """
    here
    we consider len(x) is one and check for repetition
    if len(x) = 1; len(y)  = ( len(string) - len(x) * no. of x's ) / no. of y's ((30 - 1 * 4) /2) (since 4 x and 2 y and it is a formula)
    
    now calculate first y position in main string : yIdx = first y pos in pattern * len X = 2
    since y should be at index 2 in patter
    potential x=g (since len is considered as 1) and y = gopowerranger (since y is considererd form idx 2 to g ie x )
     and put this in the pattern and check if it is sam as the string  g g gopowerranger g g gopowerranger which is wrong
     
     so
     
     recalulate len of x and y and potential x and y 
     len(x) = 2 len(y) = (30-2*4)/2 = 11
     first y in string starts at 2*2 = 4
     x=go
     y=poerranger
    
    """

    if len(pattern) > len(string):
        return []
    newPattern  = getNewPattern(pattern)
    didSwitch = newPattern[0] != pattern[0] # to keep track if we have done the switch or not
    counts = {"x":0, "y":0} #we can have an array instead
    firstYPos = getCountAndFirstYPos(newPattern, counts)

    if counts["y"] != 0:
        for lenOfX in range(1, len(string)):
            lenOfY = (len(string) - lenOfX * counts["x"]) / counts["y"]

            if lenOfY <=0 or lenOfY % 1 != 0:
                continue

            lenOfY = int(lenOfY) # we might get float value in the calculation

            yIdx = firstYPos * lenOfX

            x = string[0:lenOfX] #g in first iteration
            y = string[yIdx:yIdx+lenOfY]  #gopowerangers
            #print(x,y)
            potentialMatch = map(lambda char : x if char == "x" else y, newPattern)
            #print("".join(potentialMatch))
            print(type(potentialMatch))
            if string == "".join(potentialMatch):
                return [x, y]  if not didSwitch else [y, x]

    else:
        lenOfX = len(string)/ counts["x"]
        if lenOfX % 1 ==0:
            lenOfX = int(lenOfX)

            x = string [:lenOfX]
            potentialMatch = map(lambda char: x, newPattern)

            if string == "".join(potentialMatch):
                return [x, ""] if not didSwitch else ["", x]

    return []


"""
print("enter a tring in a pattern")
print("Enter a string") #gogopowerrangergogopowerranger
string = input("")
print("Enter pattern of the string")
pattern = input("")  #xxyxxy
"""
pattern = "xxyxxy"
string = "gogopowerrangergogopowerranger"
print(patternMatching(pattern, string))