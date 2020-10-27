def heapSort(array):
    """
    O(N logN) Time
    O(1) space
    :param array:
    :return:
    """
    buildMaxHeap(array)
    for endIdx in reversed(range(1,len(array))):
        array[0], array[endIdx] = array[endIdx], array[0]
        siftDown(0, endIdx-1, array)
    return array

def buildMaxHeap(array):
    firstParentIdx = (len(array)-1) // 2
    for currentIdx in reversed(range(firstParentIdx + 1)):
        siftDown(currentIdx, len(array) - 1, array)

    pass

def siftDown(currentIdx, endIdx, heap):
    childOneIdx = currentIdx * 2 + 1
    while childOneIdx <= endIdx:
        childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1

        if childTwoIdx > -1 and heap[childTwoIdx] > heap[childOneIdx]:
            idxToSwap = childTwoIdx
        else:
            idxToSwap = childOneIdx

        if heap[idxToSwap] > heap[currentIdx]:
            heap[idxToSwap], heap[currentIdx] = heap[currentIdx], heap[idxToSwap]
            currentIdx = idxToSwap # since we swapped the values above, we are updating the index as well
            childOneIdx = currentIdx * 2 + 1 # updating the childoneIdx formula as well
        else:
            return


    pass



array=[1,3,7,12,45,19,56,98,93,11,6]
heapSort(array)
print(array)