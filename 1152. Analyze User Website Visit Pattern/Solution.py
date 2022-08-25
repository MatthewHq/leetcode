class Solution:
    def mostVisitedPattern(self, username, timestamp, website):
        # we will begin with the assumption that timestamp is always in order, it only makes sense
        mainHash = {}
        highScore = 0
        scoreBoard = []

        userRRIndex = {}
        userRRContent = {}

        orderKey={}
        orderTS=timestamp.copy()
        orderTS.sort()

        for i in range(len(timestamp)):
            orderKey[timestamp[i]]=i

        for i in range(len(username)):
            x=orderKey[orderTS[i]]
            cUser = username[x]
            cWeb = website[x]
            if self.hashProc(userRRIndex, cUser, 0) == None:
                userRRIndex[cUser] =userRRIndex[cUser]+ 1
            # print(userRRIndex[cUser], userRRIndex[cUser] % 3)
            if self.hashProc(userRRContent, cUser, [cWeb]) == None:
                # print(timestamp[i],userRRIndex,"EY")
                # print("User and Length", cUser, len(
                # userRRContent[cUser]), userRRContent[cUser])
                if len(userRRContent[cUser]) == 3:
                    # print("ENTERED")
                    userRRContent[cUser][userRRIndex[cUser] % 3] = cWeb
                else:
                    # print("appending", cUser, userRRContent[cUser])
                    userRRContent[cUser].append(cWeb)

                if len(userRRContent[cUser]) == 3:
                    pattern = ""
                    # print("OKAY LOOPING ON ",userRRContent)
                    for j in range(3):
                        z = (userRRIndex[cUser]+j+1) % 3
                        
                        pattern += userRRContent[cUser][z]+","
                        newSet = set()
                    # print("RESULT",pattern)
                    pattern = pattern[0:len(pattern)-1]
                    self.hashProc(mainHash, pattern, newSet)
                    mainHash[pattern].add(cUser)
                    if len(mainHash[pattern]) >= highScore:
                        if len(mainHash[pattern]) > highScore:
                            scoreBoard.clear()
                        highScore = len(mainHash[pattern])
                        scoreBoard.append(pattern)
        scoreBoard.sort()
        # print(mainHash)
        # print(scoreBoard[0])
        # print()
        # print(highScore)
        return scoreBoard[0].split(",")

    def hashProc(self, hash, key, valEmpt):
        result = None
        if hash.get(key) == None:
            result = valEmpt
            hash[key] = result
        else:
            result = None
        return result


username = ["joe", "joe", "joe", "james", "james",
            "james", "james", "mary", "mary", "mary"]
timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
website = ["home", "about", "career", "home", "cart",
           "maps", "home", "home", "about", "career"]


username = ["ua", "ua", "ua", "ub", "ub", "ub"]
timestamp = [1, 2, 3, 4, 5, 6]
website = ["a", "b", "a", "a", "b", "c"]


username = ["uA", "uA", "uA", "uB", "uB", "uB"]
timestamp = [1, 2, 3, 4, 5, 6]
website = ["a", "b", "a", "a", "b", "c"]

username = ["dowg","dowg","dowg"]
timestamp =[158931262,562600350,148438945]
website = ["y","loedo","y"]


sol = Solution()
print(sol.mostVisitedPattern(username, timestamp, website))
