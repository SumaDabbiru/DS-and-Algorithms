def TwoSum( lst, target):
    #using two pointer o(nlogn)
    left = 0
    right=len(lst)-1
    while left<right:
        if lst[left]+lst[right]==target:
            return [left,right]
        elif lst[left]+lst[right]<target:
            left+=1
        elif lst[left] + lst[right] > target:
            right-=1
'''     
using hashmap o(n)
    dic={}
    for i in range(len(lst)):
        if target-lst[i] in dic:
            return [dic[target-lst[i]],i]
        else:
            dic[lst[i]]=i
    return[-1,-1]
    
Bruteforce method
        array = sorted(array)
        for i in range(len(array)):
            for j in range(len(array)):
                if array[i] + array[j] == targetSum:
                    return [array[i], array[j]]
        return []
        '''
lst=[]
print("Two Sum Program!")
print("Enter the size of the list")
n=int(input())
print("Enter the list")
for i in range(n):
    element=int(input())
    lst.append(element)
print("Enter the target")
target=int(input())
k=TwoSum (lst, target)
print(k)



