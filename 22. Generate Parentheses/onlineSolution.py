class Solution(object):
    def generateParenthesis(self, n: int):
        def dfs(left, right, s):
            # print("[{0}|= {2} =|{1}]".format(left,right,s))
            print("{2}".format(left,right,s))
            if len(s) == n * 2:
                res.append(s)
                return

            if left < n:
                dfs(left + 1, right, s + '(')

            if right < left:
                dfs(left, right + 1, s + ')')

        res = []
        dfs(0, 0, '')
        return res

# import time
# times={}
# for x in range(10):
#     for i in range(10,13):
#         start_time = time.time()

        # sol = Solution()
        # sol.generateParenthesis(i)
#         if times.get(i)==None:
#             times[i]=time.time() - start_time
#         else:
#             times[i]+=time.time() - start_time
#         # print("--- %s seconds ---" % (time.time() - start_time) + str(i))

# for i in times.keys():
#     print(i,times[i])


sol = Solution()
print(sol.generateParenthesis(3))

