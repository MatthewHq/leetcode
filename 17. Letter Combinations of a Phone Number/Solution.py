from numpy import indices
from torch import index_select


class Solution:

    letters = {'2': ['a', 'b', 'c'],
                   '3': ['d', 'e', 'f'],
                   '4': ['g', 'h', 'i'],
                   '5': ['j', 'k', 'l'],
                   '6': ['m', 'n', 'o'],
                   '7': ['p', 'q', 'r', 's'],
                   '8': ['t', 'u', 'v'],
                   '9': ['w', 'x', 'y', 'z']
                   }

    def letterCombinations(self, digits: str):

        indind = [0 for i in range(len(digits))]

        print(self.letters)
        # cSum=self.checkSum(digits)
        cont=True
        currentChange
        while cont:
            pass
        
        
        # while sum(indind)<checkSum:
        #     pass
        return None


    # def checkSum(self,digits):
    #     sum=0
    #     for i in range(len(digits)):
    #         sum+=len(self.letters[digits[i]])
    #     sum-=len(digits)
    #     print(sum)
    #     return sum

        # return letters[digits]

sol = Solution()
print(sol.letterCombinations('29'))
