def quicksort(array):
    quicksortsub(array, 0, len(array)-1)
    return array
    pass

def quicksortsub(array, startidx, endidx):
    if startidx >= endidx:
        return

    pivotidx = startidx
    leftidx = startidx+1
    rightidx =endidx

    while rightidx >= leftidx:
        if array[leftidx] > array[pivotidx] and array[rightidx] < array[pivotidx]:
            array[leftidx], array[rightidx] = array[rightidx], array[leftidx]
        if array[leftidx] <= array[pivotidx]:
            leftidx += 1
        if array[rightidx] >= array[pivotidx]:
            rightidx -=1
    array[pivotidx], array[rightidx] = array[rightidx], array[pivotidx]

    #leftSubArrayIsSmaller = rightidx - 1 - startidx <  endidx - (rightidx+1)

    # if leftSubArrayIsSmaller:
    #     quicksortsub(array, startidx, rightidx - 1)
    #     quicksortsub(array, rightidx + 1, endidx)
    #
    # else:
    quicksortsub(array, rightidx + 1, endidx)
    quicksortsub(array, startidx, rightidx - 1)
    pass

array=[1,3,7,12,45,19,56,98,93,11,6]
print(quicksort(array))