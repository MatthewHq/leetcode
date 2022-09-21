class Solution:
    def isValid(self, s):
        pairs = {
            '(': ')',
            '[': ']',
            '{': '}',
            ')': '1',
            ']': '1',
            '}': '1'
        }
        expectedStack = []
        for c in s:

            if pairs[c] == '1':
                if len(expectedStack) != 0 and expectedStack[len(expectedStack)-1] == c:
                    expectedStack.pop()
                else:
                    return False
            else:
                expectedStack.append(pairs[c])
        if len(expectedStack) != 0:
            return False
        return True


# s = "((((()()))))"
# s = "([{}])"
# s = "([)]"
# s = "()[]{}"
# s = "{[]}"
s = "]"
sol = Solution()
print(sol.isValid(s))
