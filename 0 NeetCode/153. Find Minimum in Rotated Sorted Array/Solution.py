from typing import List,Optional
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        lowest=None
        while l<=r:
            m=l+(r-l)//2
            currentMin=min(nums[l],nums[m],nums[r])
            
            if lowest==None or currentMin<lowest:
                lowest=currentMin
            
            if currentMin==nums[m]:
                l=l+1
                r=m-1
            elif currentMin==nums[r]:
                l=m+1
                r=r-1
            elif currentMin==nums[l]:
                return lowest
            
        return lowest

sol = Solution()
nums = [3,4,5,1,2]
nums = [1,1,1,1,1,2]
nums=[11,13,15,17]
print(sol.findMin(nums))
