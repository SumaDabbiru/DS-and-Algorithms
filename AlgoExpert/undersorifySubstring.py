def undersorifySubstring(string, substring):
    """
    :param string:
    :param subs:
    :return:
    """
    """
    first get locations of th substring; collapse them if there is overlap; and store in locations parameter
    then add underscore based on the locations to the string
    """
    locations = collapse(getLocations(string, substring))

    return underscorify(string, locations)

def getLocations(string, substring):
    """
    :param string:
    :param substring:
    :return:[ [0, len(substring)] [] ]
    """
    """
    locations = []
    startIdx = 0

    while startIdx < len(string):
        nextIdx = string.find(substring, startIdx)
        if nextIdx != -1:
            locations.append([nextIdx, nextIdx + len(substring)])
            startIdx = nextIdx + 1
        else:
            break
    print(locations)
    return locations

    pass
    """
    locations = []
    left  = 0
    right = len(string)
    t = len(substring)
    
    while left < right:
        if string[left:left+t] == substring:
            locations.append([left,left+t])
        left+=1
    return locations

def collapse(locations):
    """

    :param locations:
    :return:
    """
    """
    this is to merge any overlaps because when substrigs overlap we do not need to put underscore in the middle
    ie atesttestestb should give a_testtestest_b not a_test_test_estb
    """

    if not len(locations):
        return locations
    newLocations = [locations[0]]
    previous = newLocations[0] #maped to first subarray of locations
    #iterate through locations
    for i in range(1,len(locations)):
        current = locations[i]
        #check if there is overlap or sits right next to previous
        if current[0] <= previous[1]:

            previous[1] = current[1] #change the previous end index to next locations end index
        else:
            newLocations.append(current)
            previous = current
    print(newLocations)
    return newLocations


def underscorify(string, locations):
    """
    add all the underscores to the actual string by treversing the string nd locations simultaniously
    :param string:
    :param locations:
    :return:
    """
    locationsIdx = 0
    stringIdx = 0
    inBetweenunderscores = False
    finalchar = []
    i = 0
    while stringIdx < len(string) and locationsIdx < len(locations): # traverse through string and locations
        if stringIdx == locations[locationsIdx][i]: # i can be 0 or 1 that is to add _ at start and end [[0,4], [12,18], [18,22], ]
            finalchar.append("_")
            inBetweenunderscores = not inBetweenunderscores #to track if we are started a _ and didnt close it
            if not inBetweenunderscores: # this helps to traverse through the locations
                locationsIdx += 1
            i = 0 if i == 1 else 1

        finalchar.append(string[stringIdx])
        stringIdx +=1
     # to check if there is any left string index or locations that are not straversed through
    if locationsIdx < len(locations):
        finalchar.append("_")

    if stringIdx < len(string):
        finalchar.append(string[stringIdx:])
    print(finalchar)
    return "".join(finalchar)

    pass


#print("Put undersore before and after the substring found in string")
#print("Enter a string")
#string = input("")
#print("Enter substring")
#substring = input("")
string = "testthis is for testtest to testestest the test"
substring = "test"
print(undersorifySubstring(string, substring))