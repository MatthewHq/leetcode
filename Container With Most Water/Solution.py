class Solution:
    def maxArea(self, height) -> int:
        p1 = 0
        p2 = len(height)-1

        maxArea = 0

        while p1 != p2:
            # print("p1, ", p1, " p2, ", p2)
            checkArea = abs(p1-p2)*min(height[p1], height[p2])
            # print("check area, ",checkArea)
            if(checkArea > maxArea):
                maxArea = checkArea
            if min(height[p1], height[p2]) == height[p1]:
                p1 += 1
            else:
                p2 -= 1
        return maxArea


sol = Solution()

print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(sol.maxArea([8,8,8,8,8,8,8,8]))
print(sol.maxArea([5,16,16,1,1,1,16,16,16,16,5]))
