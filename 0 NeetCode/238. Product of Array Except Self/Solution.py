class Solution:
    def productExceptSelf(self, nums):
        sweeps = []
        exceptions = []
        l = len(nums)
        for i in range(len(nums)-1):
            reverseIndex = l-i-1
            index = i
            if index == 0:
                sweeps.append([nums[index]])
                sweeps.append([nums[reverseIndex]])
            else:
                sweeps[0].append(sweeps[0][i-1]*nums[i])
                sweeps[1].append(sweeps[1][i-1]*nums[reverseIndex])
        for i in range(len(nums)):
            if i == 0:
                exceptions.append(sweeps[1][l-i-2])
            elif i == l-1:
                exceptions.append(sweeps[0][i-1])
            else:
                exceptions.append(sweeps[0][i-1]*sweeps[1][l-i-2])

        print(nums)
        print(sweeps)
        print(exceptions)


nums = [8, 2, 3, 4, 5]
nums = [-1,2,3,4,5,1,2]
sol = Solution()
sol.productExceptSelf(nums)
