from typing import List,Optional
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow=nums[0]
        fast=nums[0]
        fast=self.increase(fast,2,nums)
        slow=self.increase(slow,1,nums)

        # print(nums)

        while slow!=fast:
            fast=self.increase(fast,2,nums)
            slow=self.increase(slow,1,nums)
            
    
            
        intersection1=slow
        # print(slow)
        slow=nums[0]

        while intersection1!=slow:
            slow=self.increase(slow,1,nums)
            intersection1=self.increase(intersection1,1,nums)
        
        # print(slow)

        return slow

    def increase(self,num,increment,nums):
        for i in range(increment):
            num=nums[num]
        return num
        

        



sol = Solution()



nums = [1,3,4,2,2]
# nums = [3,1,3,4,2]
# nums = [3,1,5,3,2,6,7,8,9]
# nums=[1,3,4,2,2]
print(sol.findDuplicate(nums))