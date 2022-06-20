class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dir=0
        dirCount=[0,0,0,0]
        for i in range(4):
            for c in instructions:
                if c=='L':
                    dir-=1
                    if dir==-1:
                        dir=3
                elif c=='R':
                    dir+=1
                    if dir==4:
                        dir=0
                elif c=='G':
                    dirCount[dir]+=1
            x=dirCount[1]-dirCount[3]
            y=dirCount[0]-dirCount[2]
            if i==0 and x == y == 0:
                return True
        x=dirCount[1]-dirCount[3]
        y=dirCount[0]-dirCount[2]
        if x == y == 0:
            return True
            


    


instructions = "GL"
sol = Solution()
print(sol.isRobotBounded(instructions))