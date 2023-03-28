class MinStack:
    def __init__(self):
        self.stackIndex = -1
        self.stackMax = 0

        self.arr = []
        self.minArr = []

    def addToArr(self,currMin, index, val):
        # print(self.stackMax-1, index)
        if self.stackMax-1 < index:
            self.arr.append(val)
            self.minArr.append(currMin)
            # print(self.arr)
            self.stackMax = len(self.arr)
        else:
            self.arr[index] = val
            self.minArr[index]=currMin
            

    def push(self, val: int) -> None:
        self.stackIndex += 1
        
        currMin=val
        if (len(self.minArr) != 0 and self.stackIndex!=0) and self.minArr[self.stackIndex-1] < val:
            # self.addToArr(self.minArr, self.stackIndex, val)
            currMin=self.minArr[self.stackIndex-1]

            # self.addToArr(self.minArr, self.stackIndex,
                        #   self.minArr[self.stackIndex-1])
        self.addToArr(currMin,self.stackIndex, val)
        # print(self.arr)
        # print(self.minArr)

    def pop(self) -> None:
        self.stackIndex-=1
        return self.arr[self.stackIndex+1]

    def top(self) -> int:
        return self.arr[self.stackIndex]

    def getMin(self) -> int:
        return self.minArr[self.stackIndex]
    

obj = MinStack()

o1=["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
o2=[[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]

counter=0
for x in o1:
    if x=="push":
        obj.push(o2[counter])
        print("push",o2[counter])
        print(obj.arr)
        print(obj.minArr)
    elif x=="pop":
        print("pop",obj.pop())
        print(obj.arr)
        print(obj.minArr)
    elif x=="getMin":
        print("min",obj.getMin())
    elif x=="top":
        print("top",obj.top())
    counter+=1

        # Your MinStack object will be instantiated and called as such:


# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
