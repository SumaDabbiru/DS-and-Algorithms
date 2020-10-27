def productsum(array,multiplier=1):

    sum=0
    for element in array:
        if type(element) is list:
            sum=sum+productsum(element,multiplier+1)

        else:
            sum=sum+element
    return ( sum * multiplier)

# print("The product sum problem Enter an array")
# array=list[input()]
# print(productsum(array))

print(productsum([5,2,[7,-1],3,[6,[-13,8],4]]))