from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        l,r=0,n-1
        

        leftMax=[height[l]]
        rightMax=[height[r]]

        for i in range(n-1):
            l+=1
            r-=1
            leftMax.append(max(leftMax[l-1],height[l]))
            rightMax.append(max(rightMax[l-1],height[r]))
        
        # print(leftMax,rightMax)

        trapped=0

        for i in range(1,n-1):
            # print(leftMax[i],rightMax[n-i-1],min(leftMax[l],rightMax[n-i-1]))
            trapped+=min(leftMax[i],rightMax[n-i-1])-height[i]
        return trapped


sol = Solution()
height=[1,2,1,3,1,1,4,1,2,1]
height=[1,0,2,1,0,1,3,2,8,1,2,0,3,2,1,2,1,3,2,1,2,1]
# height=[0,1]
print(sol.trap(height))

