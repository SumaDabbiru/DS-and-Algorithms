def InsertionSort(array):

    for i in range(1,len(array)):
        separator=array[i]
        j=i
        while j>0 and separator<array[j-1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j-=1
        array[j]=separator
    return array

    # for i in range(1,len(array)):
    #     j=i
    #     while j>0 and array[j]<array[j-1]:
    #         array[j], array[j-1]=array[j-1],array[j]
    #         j-=1
    # return array


print("Insertion")
print("Enter length of an list and then the list")
n=int(input())
array=[]
for i in range(n):
    k=int(input())
    array.append(k)
print(InsertionSort(array))