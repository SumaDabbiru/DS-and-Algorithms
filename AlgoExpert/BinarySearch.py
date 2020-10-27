def BinarySearch(array,target):
    left=0
    right=len(array)-1

    while left<=right:
        mid = (left + right) // 2
        if array[mid]==target:
            return mid
        elif array[mid]<target:
            left=mid+1
        elif array[mid]>target:
            right=mid-1
    return -1
    pass
def regsearch(array,target):
    for i in range(len(array)):
        if array[i]==target:
            return i
    return -1
    pass

print("BinarySearch")
print("Enter length of an list and then the list")
n=int(input())
array=[]
for i in range(n):
    k=int(input())
    array.append(k)
print("number to search")
target=int(input())
#print(regsearch(array,target))
print(BinarySearch(array,target))