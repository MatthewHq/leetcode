from typing import List,Optional
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
       l=len(nums)
    #    print(l)
       mx=(l*(l+1))/2-1
    #    print(mx)
       realSum=sum(nums)
    #    print(realSum)
       dif=mx-realSum
    #    print(dif)
       dupe=l-1-dif
    #    print(dupe)
       return int(dupe)
sol = Solution()



nums = [1,3,4,2,2]
nums = [3,1,3,4,2]
print(sol.findDuplicate(nums))