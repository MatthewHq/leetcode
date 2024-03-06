from typing import List,Optional
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l=1
        r=max(piles)
        if len(piles)==h:
            return r
        
        mid=None
        while l<=r:
            mid=l+(r-l)//2
            
            hours=self.calculateHours(piles,mid)
            if hours<=h:
                holder=mid
            print(l,mid,r,hours)
            if hours>h:
                l=mid+1
            elif hours<h:
                r=mid-1
            else:
                r=mid-1
                
        
            
        return holder

    def calculateHours(self,piles,k):
        sum=0
        for i in piles:
            ceiling = i // k + (i % k != 0)
            sum+=ceiling
        return sum
    
    
sol = Solution()
piles=[1,1,1,999999999] #10
piles=[312884470]
# piles=[1,2,3,4]
# k=2
# print(sol.calculateHours(piles,k))

print(sol.minEatingSpeed(piles,312884469))

