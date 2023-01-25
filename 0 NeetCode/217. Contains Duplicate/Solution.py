class Solution:
    def containsDuplicate(self, nums) -> bool:
        dupeSet=set()
        for i in nums:
            if i in dupeSet:
                return False
            dupeSet.add(i)
        return True
            

sol = Solution()

arr=[1,2,3,4,4]
arr2=[1,2,3,4,5]
print(sol.containsDuplicate(arr))
print(sol.containsDuplicate(arr2))
        