from typing import List


class Solution:

    # calculate limit
    def cLim(self, anchorVal, target):
        return target-anchorVal

    # return the next appropriate pointer
    # anchorDir used for direction (1 or 0)
    # 0 is moving right, 1 is moving left
    # anchor for position [0:len(numbers)]
    def movePointer(self, numbers, anchorDir, p1, p2, limit):
        # print("move", p1, p2, anchorDir, numbers, "lim",limit)
        if anchorDir == 1:
            pointer = p1
            while numbers[pointer] < limit:
                pointer += 1
        else:  # anchorDir == 0
            pointer = p2
            while numbers[pointer] > limit:
                pointer -= 1
        return pointer

    def calcAnchor(self, anchorDir, numbers, p1, p2):
        if anchorDir == 0:
            return numbers[p1]
        else:  # anchorDir == 1
            return numbers[p2]

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers)-1

        # initialize anchor as p2 | 0=p1 and 1=p2
        anchorDir = 0

        while numbers[p1]+numbers[p2] != target:
            # print(p1, p2,numbers)
            anchorVal = self.calcAnchor(anchorDir, numbers, p1, p2)
            # print("anchval",anchorVal)
            currentLimit = self.cLim(anchorVal, target)
            # print("lim",currentLimit)
            if anchorDir == 1:
                p1 = self.movePointer(numbers, anchorDir, p1, p2, currentLimit)
            else:  # anchorDir == 0
                p2 = self.movePointer(numbers, anchorDir, p1, p2, currentLimit)
            # print(int(anchorDir),"<<>>",p1,p2,"\n======")

            anchorDir = not anchorDir

        return [p1+1, p2+1]


sol = Solution()

numbers = [1, 1, 3, 3, 4, 8]
print(sol.twoSum(numbers, 6))  # 2,3

numbers = [1, 1, 2, 2, 4, 8]
print(sol.twoSum(numbers, 6))  # 2,4

numbers = [1, 1, 3, 3, 3, 3, 3, 3, 4, 4,
           4, 4, 4, 5, 5, 5, 5, 5, 6, 7, 8, 19]
print(sol.twoSum(numbers, 10))  # 2,3
