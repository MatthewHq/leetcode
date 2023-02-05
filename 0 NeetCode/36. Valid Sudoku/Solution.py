class Solution:
    def isValidSudoku(self, board) -> bool:
        hashBank = {}
        rowCount = len(board)
        colCount = len(board[0])
        for i in range(rowCount):
            for j in range(colCount):
                if board[i][j]!='.':
                    if not self.hashCheck(self.getSquare(i, j)+str(board[i][j]), board[i][j], hashBank) or not self.hashCheck("l"+str(i)+str(board[i][j]), board[i][j], hashBank) or not self.hashCheck("c"+str(j)+str(board[i][j]), board[i][j], hashBank):
                        return False
        # print(hashBank)
        return True

    def hashCheck(self, key, val, hashBank):
        if hashBank.get(key) == val:
            return False
        else:
            hashBank[key] = val
        return True

    def getSquare(self, i, j):
        # print(i,j,int(i/3),int(j/3))
        return str(int(i/3))+str(int(j/3))

#realized at the end I could have just used a set but submitted to save some time since it was similar enough

sol = Solution()
board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                       ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
# board = [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
print(sol.isValidSudoku(board))
