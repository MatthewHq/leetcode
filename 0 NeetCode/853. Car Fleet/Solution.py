from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        mainStack = [0]
        offStack = []

        for car in range(1, len(position)):

            print("=======", car)
            # print("comapare pos",
                #   position[mainStack[len(mainStack)-1]], "<", position[car])

            # if position[mainStack[len(mainStack)-1]] < position[car]:
            #     nextCarArrival = self.arrival(
            #         target, position[mainStack[len(offStack)-1]], speed[mainStack[len(offStack)-1]])
            #     currentCarArrival = self.arrival(
            #         target, position[car], speed[car])
            #     print("arrivals ",nextCarArrival,">?",currentCarArrival)
            #     if nextCarArrival <= currentCarArrival:
            #         mainStack.append(car)
            #     print("alt", mainStack, offStack)
            # else:
            while len(mainStack) > 0 and position[mainStack[len(mainStack)-1]] > position[car]:
                offStack.append(mainStack.pop())
                print("before", mainStack, offStack)
            print("=======")

            print("mid", mainStack, offStack)
            if len(offStack) > 0:
                nextCarArrival = self.arrival(
                    target, position[offStack[len(offStack)-1]], speed[offStack[len(offStack)-1]])
                currentCarArrival = self.arrival(
                    target, position[car], speed[car])
                print("arrivals ", currentCarArrival, ">?", nextCarArrival)
                if currentCarArrival > nextCarArrival:
                    mainStack.append(car)

            for x in range(len(offStack)):
                mainStack.append(offStack.pop())
            print("after", mainStack, offStack)

            print(car)
        return len(mainStack)

    def arrival(self, target, pos, sp):
        return (target-pos)/sp


sol = Solution()
target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]


position = [8, 10, 0, 5, 3]
speed = [4, 1, 2, 1, 3]

target = 10
position = [6, 8]
speed = [3, 2]

target = 10
position = [0, 4, 2]
speed = [2, 1, 3]

# target = 100
# position = [0,2,4]
# speed = [4,2,1]

print("ASNWER", sol.carFleet(target, position, speed))
