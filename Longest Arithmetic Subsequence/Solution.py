class Solution:
    def longestArithSeqLength(self, nums) -> int:

        ssThreads = {}
        UUIDs = []
        subSeqMax = 1

        for i in range(1, len(nums)):
            if ssThreads.get(nums[i]) != None:
                toPop = []
                for storedStep in ssThreads.get(nums[i]).keys():
                    # print("stored key", storedStep)
                    print("data", UUIDs[ssThreads.get(nums[i]).get(storedStep)][1])
                    UUIDs[ssThreads.get(nums[i]).get(storedStep)][0] = nums[i]
                    UUIDs[ssThreads.get(nums[i]).get(storedStep)][1] = UUIDs[ssThreads.get(nums[i]).get(storedStep)][1]+1
                    newExpected = storedStep+nums[i]
                    print("HEY ", UUIDs[ssThreads.get(nums[i]).get(storedStep)][1], i, nums[i], storedStep, newExpected)
                    if ssThreads.get(newExpected) == None:
                        ssThreads[newExpected] = {}
                    if ssThreads.get(newExpected).get(storedStep) == None or UUIDs[ssThreads.get(newExpected).get(storedStep)][1]<UUIDs[ssThreads.get(nums[i]).get(storedStep)][1]:
                        ssThreads.get(newExpected)[storedStep] = ssThreads.get(nums[i]).get(storedStep)
                    toPop.append(storedStep)
                    if UUIDs[ssThreads.get(nums[i]).get(storedStep)][1] > subSeqMax:
                        subSeqMax = UUIDs[ssThreads.get(nums[i]).get(storedStep)][1]

                for pop in toPop:
                    ssThreads.get(nums[i]).pop(pop)
                    if(len(ssThreads.get(nums[i])) == 0):
                        ssThreads.pop(nums[i])
            for j in range(0, i):

                step = nums[i]-nums[j]
                xpected = nums[i]+step
                if ssThreads.get(xpected) == None:
                    ssThreads[xpected] = {}
                if ssThreads.get(xpected).get(step) == None:
                    UUIDs.append([nums[i], 1])
                    ssThreads.get(xpected)[step] = len(UUIDs)-1
                
                # print(i, j, nums[i]+nums[i]-nums[j])
                print("=======", " i:",i, " nums[i]:",nums[i]," step:", step," xpected:",xpected)
                print(ssThreads)
                print(UUIDs)
                print("max ", subSeqMax+1)
        return subSeqMax+1


sol = Solution()
# sol.longestArithSeqLength([83, 20, 17, 43, 52, 78, 68, 45])
# sol.longestArithSeqLength([3, 6, 9, 12])
# sol.longestArithSeqLength([10, 15, 20, 25, 30, 35, 40, 50, 60])
# # sol.longestArithSeqLength([24, 13, 1, 100, 0,0,0])
# sol.longestArithSeqLength([24, 13, 1, 100, 0, 94, 3, 0, 3])
# sol.longestArithSeqLength([22, 8, 57, 41, 36, 46, 42, 28, 42, 14, 9, 43, 27, 51, 0, 0, 38, 50, 31, 60, 29, 31, 20, 23, 37, 53, 27, 1, 47, 42, 28, 31,
#                           10, 35, 39, 12, 15, 6, 35, 31, 45, 21, 30, 19, 5, 5, 4, 18, 38, 51, 10, 7, 20, 38, 28, 53, 15, 55, 60, 56, 43, 48, 34, 53, 54, 55, 14, 9, 56, 52])

sol.longestArithSeqLength([1,1,0,0,1,0,0,1,0])
# sol.longestArithSeqLength([1,1,0,0,1,0,0,1,0,1,0,1,1,1,0,1,1,0,1,1,0,0,1,1,0,1,0,1,1,0,1,1,1,1,1,0,1,0,0,0,0,0,0,0,1,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0,1,1,1,1,1,0,0,0,1,1,1,1,1,1,0,1,1,0,0,0,1,1,1,1,0,0,1,1,1,0,0,0,1,0,1,0,1,1,1,0,1,1,0,1,1,1,0,1,1,1,0,1,0,1,0,0,0,1,1,0,0,0,0,1,1,0,0,1,0,0,1,0,1,0,0,0,0,0,1,1,1,1,1,0,1,1,0,0,0,0,0,0,1,1,1,0,1,1,0,1,1,1,0,1,0,1,0,0,1,0,0,1,0,0,1,1,0,1,0,0,1,1,0,1,0,0,0,1,0,1,1,1,1,1,0,0,0,1,0,0,1,0,1,1,1,1,0,1,1,0,0,0,0,1,0,1,0,1,1,1,1,1,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,1,1,0,0,1,1,1,0,1,1,0,1,1,1,0,1,0,0,1,0,1,0,0,1,0,1,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1,1,0,1,0,0,0,1,0,1,0,0,0,0,1,0,0,0,1,0,1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,1,0,1,1,0,0,1,1,0,0,1,0,1,1,1,1,0,1,1,1,0,0,0,1,0,0,1,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,0,1,0,0,0,1,1,0,1,0,1,0,0,0,0,1,1,0,0,1,1,0,0,1,1,1,0,0,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,0,0,1,0,0,0,1,0,0,0,0,1,1,1,0,1,1,0,0,1,0,0,1,0,0,1,0,0,1,1,0,0,1,1,0,0,0,1,1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,1,1,0,1,1,0,1,1,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,1,1,0,1,0,1,0,1,0,0,0,0,1,1,0,0,0,1,1,0,1,1,0,1,1,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,1,0,1,1,1,0,0,0,1,1,0,1,0,0,1,0,0,0,1,1,0,0,0,0,1,1,0,0,1,1,0,1,0,0,0,1,1,0,1,0,0,0,1,1,1,1,1])




# print(sol.longestArithSeqLength([83, 20, 17, 43, 52, 78, 68, 45]))
