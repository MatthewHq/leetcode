

from lib2to3.pgen2 import token
from re import S
from typing import final


class Solution:
    def myAtoi(self, s: str) -> int:
        MAX_32_BIT = 2147483647
        MIN_32_BIT = -2147483648

        tokenized = []
        digitStreak = False
        # negative is -1 if negative number, else negative is 1
        negative = 1

        for i in range(len(s)):
            if not digitStreak:
                if s[i] != ' ':
                    if s[i] == '-':
                        negative = -1
                    elif s[i] == '+':
                        negative = 1
                    elif ord(s[i]) > 47 and ord(s[i]) < 58:
                        digitStreak = True
                        tokenized.append(ord(s[i])-48)
            else:
                if ord(s[i]) > 47 and ord(s[i]) < 58:
                    tokenized.append(ord(s[i])-48)
                    if len(tokenized) == 10:
                        # digitStreak = False
                        break
                else:
                    # digitStreak = False
                    break
        # print("final negative", negative)
        # print(tokenized)

        finalNumber = 0
        for i in range(len(tokenized)):
            finalNumber = 10*finalNumber+tokenized[i]*negative

        if finalNumber < MIN_32_BIT:
            finalNumber = MIN_32_BIT
        elif finalNumber > MAX_32_BIT:
            finalNumber = MAX_32_BIT
        return finalNumber


sol = Solution()


print(sol.myAtoi("words and 987"))
print(sol.myAtoi(" 01000001 "))
