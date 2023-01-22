class Solution:
    def containsDuplicate(self, nums) -> bool:
        dupeHash={}
        containsDupe=False
        for num in nums:
            if dupeHash.get(num) == None:
                dupeHash[num]=True
            else:
                containsDupe=True
        return containsDupe

sol = Solution()

arr=[1,2,3,4,4]
arr2=[1,2,3,4,5]
print(sol.containsDuplicate(arr2))
        