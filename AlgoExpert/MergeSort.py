def RMergeSort(array):
    """
    Recursive
    :param array:
    :return:
    """
    if len(array) == 1:
        return array

    mid =  len(array) // 2
    leftsub = array[:mid]
    rightsub = array[mid:]

    RMergeSort(leftsub)
    RMergeSort(rightsub)

    i = j = k = 0

    while i < len(leftsub) and j < len(rightsub):
        if leftsub[i] < rightsub[j]:
            array[k] = leftsub[i]
            i+=1
        else:
            array[k] =  rightsub[j]
            j+=1

        k+=1

    while i < len(leftsub):
        array[k]=leftsub[i]
        i+=1
        k+=1

    while j< len(rightsub):
        array[k] = rightsub[j]
        j += 1
        k+=1
    pass

def mergeSort(array):
    """
    Iterative
    :param array:
    :return:
    """
    if len(array)==1:
        return array

    mid =  len(array) // 2
    leftsub = array[:mid]
    rightsub = array[mid:]

    return mergeSortedArrays(mergeSort(leftsub), mergeSort(rightsub))

def mergeSortedArrays(lefthalf, righthalf):
    sortedArray = [0] * (len(lefthalf) + len(righthalf))
    i = j = k = 0
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] <= righthalf[j]:
            sortedArray[k] = lefthalf[i]
            i+=1
        else:
            sortedArray[k] = righthalf[j]
            j-=1
         k+=1

    while i < len(lefthalf):
        sortedArray[k] = lefthalf[i]
        i+=1
        k+=1

    while j< len(righthalf):
        sortedArray[k] = righthalf[j]
        j += 1
        k+=1

    return sortedArray


array=[1,3,7,12,45,19,56,98,93,11,6]
#RMergeSort(array)
mergesort(array)
print(array)