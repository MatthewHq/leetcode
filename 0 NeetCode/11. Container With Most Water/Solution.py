from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, (len(height)-1)
        # print(l, r)
        waterMax = 0
        while l < r:
            currentWater = (r-l)*min(height[l], height[r])
            if currentWater > waterMax:
                waterMax = currentWater
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return waterMax


sol = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(sol.maxArea(height))
