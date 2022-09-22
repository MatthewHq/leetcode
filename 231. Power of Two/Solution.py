class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0:
            return False
        flag=False
        i=0
        while (n>>i)!=0:
            if 1 & (n>>i) ==1:
                if not flag:
                    flag = True
                else:
                    return False
            i+=1
        return True

sol = Solution()

# print(sol.isPowerOfTwo(17))
# print("---")
print(sol.isPowerOfTwo(255))
