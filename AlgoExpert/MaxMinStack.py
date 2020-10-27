class stack():
    def __init__(self):
        self.MinMaxStack = []
        self.stack = []
        #self.size=len(self.stack)
        # headindex=0
        # count=0
        # size=k

    def push(self,num):
        newMinMax={"min":num,"max":num}
        if len(self.MinMaxStack):
            lastMinMax=self.MinMaxStack[len(self.MinMaxStack)-1]
            newMinMax["min"]=min(lastMinMax["min"],num)
            newMinMax["max"] = max(lastMinMax["max"], num)
        self.MinMaxStack.append(newMinMax)
        self.stack.append(num)
        return True


        pass
    def pop(self):
        self.MinMaxStack.pop()
        self.stack.pop()
        return True
        pass

    def peek(self):
        return self.stack[len(self.stack)-1]
        pass

    def getMin(self):
        return self.MinMaxStack[len(self.MinMaxStack)-1]["min"]
        # i=0
        # while i<(size):
        #     smallest = stack[i]
        #     if stack[i]<smallest:
        #         smallest=stack[i]
        #     i+=1
        # return smallest

        pass
    def getMax(self):
        return self.MinMaxStack[len(self.MinMaxStack) - 1]["max"]
        # i = 0
        # while i < (size):
        #     largest = stack[i]
        #     if stack[i] > largest:
        #         largest = stack[i]
        #     i += 1
        # return largest
        # pass

    def printarray(self):
        for i in range(len(self.stack)):
            print(self.stack[i])



array=stack()
#size=5
array.push(2)
array.push(1)
array.push(3)
array.push(5)
array.push(4)
print(array.printarray())
print(array.getMax())
print(array.getMin())
array.pop()
print(array.peek())



