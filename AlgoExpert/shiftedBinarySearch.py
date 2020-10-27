def shiftedBinarySearch(array, target):
    left = 0
    right = len(array)-1
    while left <= right:
        mid = (left + right)//2

        potentialMatch =  array[mid]
        leftNum = array[left]
        rightNum = array[right]
        if target == potentialMatch:
            return mid
        elif leftNum <= potentialMatch:
            if target < potentialMatch and target >=leftNum:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if target > potentialMatch and target < rightNum:
                left = mid + 1
            else:
                right = mid - 1
    return -1

    pass

array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 45]
target = 33
print(shiftedBinarySearch(array, target))