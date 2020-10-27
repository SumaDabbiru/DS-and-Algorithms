def moveelementtoend(lst, num):
    left=0
    right=len(lst)-1
    #for i  range(len(lst)-1):
    while left<right:
        while left<right and lst[right]==num:
            right-=1
        if lst[left]==num:
            lst[left],lst[right] = lst[right], lst[left]
        left+=1

    return lst

    pass
"""
lst = []
print("Move the element to end")
print("Enter the size of the list")
n = int(input())
print("Enter the list")
for i in range(n):
    element = int(input())
    lst.append(element)
print("Enter the number")
target = int(input())
"""
lst=[2, 1, 2, 2, 2, 3, 4, 2]
target = 2

print(moveelementtoend(lst, target))