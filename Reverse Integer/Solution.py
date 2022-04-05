class Solution:
    def reverse(self, x: int) -> int:
        MIN_32_BIT_TRUNCATED = -214748364  # -2147483648 <- not truncated
        negative = x < 0
        numDigits = 0
        comparator = -1
        truncateds = []
        numOrder = []

        if not negative:
            x *= -1

        if x > -10:
            return x if negative else -x

 
        while comparator >= x:
            comparator *= 10
            numDigits += 1

        for i in range(numDigits):
            truncateds.append((int)(x/10**i))

        streakOfZeros = True
        finalNumDigits = numDigits
        for i in range(numDigits-1):
            trunc = truncateds[i]-truncateds[i+1]*10
            if not streakOfZeros:
                numOrder.append(trunc)
            elif trunc != 0:
                streakOfZeros = False
                numOrder.append(trunc)
            else:
                finalNumDigits -= 1

        for i in range(numDigits-finalNumDigits):
            truncateds.pop(0)
        numDigits = finalNumDigits
        numOrder.append(truncateds[numDigits-1])

        reversedFit = 0
        for i in range(0, numDigits-1):
            reversedFit += numOrder[i]*10**(numDigits-i-2)

        corrector = 1 if negative else -1
        if(reversedFit < MIN_32_BIT_TRUNCATED):
            corrector = 0
        elif numDigits > 9:
            finalDigitCheck = -8 if negative else -7
            if numOrder[numDigits-1] < finalDigitCheck:
                corrector = 0
        return corrector*(reversedFit*10+numOrder[numDigits-1])


sol = Solution()
print(sol.reverse(-1100000))

