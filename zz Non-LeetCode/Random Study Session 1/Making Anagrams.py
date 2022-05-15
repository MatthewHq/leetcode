

from urllib.request import BaseHandler


class anagramMaker:

    def __init__(self,a,b):
        self.a=a
        self.b=b
        self.aHash={}
        self.bHash={}
        self.deletions=0

        for c in a:
            self.addToDict(c,self.aHash)
        for c in b:
            self.addToDict(c,self.bHash)
        
        for key in self.aHash:
            self.equalize(key,self.aHash,self.bHash)
        for key in self.bHash:
            self.equalize(key,self.bHash,self.aHash)
    
    def equalize(self,key,hash1 ,hash2):
        if hash2.get(key)==None:
            self.deletions+=hash1[key]
        else:
            h1v=hash1[key]
            h2v=hash2[key]
            if h1v==h2v:
                return
            if h1v>h2v:
                self.deletions+=h1v-h2v
                hash1[key]=h2v
            else:
                self.deletions+=h2v-h1v
                hash2[key]=h1v
            hash2.pop(key)



        

    def addToDict(self,c,hash):
        if hash.get(c)==None:
            hash[c]=1
        else:
            hash[c]+=1

    


def makeAnagram(a, b):
    # Write your code here
    ana=anagramMaker(a,b)
    return ana.deletions
    print(ana.deletions)
        


a='fcrxzwscanmligyxyvym'
b='jxwtrhvujlmrpdoqbisbwhmgpmeoke'
print(makeAnagram(a,b))
