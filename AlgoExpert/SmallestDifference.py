def SmallestDifference(arrayOne,arrayTwo):
    """
    :param lst1:
    :param lst2:
    :return:
    """
    arrayOne.sort()
    arrayTwo.sort()
    p1, p2, diff = 0,0,0
    difference = float("inf")
    result = [0,0]
    while p1 < len(arrayOne) and p2 < len(arrayTwo):
        num1 = arrayOne[p1]
        num2 = arrayTwo[p2]
        if arrayOne[p1] > arrayTwo[p2]:
            diff = arrayOne[p1] - arrayTwo[p2]
            p2+=1
        elif arrayOne[p1] < arrayTwo[p2]:
            diff = arrayTwo[p2] - arrayOne[p1]
            p1+=1
        else:
            result = [num1,num2]
            return result
        if diff < difference:
            difference = diff
            result = [num1,num2]

    return result

lst1=[-1,5,10,20,28,3]
lst2=[26,134,135, 15,17]
print(SmallestDifference(lst1,lst2))

