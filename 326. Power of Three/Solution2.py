class Solution:
    def isPowerOfThree(self, n) -> bool:
        #i can just do mod but it felt too similar to other solution so i did some weird thing
        if n==0:
            return False
        while(True):
            if not int(n/1)==n:
                return False
            if n==1:
                return True
            try:
                n=n/3
            except:
                return False
            
    def testing(self,n):
        return n/3
sol = Solution()
print(sol.isPowerOfThree(0))
# print(sol.testing(27))