class Solution:
    def threeSum(self, nums):
        counted = {}
        triplets = []
        checkpoints = {}
        for num in nums:
            checkpoints[0-num] = num
            if counted.get(num) == None:
                counted[num] = 1
            else:
                counted[num] += 1

        # print(checkpoints)
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                third = checkpoints.get(nums[i]+nums[j])
                # print(i, j, nums[i]+nums[j], third, [nums[i], nums[j], third])
                
                if third != None:
                    append = True
                    if third!=0:
                        if third == nums[j] and counted[nums[j]] < 2:
                            append = False
                        if third == nums[i] and counted[nums[i]] < 2:
                            append = False
                    elif nums[j]==0 and nums[i] ==0 and counted[0] <3:
                        append=False
                    # print("=======================")
                    if append:
                        inOrder=sorted([nums[i], nums[j], third])
                        if inOrder not in triplets:
                            triplets.append(inOrder)
        return triplets


sol = Solution()

nums = [-1, 0, 1, 2, -1, -4]
nums = [0,1,1]
nums = [-1,0,1,0,0]

print(sol.threeSum(nums))
