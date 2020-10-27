def longestSubstringWithoutDuplication(string):

    """
    o(n)time
    O(min(n,a)) space
    :param string:
    :return:
    """
    lastseen = {}
    longest=[0,1]
    startIdx=0

    for i,n in enumerate(string):
        lastseen[n] = i
        

        if n in lastseen:
            startIdx = lastseen[n] + 1 #max(startIdx, )

        if longest[1]-longest[0] < i+1 - startIdx:
            longest = [startIdx, i+1]

        
    print(lastseen)

    return string[longest[0]:longest[1]]

def longestSubstringWithoutDuplication2(string):

    """
    o(n)time
    O(min(n,a)) space
    :param string:
    :return:
    """
    subs = ""
    length = 0
    result = ""
    for i in string:
        length = max(length, len(subs))
        if i not in subs:
            subs += i
        elif i in subs:
            subs = subs[subs.index(i)+1:]
            subs += i
            
        if len(subs)> length:
            result = subs
    return result


#print("longestSubstringWithoutDuplication")
#print("Enter a set of alphabets:")
string="clementisacap"
print(longestSubstringWithoutDuplication2(string))