class Solution:
    def mySqrt(self, x: int) -> int:
        total=0
        counter=0
        while total<=x:
            total=counter*counter
            counter+=1
        return counter-2

sol = Solution()
print(sol.mySqrt(8))
print(sol.mySqrt(16))
print(sol.mySqrt(25))
print(sol.mySqrt(24))
print(sol.mySqrt(81))
print(sol.mySqrt(500))


