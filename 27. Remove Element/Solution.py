class Solution:
    def removeElement(self, nums, val: int) -> int:
        if len(nums)==1:
            if nums[0]==val:
                return 0  
            else: #for readability lol
                return 1
        currentIndex=None

        for i in range(len(nums)):
            if nums[i]!=val:
                if currentIndex!=None:
                    nums[currentIndex]=nums[i]
                    nums[i]=val
                    currentIndex+=1
            elif currentIndex==None:
                currentIndex=i

        print(nums)
        return currentIndex

sol = Solution()
nums = [3,2,2,3]
nums = [3,3,3,2,1,3,2,3,4]

print(sol.removeElement(nums,3))


