def SelectionSort(array):
    # n=len(array)
    # smallest=0
    # for i in range(n):
    #     for j in range(i+1,n):
    #         smallest=array[i]
    #         if array[i]>array[j]:
    #             smallest=min(smallest,array[j])
    #             array[i],array[j]=smallest,array[i]
    #
    # return array

    currentindex=0
    while currentindex < len(array):
        smallest=currentindex
        for i in range(currentindex+1,len(array)):
            if array[smallest]> array[i]:
                smallest=i
        array[currentindex], array[smallest] = array[smallest], array[currentindex]
        currentindex+=1
    return array


print("Selection")
print("Enter length of an list and then the list")
n=int(input())
array=[]
for i in range(n):
    k=int(input())
    array.append(k)
print(SelectionSort(array))

