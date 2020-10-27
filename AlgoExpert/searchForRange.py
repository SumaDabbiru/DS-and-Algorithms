def searchForRange(array, target):
    """
    check the result again
    :param array:
    :param target:
    :return:
    """
    left = 0
    right = len(array) - 1
    result = [-1,-1]

    while left <= right:
        mid = (left + right) // 2

        if array[mid] < target:
            left = mid + 1
        elif array[mid] > target:
            right = mid - 1

        else:        # array[mid] == target
            firstIdx = lastIdx = mid


            while array[firstIdx] == target:
                if firstIdx == 0 or array[firstIdx - 1] != target:
                    result[0] = firstIdx
                    break
                firstIdx -= 1

            while array[lastIdx] == target:
                if lastIdx == len(array) - 1 or array[lastIdx] != target:
                    result[1] = lastIdx
                    break
                lastIdx += 1
            return [firstIdx, lastIdx]

    #return [-1, -1]
    pass




# array = [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
# target = 45
array = [5, 7, 7, 8, 8, 10]
target = 10

print(searchForRange(array, target))
