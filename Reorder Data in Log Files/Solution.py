class Solution:
    def reorderLogFiles(self, logs):
        digitLogs=[]
        wordDir=[]
        wordHash={}
        output=[]
        for i in range(len(logs)):
            log=logs[i]
            if log[len(log)-1].isdigit():
                digitLogs.append(i)
        
            else:
                firstSpace=log.find(" ")
                id=log[:firstSpace]
                toSortLog=log[firstSpace+1:len(log)]
                if wordHash.get(toSortLog)==None:
                    wordHash[toSortLog]=[id]
                    wordDir.append(toSortLog)
                else:
                    wordHash[toSortLog].append(id)
               
                
            
            if len(wordDir)>0:
                wordDir.sort()
        for i in range(len(wordDir)):
            if len(wordHash[wordDir[i]])==1:
                output.append(wordHash[wordDir[i]][0]+" "+wordDir[i])
            else:
                wordHash[wordDir[i]].sort()
                for id in wordHash[wordDir[i]]:
                    output.append(id+" "+wordDir[i])

        for i in range(len(digitLogs)):
            output.append(logs[digitLogs[i]])
        return output
        

                




    #    ["dig1 8 1 5 1","let1 art zero can","dig2 3 6","let2 own kit dig","let3 art zero"]  
logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]

sol = Solution()
print(sol.reorderLogFiles(logs))