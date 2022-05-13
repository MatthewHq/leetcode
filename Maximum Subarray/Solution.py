class Solution:
    def maxSubArray(self, nums):
        absMax=nums[0]
        # asbMaxInd=0

        maxVal=[]
        maxInd=[]

        maxVal.append(nums[0])
        maxInd.append(0)
        for i in range(1,len(nums)):
            localMax=nums[i]
            localInd=i
                # print(i,j)
                # print(maxVal)
                # print(maxInd)
            if localMax<nums[i]+maxVal[i-1]:
                localMax=nums[i]+maxVal[i-1]
                localInd=maxInd[i-1]


            maxVal.append(localMax)
            maxInd.append(localInd)
            if localMax>absMax:
                absMax=localMax
                # absMaxInd=localInd
        # print(maxVal)
        # print(maxInd)

        # print(absMax)
        return absMax
        # print(absMaxInd)
        




nums = [-2,1,-3,4,-1,2,1,-5,4]
sol=Solution()
print(sol.maxSubArray(nums))