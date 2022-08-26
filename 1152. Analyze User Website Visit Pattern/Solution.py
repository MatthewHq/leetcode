class Solution:
    def mostVisitedPattern(self, username, timestamp, website):
        mainHash = {}
        highScore = 0
        scoreBoard = []

        userRRContent = {}

        orderKey={}
        orderTS=timestamp.copy()
        orderTS.sort()
        # print("orderTS",orderTS)

        for i in range(len(timestamp)):
            orderKey[timestamp[i]]=i

        for i in range(len(username)):
            
            x=orderKey[orderTS[i]]
            cUser = username[x]
            cWeb = website[x]
            if self.hashProc(userRRContent, cUser, [cWeb]) == None:
                userRRContent[cUser].append(cWeb)
                # if len(userRRContent[cUser]) == 3:
                #     pattern = ""
                #     for j in range(3):
                #         z = (userRRIndex[cUser]+j+1) % 3
                        
                #         pattern += userRRContent[cUser][z]+","
                #         newSet = set()
                #     pattern = pattern[0:len(pattern)-1]
                #     self.hashProc(mainHash, pattern, newSet)
                #     mainHash[pattern].add(cUser)
                #     if len(mainHash[pattern]) >= highScore:
                #         if len(mainHash[pattern]) > highScore:
                #             scoreBoard.clear()
                #         highScore = len(mainHash[pattern])
                #         scoreBoard.append(pattern)
        for user in userRRContent.keys():
            # print(userRRContent)
            patterns=self.allPatterns(userRRContent[user])
            if patterns!=None:
                for pat in patterns:
                    pattern=""
                    for patCandidate in pat:
                        pattern += patCandidate+","
                    pattern = pattern[0:len(pattern)-1]
                    newSet=set()
                    self.hashProc(mainHash, pattern, newSet)
                    mainHash[pattern].add(user)
                    if len(mainHash[pattern]) >= highScore:
                        if len(mainHash[pattern]) > highScore:
                            scoreBoard.clear()
                        highScore = len(mainHash[pattern])
                        scoreBoard.append(pattern)
                
        scoreBoard.sort()
        # print(userRRContent)
        # print("mainhash",mainHash)
        # print(scoreBoard)
        # print(highScore)
        return scoreBoard[0].split(",")

    def allPatterns(self,candidates):
        if len(candidates) < 3:
            return None
        inds = [0, 1, 2]
        result = []
        for i1 in range(len(candidates)-2):
            for i2 in range(i1+1, len(candidates)-1):
                for i3 in range(i2+1, len(candidates)):
                    # print(i1, i2, i3)
                    result.append([candidates[i1],candidates[i2],candidates[i3]])
        return result

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

username = ["uod","uod","uod","kfuagsh","uod"]
timestamp =[520778108,799976888,522803143,968158505,908405336]
website =  ["bfx","taohbuuleq","vsryf","irmbcoebt","bfx"]


# username = ["ua", "ua", "ua", "ub", "ub", "ub"]
# timestamp = [1, 2, 3, 4, 5, 6]
# website = ["a", "b", "a", "a", "b", "c"]


# username = ["uA", "uA", "uA", "uB", "uB", "uB"]
# timestamp = [1, 2, 3, 4, 5, 6]
# website = ["a", "b", "a", "a", "b", "c"]


# username = ["ua","ua","ua","ub","ub","ub"]
# timestamp = [1,2,3,4,5,6]
# website = ["a","b","c","a","b","a"]

# username = ["dowg","dowg","dowg"]
# timestamp =[158931262,562600350,148438945]
# website = ["y","loedo","y"]

# username = ["zkiikgv","zkiikgv","zkiikgv","zkiikgv"]
# timestamp =[436363475,710406388,386655081,797150921]
# website =  ["wnaaxbfhxp","mryxsjc","oz","wlarkzzqht"]

sol = Solution()
print(sol.mostVisitedPattern(username, timestamp, website))
