from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        mainStack = [position[0]]
        offStack = []
        arrivals = {position[0]:self.arrival(target, position[0], speed[0])}
        # print(position)

        for i in range(1,len(position)):
            frontCheck,rearCheck=True,True
            currentPos=position[i]
            # print(mainStack)
            arrivals[currentPos]=self.arrival(target, currentPos, speed[i])
            while(len(mainStack)!=0 and currentPos < mainStack[-1]):
                offStack.append(mainStack.pop())
            
                
            if len(offStack)!=0:
                if arrivals[currentPos]>arrivals[offStack[-1]]: #if current slower than forward
                    offStack.append(currentPos)
            else:
                offStack.append(currentPos)
            
            
            if len(mainStack)!=0 and arrivals[mainStack[-1]]<=arrivals[currentPos]: #if rear is faster then current
                mainStack.pop()

            while len(offStack)>0:
                mainStack.append(offStack.pop())

        cleanupStack=[mainStack.pop()]
        while len(mainStack)!=0:
            # print(cleanupStack[-1])
            # print(mainStack[-1])
            if(arrivals[cleanupStack[-1]]>=arrivals[mainStack[-1]]):
                mainStack.pop()
            else:
                cleanupStack.append(mainStack.pop())
            
        # print(cleanupStack)
            




        # print(mainStack)
        # testingOutput=[]
        # for i in mainStack:
        #     testingOutput.append(arrivals[i])
        # print(testingOutput)
        # print(arrivals)

        # print(cleanupStack)
        return len(cleanupStack)


        # for i in range(len(position)):
        #     print(target, currentPos, speed[i], self.arrival(
        #         target, currentPos, speed[i]))

    def arrival(self, target, position, speed):
        return (target-position)/speed


sol = Solution()

target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]


target = 13
position = [10,2,5,7,4,6,11]
speed = [7,5,10,5,9,4,1]




print(sol.carFleet(target, position, speed))
