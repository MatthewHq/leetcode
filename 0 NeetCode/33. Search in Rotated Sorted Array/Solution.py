from typing import List,Optional
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        
        while l<=r:
            m=l+(r-l)//2
            # print(l,m,r)
            if nums[m]==target:
                return m
            
            ### Defining which range is ascending
            ###     then we have to define what range we will fall into, left or right
            ###     "dir"
            ###         true:   between l - m
            ###         false:  between m - r
            
            dir=True
            
            if nums[r]>nums[m]:
                ### between m and r are ascending
                if nums[m]<target<=nums[r]:
                    dir=False
                
            else:
                ### between l and m are ascending
                if not (nums[l]<=target<nums[m]):
                    dir=False
            
            # print(nums[l],nums[m],nums[r])
            # print("L-M" if dir else "M - R")
            
            if dir:
                r=m-1
            else:
                l=m+1
        return -1
            
                    
        
            #almost there, we decided to do a deductive approach however we realize our method of deduction was too static and needs to be implemented in a dynamic way
    

sol = Solution()

nums = [1]
target = 1

print(sol.search(nums,target))

