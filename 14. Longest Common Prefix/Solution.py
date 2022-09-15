class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 1:
            return strs[0]
        ret = ""
        charIndex = 0
        if len(strs[0]) == 0:
            return ret
        currChar = strs[0][charIndex]
        strsLen = len(strs)

        for c in strs[0]:
            strIndex = 1
            currChar = c
            while strIndex < strsLen:
                # print(strs[strIndex],len(strs[strIndex]),charIndex,strs[charIndex],currChar)
                if len(strs[strIndex]) == charIndex or strs[strIndex][charIndex] != currChar:
                    # print("RETURNING")
                    return ret
                # print("a")
                strIndex += 1
            charIndex += 1
            ret += currChar
            # print(currChar)
        # print("HUH")
        return ret


sol = Solution()
strs = ["flower", "flow", "flight"]
strs = ["a"]
strs = ["flower", "flower", "flower", "flower"]

print(sol.longestCommonPrefix(strs))
