# def longestPalindromicSubstring(string):
#     """
#     did this comparing with longest peak
#     return the length of longest palindrom string
#     """
#     longestlength = 0
#     i = 1
#
#     while i < len(string) - 1:
#         ispeak = string[i - 1] == string[i + 1]
#         while not ispeak:
#             i += 1
#             continue
#
#         leftindex = i - 1
#         rightindex = i + 1
#         while leftindex >= 0 and rightindex <= len(string)-1 and  string[leftindex] == string[rightindex]:
#             leftindex -= 1
#             rightindex +=1
#
#
#         currentpeaklength = rightindex - leftindex - 1
#
#         longestlength = max(currentpeaklength, longestlength)
#         i = rightindex
#
#     return string[leftindex+1:rightindex]
#     pass

def longestPalindromicSubstring(string):
    """
    O(n^2) time | O(1) space
    Algoexpert
    :param string:
    :return:
    """
    currentLongest = [0,1]

    for i in range(1, len(string)):
        odd = getlongestPalindromicSubstring(string, i-1, i+1)
        even = getlongestPalindromicSubstring(string, i-1, i)
        longest = max(odd, even, key=lambda x: x[1] - x[0])
        print(longest)
        currentLongest = max(longest, currentLongest, key=lambda x: x[1] - x[0])
    return string[currentLongest[0] : currentLongest[1]]

def getlongestPalindromicSubstring(string, leftIdx, rightIdx):
    while leftIdx >0  and rightIdx < len(string):
        if string[leftIdx] != string[rightIdx]:
            break
        leftIdx -= 1
        rightIdx += 1
    return [leftIdx+1, rightIdx]

# def longestPalindromicSubstring(string):
#     """
#     O(n^3) time | O(1) space
#     Algoexpert
#     :param string:
#     :return:
#     """
#     longest = ""
#     currentLongest = [0,1]
#
#     for i in range(1, len(string)):
#         for j in range(i,len(string)):
#             substring = string[i : j+1]
#
#             if len(substring) > len(longest) and isPalindrome(substring):
#                 longest = substring
#     return longest
#
# def isPalindrome(string):
#     left=0
#     right=len(string)-1
#     while left<right:
#         if string[left]!=string[right]:
#             return False
#         left+=1
#         right-=1
#     return True


string="asdfdsbmdflirilasbdjexyxjhlqwertytrewq"
print(longestPalindromicSubstring(string))