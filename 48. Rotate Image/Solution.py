class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        layers = (int)(n/2)
        # layers= n/2 if n%2==0 else n/2+1

        # for i in range(layers): DEBUG
        # print(i)

        for i in range(layers):  # each layer
            # print("===NEW LAYER===")
            rotationCount = n-(2*i)-1
            # print("rots",rotationCount)
            rootSet = [i, i]
            curSet = rootSet
            curr=None
            for j in range(rotationCount):  # each number set of 4 to be rotated
                hold = matrix[curSet[0]][curSet[1]]
                for k in range(4):
                    # print("currentSet: {}, {} <- {}".format(curSet,hold,curr))
                    curr=hold
                    
                    # calculate which slot will be taken
                    g2 = self.goesTo(n, curSet[0], curSet[1])
                    # print("g2: {}".format(g2))
                    # hold the value who's slot will be taken
                    hold = matrix[g2[0]][g2[1]]
                    # move current into target slot
                    matrix[g2[0]][g2[1]] = curr
                    curSet = g2
                # print("NEXT IN SAME LAYER")
                curSet = [curSet[0], curSet[1]+1]
                

        """
        Do not return anything, modify matrix in-place instead.
        """
        # print(matrix)

    def goesTo(self, n, i, j):
        return [j, n-1-i]


sol = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrix=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
sol.rotate(matrix)
