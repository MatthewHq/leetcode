class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum=0
        rSumArr=[]
        for i in nums:
            runningSum+=i
            rSumArr.append(runningSum)

        return rSumArr
