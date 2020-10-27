def BubbleSort(array):
    # temp=0
    # n=len(array)
    # for i in range(n):
    #     for j in range(i,n-1):
    #         if array[i]>array[j+1]:
    #             temp=array[i]
    #             array[i]=array[j+1]
    #             array[j + 1] = temp
    #
    # return array
    isSorted=False
    counter=0
    while not isSorted:
        isSorted=True
        for i in range(len(array)-1-counter):
            if array[i]>array[i+1]:
                array[i],array[i+1]=array[i+1],array[i]
                #swap(i,i+1,array)
                isSorted=False
            #else:
                #isSorted = True
        counter+=1
    return array

def swap(i,j,array):
    array[i], array[j] = array[j], array[i]

print("Bubble")
print("Enter length of an list and then the list")
n=int(input())
array=[]
for i in range(n):
    k=int(input())
    array.append(k)
print(BubbleSort(array))