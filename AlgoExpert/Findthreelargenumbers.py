# # incomplete
# def threelargestnumbers(array):
#     largest=[0,0,0]
#     for num in array:
#         updatelargest(largest,num)
#     return largest
#
# def updatelargest(largest,num):
#     if largest[2]==0 or num>largest[2]:
#         update(largest,num,2)
#     elif largest[1] == 0 or num > largest[1]:
#         update(largest, num, 1)
#     elif largest[0] == 0 or num > largest[0]:
#         update(largest, num, 0)
#
# def update(array,num,index):
#     for i in range(index+1):
#         if i==index:
#             array[i]=num
#         else:
#             array[i]=array[i+1]
#
#     pass

print("Three largest numbers in array")
print("Enter length of an list and then the list")
n=int(input())
array=[]
for i in range(n):
    k=int(input())
    array.append(k)
print(threelargestnumbers(array))