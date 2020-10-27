def ThreeSum(lst, target):

    triplet=[]
    lst.sort()

    for i in range(len(lst)-1):
        left=i+1
        right = len(lst) - 1

        while left < right:
            if lst[i]+lst[left] + lst[right] == target:
                triplet.append([lst[i], lst[left], lst[right]])
                left+=1
                right-=1
            elif lst[i]+lst[left] + lst[right] < target:
                left += 1
            elif lst[i]+lst[left] + lst[right] > target:
                right -= 1
    return triplet

lst=[12,3,1,2,-6,5,-8,6]
target=0
print(ThreeSum(lst, target))

'''     
Bruteforce method
    lst=[]
    array = sorted(array)
    for i in range(len(array)):
        for j in range(len(array)):
            for k in range(len(array)):
                if array[i] + array[j] + array[k] == target:
                    lst.append([array[i], array[j], array[k] ])
    return lst
        

        '''
# lst = []
# print("Two Sum Program!")
# print("Enter the size of the list")
# n = int(input())
# print("Enter the list")
# for i in range(n):
#     element = int(input())
#     lst.append(element)
# print("Enter the target")
# target = int(input())
# print(ThreeSum(lst, target))


