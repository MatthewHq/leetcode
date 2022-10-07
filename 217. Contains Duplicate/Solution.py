class Solution:
    def containsDuplicate(self, nums): 
        toHash={}

        for num in nums:
            if toHash.get(num)!=None:
                return True
            else:
                toHash[num]=True
        return False

sol = Solution()


nums=[1]
print(sol.containsDuplicate(nums))

