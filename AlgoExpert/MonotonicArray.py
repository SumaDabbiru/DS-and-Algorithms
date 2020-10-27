def isMonotonicArray(lst):
    if len(array) <= 2:
		return True
	i =  1
	while i < len(array)-1:
		if array[i-1] < array[i] > array[i+1] or array[i-1] > array[i] < array[i+1]:
            return False
		i += 1
    return True
    
    """
    isnonDecreasing = isnonIncreaseing = True

    for i in range(1,len(lst)):
        if lst[i-1] > lst[i]:
            isnonDecreasing = False
        if lst[i - 1] < lst[i]:
            isnonIncreaseing = False
    return isnonDecreasing or isnonIncreaseing

    """

lst=[0,1,2,3,4,5,6,7,8,1]
print(isMonotonicArray(lst))