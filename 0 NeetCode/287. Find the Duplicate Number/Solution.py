from typing import List,Optional
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i=0
        while i<len(nums): # < what
            if nums[i]-1!=i:
                print(nums)
                holder=nums[i]
                otherIndex=nums[i]-1

                #current target set to other
                nums[i]=nums[otherIndex]

                #are they the same? found culprit
                if nums[i]==holder:
                    return holder
                
                #set other to what we were holding
                nums[otherIndex]=holder
                if nums[i]-1==i:
                    i+=1
            else:
                i+=1
sol = Solution()



nums = [1,3,4,2,2]
nums = [3,1,3,4,2]
print(sol.findDuplicate(nums))