class Codec:
    def encode(self, strs) -> str:
        """Encodes a list of strings to a single string.
        """
        starts=""
        charCounter=0
        fullStr=""

        for stri in strs:
            starts+=str(charCounter)+"="+str(len(stri))+"."
            for c in stri:
                fullStr+=c
                charCounter+=1
        
        #print(starts)
        #print(starts+"/"+fullStr)
        return starts+"/"+fullStr
        

    def decode(self, s: str):
        """Decodes a single string to a list of strings.
        """
        strs=[]
        starts=[]
        lengths=[]

        currentIndex=""
        indexLoop=True
        fullStr=""
        fullStrIndex=None

        for i in range(len(s)):
            c=s[i]
            if indexLoop:
                if c=='.':
                    lengths.append(int(currentIndex))
                    currentIndex=""
                elif c=='=':
                    starts.append(int(currentIndex))
                    currentIndex=""
                elif c=="/":
                    indexLoop=False
                    fullStrIndex=i+1
                else:
                    currentIndex+=c

            else:
                #fullStr+=c
                break
        
        for i in range(len(starts)):
            if lengths[i]==0:
                strs.append('')
            else:
                strs.append(s[fullStrIndex+starts[i]:fullStrIndex+starts[i]+lengths[i]])
        return strs
        

        
        print(starts,lengths)
        print(strs)
        # 
        # currentWord=""
        # startsIndex=0
        # for i in range(fullStrIndex,len(s)):
        #     virtualIndex=i-fullStrIndex
        #     if virtualIndex==startsIndex:
        #         if len(currentWord)!=0:
        #             strs.append(currentWord)
        #             currentWord=""
        #         currentWord+=fullStr[i]


        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

strs=[]

strs.append(["meme","town"])
#strs.append(["Hello","World"])
strs.append([""])
strs.append(["0"])
strs.append(["2","","","1"])
strs.append(["i",""])

for x in strs:
    codec = Codec()
    # codec.encode(x)
    #print(codec.encode(x))
    print(codec.decode(codec.encode(x)))