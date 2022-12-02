class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums)==1:
            return 1

        current=nums[0]
        nextIndex=1

        for i in range(len(nums)):
            if nums[i]!=current:
                nums[nextIndex]=nums[i]
                nextIndex+=1
                current=nums[i]
        return nextIndex




sol = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
nums = [1,1,2]

print(sol.removeDuplicates(nums))
