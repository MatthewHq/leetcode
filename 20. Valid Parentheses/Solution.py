class Solution:
    def isValid(self, s):
        parenthesi = 0
        brace = 0
        bracket = 0
        output = 'None'

        #make expected a STACK

        for c in s:
            # PARENTHESI
            if c == '(':  # open
                parenthesi += 1
                expected = ')'
            elif c == ')':  # --close
                if parenthesi == 0 or expected != ')':
                    print("A")
                    return False
                parenthesi -= 1

            # BRACE
            elif c == '{':  # open
                brace += 1
                expected = '}'
            elif c == '}':  # --close
                if brace == 0 or expected != '}':
                    return False
                brace -= 1

            # BRACKET
            elif c == '[':  # open
                bracket += 1
                expected = ']'
            elif c == ']':  # --close
                if bracket == 0 or expected != ']':
                    return False
                bracket -= 1

        # print(parenthesi,brace,bracket)
        if parenthesi != 0 or brace != 0 or bracket != 0:
            return False
        return True


s = "((((()()))))"
s = "([{}])"
s = "([)]"
s = "()[]{}"
s="{[]}"
sol = Solution()
print(sol.isValid(s))
