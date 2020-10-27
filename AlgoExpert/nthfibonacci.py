def getnthfib(n):
    # lst=[1,1]
    # for i in range(2,n):
    #     lst.append(lst[i-1]+lst[i-2])
    # return lst
    lasttwo=[0,1]
    counter=3
    while counter<=n:
        newfib=lasttwo[0]+lasttwo[1]
        lasttwo[0]=lasttwo[1]
        lasttwo[1]=newfib
        counter+=1
    return lasttwo[1] if n>1 else lastwo[0]
    pass
print("enter a number for a fibonacci series")
n=int(input())
print(getnthfib(n))

# def getnthfib(n):
#     if n==1 or n==0:
#         return 1
#     return getnthfib(n-1)+getnthfib(n-2)
#     pass
# print("enter a number for a fibonacci series")
# n=int(input())
# for i in range(n):
#     print(getnthfib(i))