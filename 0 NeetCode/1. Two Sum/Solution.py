class Solution:
    def twoSum(self, nums, target: int):
        matches = {}

        for i in range(len(nums)):
            if matches.get(target-nums[i]) == None:
                matches[target-nums[i]] = [i]
            else:
                matches[target-nums[i]].append(i)

        for i in range(len(nums)):
            num = nums[i]
            if matches.get(num) != None:
                for index in matches[num]:
                    if index!=i:
                        return [i, index]


nums = [2, 7, 11, 15, 1]
tar = 9
nums = [1, 55, 78, 81, 92, 101, 102]
tar = 78+92
nums = [3, 3, 0, 6]
tar = 6
sol = Solution()
print(sol.twoSum(nums, tar))
