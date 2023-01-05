class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==1:
            return True
        #usually prefer to work in while loop but will do recursion just to sharpen recursion
        return self.recurseInt(n)
    
    def recurseInt(self,target,runningCount=3):
        if runningCount>target:
            return False
        if runningCount==target:
            return True
        runningCount*=3
        return self.recurseInt(target,runningCount)


sol=Solution()
for i in range(10):

    print(i)
    print(3**i,sol.isPowerOfThree(3**i))
    print((3**i)+1,sol.isPowerOfThree((3**i)+1))
    print(3**i-1,sol.isPowerOfThree(3**i-1))
    print("-------------")
            
