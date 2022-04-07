class Solution:
    def myAtoi(self, s: str) -> int:
        MAX_32_BIT = 2147483647
        MIN_32_BIT = -2147483648

        tokenized = []
        digitStreak = False
        whiteSpaceStreak = True
        zeroStreak = False
        # negative is -1 if negative number, else negative is 1
        negative = None

        for i in range(len(s)):
            if s[i] == '.':
                break

            if whiteSpaceStreak:
                if s[i] != ' ':
                    # notce the 48 here avoiding any leading 0s as well
                    if ord(s[i]) > 47 and ord(s[i]) < 58:
                        whiteSpaceStreak = False
                        if ord(s[i]) > 48:
                            digitStreak = True
                            tokenized.append(ord(s[i])-48)
                        else:
                            zeroStreak = True
                    elif s[i] == '-':
                        if negative == None:
                            negative = -1
                        else:
                            break
                    elif s[i] == '+':
                        if negative == None:
                            negative = 1
                        else:
                            break
                    else:
                        break
                elif negative!=None:
                    break
            elif zeroStreak:
                if ord(s[i]) > 48 and ord(s[i]) < 58:
                    digitStreak = True
                    zeroStreak = False
                    tokenized.append(ord(s[i])-48)
                elif ord(s[i]) != 48:
                    break
            elif digitStreak:
                if ord(s[i]) > 47 and ord(s[i]) < 58:
                    tokenized.append(ord(s[i])-48)
                    if len(tokenized) == 11:
                        break
                else:
                    break

        finalNumber = 0
        if negative == None:
            negative = 1
        for i in range(len(tokenized)):
            finalNumber = 10*finalNumber+tokenized[i]*negative

        if finalNumber < MIN_32_BIT:
            finalNumber = MIN_32_BIT
        elif finalNumber > MAX_32_BIT:
            finalNumber = MAX_32_BIT
        return finalNumber


sol = Solution()

print(sol.myAtoi("--3.14"))
assert sol.myAtoi("--3.14") == 0
assert sol.myAtoi("  00000000000123450678") == 123450678
print(sol.myAtoi("-000000000000001"))
assert sol.myAtoi("-000000000000001") == -1
print(sol.myAtoi("-3.14"))
assert sol.myAtoi("-3.14") == -3
print(sol.myAtoi("00000-42a1234"))
assert sol.myAtoi("00000-42a1234") == 0
print(sol.myAtoi("    +0a32"))
assert sol.myAtoi("    +0a32") == 0
print(sol.myAtoi("  +  413"))
assert sol.myAtoi("  +  413") == 0

