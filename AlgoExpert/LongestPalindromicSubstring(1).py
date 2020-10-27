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
#     return string[leftindex+1:rightindex-1]
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


    # A O(n ^ 2) time and O(1) space program to find the  
# longest palindromic substring 
  
# This function prints the longest palindrome substring (LPS) 
# of str[]. It also returns the length of the longest palindrome 
def longestPalSubstr(string): 
    maxLength = 1
  
    start = 0
    length = len(string) 
  
    low = 0
    high = 0
  
    # One by one consider every character as center point of  
    # even and length palindromes 
    for i in range(1, length): 
        # Find the longest even length palindrome with center 
    # points as i-1 and i. 
        low = i - 1
        high = i 
        while low >= 0 and high < length and string[low] == string[high]: 
            if high - low + 1 > maxLength: 
                start = low 
                maxLength = high - low + 1
            low -= 1
            high += 1
  
        # Find the longest odd length palindrome with center  
        # point as i 
        low = i - 1
        high = i + 1
        while low >= 0 and high < length and string[low] == string[high]: 
            if high - low + 1 > maxLength: 
                start = low 
                maxLength = high - low + 1
            low -= 1
            high += 1
  
    #print "Longest palindrome substring is:", 
    print (string[start:start + maxLength])
  
    return maxLength 
    pass

string="asdfdsbmdflirilasbdjexyxjhlqwertytrewq"
#print(longestPalindromicSubstring(string))
print(longestPalSubstr(string))