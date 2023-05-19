class Solution:
    def dailyTemperatures(self, temperatures):
        tempStack=[]
        nextDay=[0 for x in range(len(temperatures))]
        for tempIndex in range(len(temperatures)):
            while len(tempStack)>0 and temperatures[tempStack[len(tempStack)-1]]<temperatures[tempIndex]:
                # print(tempIndex)
                popped=tempStack.pop()
                # print("POPPING",popped)
                nextDay[popped]=tempIndex-popped
            tempStack.append(tempIndex)
        # print(tempStack.pop())
        return nextDay

sol = Solution()
temperatures = [73,74,75,71,69,72,76,73]
temperatures = [30,40,50,60]
temperatures = [30,60,90]
print(sol.dailyTemperatures(temperatures))


