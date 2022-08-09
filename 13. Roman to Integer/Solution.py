class Solution:
    def romanToInt(self, s: str) -> int:
        vals = {"I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000,
                "IV": 4,
                "IX": 9,
                "XL": 40,
                "XC": 90,
                "CD": 400,
                "CM": 900,
                }

        # cases = {"I": "V",
        #          "I": "X",
        #          "X": "L",
        #          "X": "C",
        #          "C": "D",
        #          "C": "M"}
        total = 0
        i = 0
        while i < len(s):
            # current = 0
            c = s[i]
            if i < len(s)-1 and vals.get(c+s[i+1])!=None:
                total+=vals.get(c+s[i+1])
                i+=1
            else:
                total+=vals.get(c)
            i+=1
        return total


sol = Solution()
print(sol.romanToInt("III"))
