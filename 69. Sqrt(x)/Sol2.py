class Solution:
    def mySqrt(self, x: int) -> int:
        i=0
        j=x
        half=x
        if x==1:
            return 1
        if x==0:
            return 0
        while half!=0:
            half=int((j-i)/2)
            target=i+half
            targetSq=target*target
            # print(target,targetSq)
            # print(i,j)

            if targetSq>x:
                j-=half
            else:
                i+=half
        return target


sol = Solution()
print(sol.mySqrt(0))


