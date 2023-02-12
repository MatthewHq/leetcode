class Solution:
    def isValid(self, s):
        stack=[]
        refs={
        #')':'(',
        '[':']',
        #']':'[',
        '{':'}',
        #'}':'{',
        '(':')'
        }
        for c in s:
            if len(stack)!=0 and refs.get(stack[len(stack)-1])!=None and c==refs[stack[len(stack)-1]]:
                stack.pop()
            else:
                stack.append(c)
        #print(stack)
        if len(stack)==0:
            return True
        else:
            return False
        

                
                




# s = "()"
s = "()[]{}"
s = "("
s="([)]"
sol = Solution()
print(sol.isValid(s))

