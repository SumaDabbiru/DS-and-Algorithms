def subarraySort(array):
    # identifies the subarray that has to sorted to make the whole array look sorted
    """
    left = 1
    right = len(array)-1
    result = []
    
    while left < right:
        while array[left] > array[left -1] and left < right:
            left += 1
        print(left)
        while array[right] < array[right+1] and right < len(array):
            right -= 1
            print(right)
        
        smallValue = min(array[left], array[right])
        largeValue = max(array[left], array[right])
        break
    
    for i in range(len(array)):
        if array[i] > smallValue:
            result.append(i)
    for i in reversed(range(len(array))):
        if array[i] < largeValue:
            result.append(i)
    return result
    
            
    
    """
    minval = float("inf")
    maxval = float("-inf")


    for i in range(len(arr)-1):
        num = arr[i]

        if isOutOfOrder(i, arr):
            minval = min(minval, num)
            maxval = max(maxval, num)


    if minval == float("inf"):
        return [-1,-1]

    print(minval, maxval)
    
    subarrleftIdx = 0
    subarrrightIdx = len(arr) - 1
    while minval >= arr[subarrleftIdx]:
        subarrleftIdx += 1
    while maxval <= arr[subarrrightIdx]:
        subarrrightIdx -= 1

    return [subarrleftIdx, subarrrightIdx]

def isOutOfOrder(i, arr):
    if i == 0:
        return arr[0] > arr[1]
    if i == len(arr)-1:
        return arr[len(arr) - 1] < arr[len(arr) - 2]
    return arr[i] > arr[i + 1] or arr[i] < arr[i - 1]



# print("enter a list of 10 integers")
# arr=[]
# for i in range(10):
#     arr.append(int(input()))
#
# print(arr)

arr = [1,2,4,7,10,11,7,12,6,7,16,18,19  ]
print(arr)

print(subarraySort(arr))