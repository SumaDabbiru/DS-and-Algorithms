def maxSubarray(array):
    maxEndinghere = array[0]
    maxSoFar = array[0]
    for i in range(1, len(array)):
        print(array[i])
        maxEndinghere = max(array[i], maxEndinghere + array[i])
        maxSoFar = max(maxEndinghere, maxSoFar)

        print(maxEndinghere, maxSoFar)
    return maxSoFar

array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
print(maxSubarray(array))
