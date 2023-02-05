class Codec:
    def encode(self, strs) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded=""
        for i in range(len(strs)):
            stri=strs[i]
            if len(stri)==0:
                encoded+="-"
            for j in range(len(stri)):
                c=stri[j]
                encoded+=str(ord(c))
                if j==len(stri)-1:
                    if i!=len(strs)-1:
                        encoded+="_"
                else:
                    encoded+="."
        print("encoded|{}|".format(encoded))
        return encoded
                

        

    def decode(self, s: str):
        """Decodes a single string to a list of strings.
        """
        strs=[]
        currentWord=""
        currentChar=""
        for c in s:
            if c=='.':
                currentWord+=(chr(int(currentChar)))
                currentChar=""
            elif c=='_' or c=='-':
                if len(currentChar)!=0:
                    currentWord+=(chr(int(currentChar)))
                    currentChar=""
                if len(currentWord)!=0:
                    strs.append(currentWord)
                    currentWord=""
                if c=='-':
                    strs.append('')
            else:
                currentChar+=c
        if len(currentChar)!=0:
            currentWord+=(chr(int(currentChar)))
            currentChar=""
        if len(currentWord)!=0:
            strs.append(currentWord)
            currentWord=""
        return strs
    

                

        


# Your Codec object will be instantiated and called as such:

strs=["meme","town"]
strs=["Hello","World"]
#strs=[""]
#strs=["0"]
#strs=["","","1"]
strs=["i",""]
codec = Codec()
print(codec.encode(strs))
print(codec.decode(codec.encode(strs)))