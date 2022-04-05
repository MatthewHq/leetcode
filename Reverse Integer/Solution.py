class Solution:
    def reverse(self, x: int) -> int:
        MIN_32_BIT_TRUNCATED = -214748364  # -2147483648 <- not truncated
        negative = x < 0
        numDigits = 0
        comparator = -1
        truncateds = {}
        numOrder = {}

        if not negative:
            x *= -1

        print(x)
        if x > -10:
            return x if negative else -x

        # print(x)
        while comparator > x:
            comparator *= 10
            numDigits += 1
        print("numdigts ", numDigits)

        for i in range(numDigits):
            truncateds[i] = (int)(x/10**i)

        for i in range(numDigits-1):
            numOrder[i] = truncateds[i]-truncateds[i+1]*10
        numOrder[numDigits-1] = truncateds[numDigits-1]

        reversedFit = 0
        for i in range(0, numDigits-1):
            reversedFit += numOrder[i]*10**(numDigits-i-2)

        print(reversedFit)
        print(numDigits)
        print(truncateds)
        print(numOrder)

        corrector = 1 if negative else -1
        if(reversedFit < MIN_32_BIT_TRUNCATED):
            corrector = 0
        elif numDigits > 9:
            finalDigitCheck = -8 if negative else -7
            if numOrder[numDigits-1] < finalDigitCheck:
                corrector = 0
        return corrector*(reversedFit*10+numOrder[numDigits-1])

        print(reversedFit)
        # fullyReversed =
        # print(fullyReversed)


sol = Solution()
# print(sol.reverse(1111111111))
print(sol.reverse(-9463847412))
# print(sol.reverse(123))
