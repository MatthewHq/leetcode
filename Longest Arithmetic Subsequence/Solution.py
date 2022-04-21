class Solution:
    def longestArithSeqLength(self, nums) -> int:
        allSubSeqs = {}
        subSeqMax = 0
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                currDif = nums[j]-nums[i]
                if allSubSeqs.get(currDif) == None:
                    allSubSeqs[currDif] = 2
                else:
                    allSubSeqs[currDif] = allSubSeqs.get(currDif)+1
                if subSeqMax < allSubSeqs.get(currDif):
                    subSeqMax = allSubSeqs.get(currDif)
                    print("max",subSeqMax," on ",nums[j]," - ",nums[i]," = ",currDif)
        return subSeqMax


sol = Solution()
print(sol.longestArithSeqLength([83, 20, 17, 43, 52, 78, 68, 45]))
