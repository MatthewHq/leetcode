class Solution:
    def longestArithSeqLength(self, nums) -> int:
        trackedDif = None
        subSeqCounter = 0
        subSeqMax = 0
        for i in range(1, len(nums)):
            currentDif = nums[i]-nums[i-1]
            print(currentDif)
            if currentDif == trackedDif:
                subSeqCounter += 1
            else:
                trackedDif = 1
            if subSeqMax < subSeqCounter:
                subSeqMax = subSeqCounter
        return subSeqMax+1


sol = Solution()
print(sol.longestArithSeqLength([20, 1, 15, 3, 10, 5, 8]))
