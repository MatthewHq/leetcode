class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        for token in tokens:
            try:
                stack.append(int(token))
            except:
                i2 = stack.pop()
                i1 = stack.pop()

                if token == "+":
                    stack.append(i1+i2)
                elif token == "-":
                    stack.append(i1-i2)
                elif token == "*":
                    stack.append(i1*i2)
                elif token == "/":
                    # print(i1,i2,(i1<0) ^ (i2<0))
                    if (i1<0) ^ (i2<0):
                        if i1<0:
                            i1*=-1
                        else:
                            i2*=-1
                        stack.append((i1//i2)*-1)
                    else:
                        stack.append(i1//i2)    
                # print(stack)
            # if token.isdigit():

            # else:

        return stack.pop()
    
    


sol = Solution()

print(6//-132)
tokens = ["2", "1", "+", "3", "*"]
tokens = ["4", "13", "5", "/", "+"]
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]

print(sol.evalRPN(tokens))
