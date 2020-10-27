def LongestPeak(lst):
    longestpeaklength=0
    i=1

    while i < len(lst)-1:
        ispeak = lst[i-1] < lst[i] and lst[i]>lst[i+1]
        if not ispeak:
            i+=1
            continue

        leftindex = i-1
        while leftindex>=0 and lst[leftindex] < lst[leftindex+1]:
            leftindex-=1


        rightindex = i+1
        while rightindex >= 0 and lst[rightindex-1] > lst[rightindex] :
            rightindex += 1

        currentpeaklength = rightindex-leftindex-1
        longestpeaklength=max(currentpeaklength,longestpeaklength)
        i=rightindex

    return longestpeaklength

lst=[1,2,3,3,4,0,10,6,5,-1,-3,2,3]
#lst=[1,2,3,4,5,4,3,2,1,2,3,4,3,2,1]
print(LongestPeak(lst))