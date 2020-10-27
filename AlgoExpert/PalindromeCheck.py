def isPalindrome(string):
    # #Bruteforce O(n^2)
    reversedstring=""
    for i in range(len(string)-1,-1,-1):  # range(start, stop, step) if step is -ve then it is decrement

        reversedstring+=string[i]
    print(reversedstring)

    return reversedstring==string
    #return string==string[::-1]


    # two pointer O(n) time O(1) space better than all
    # left=0
    # right=len(string)-1
    # while left<right:
    #     if string[left]!=string[right]:
    #         return False
    #     left+=1
    #     right-=1
    # return True


#recusrsion
# def isPalindrome(string,i=0):
#     j=len(string)-1-i
#     return True if i>=j else string[i]=string[j] and isPalindrome( string, i+1)



print("Enter a word to check if it is palindrome")
string=input("")
print(isPalindrome(string))