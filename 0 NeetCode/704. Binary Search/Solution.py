from typing import List,Optional
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        high=len(nums)-1
        low=0
        pt=low+int((high-low)/2)
        while target!=nums[pt]:
            curr=nums[pt]
            if curr>target:
                high=pt-1
            else:
                low=pt+1
            if low+int((high-low)/2)==pt:
                return -1
            pt=low+int((high-low)/2)
            if pt>=len(nums)or pt<0:
                return -1
        return pt

sol = Solution()
nums=[-1,1,2,3,4,5,6]
target=3
print(sol.search(nums,-1))
