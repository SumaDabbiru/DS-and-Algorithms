'''
in a given number insert 5 to provide larger number possible
'''


def updated(array):
    if lst[0] <= 5:
        lst.insert(0, 5)
        return lst
    for i in range(1,len(lst)):
        if lst[i] <= 5:
            lst.insert(i, 5)
            return(lst)
            break
    lst.append(5)
    return lst
    pass


position = 0
print("Enter a number less than 4 digits:")
num = input()
lst=[int (i) for i in str(num)]
#print(lst)
new=updated(lst)
print(int("".join(map(str, new))) )




# def result(num):
#
#     pass
#
# position=0
# print("Enter a number less than 4 digits:")
# num=int(input())
# print(num)
# if 0<num/1000<=5:
#     position=1
#     print(result(num,positon))
# elif 0<(num%1000)/100<=5:
#     print(result(num))
# elif 0<(num%100)/10<=5:
#     print(result(num))
# elif 0<num/1<=5:
#     print(result(num))


