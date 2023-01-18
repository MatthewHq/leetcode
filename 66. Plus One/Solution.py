class Solution:
    def plusOne(self, digits):
        return self.addOne(digits, len(digits)-1)

    def addOne(self, digits, target):
        if digits[target]+1 == 10:
            digits[target] = 0
            if target == 0:
                digits.insert(0, 1)
            else:
                self.addOne(digits, target-1)
        else:
            digits[target] += 1
        return digits


sol = Solution()


arr = [1, 2, 3]

for i in range(900):
    print(sol.plusOne(arr))
