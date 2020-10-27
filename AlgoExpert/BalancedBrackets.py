def BalancedBrackets(s):
    # opening="[({"
    # closing="]})"
    # brackets={")":"(","}":"{","]":"[",}
    # stack=[]
    # for i in s:
    #     if i in opening:
    #         stack.append(i)
    #     elif i in closing:
    #         if len(stack)==0:
    #             return False
    #         if stack[-1]==brackets[i]:
    #             stack.pop()
    #         else:
    #             return False
    # return len(stack)==0

    brackets={")":"(","}":"{","]":"[",}
    stack=[]
    for item in s:
        if item in brackets.values():
            stack.append(item)
        elif item in brackets.keys():
            if len(stack)>0 and stack[-1]==brackets[item]:
                stack.pop()
            else:
                return False
    return stack==[]



    pass

print("Balanced Brackets")
print("Enter only open and closed parenthesis-(){}[]. enter the number of brackets that would be entered")
bracketlist=str(input())
# n=int(input())
# bracketlist=[]
# for i in range(n):
#     b=input("")
#     bracketlist.append(b)

print(BalancedBrackets(bracketlist))