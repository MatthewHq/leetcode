from typing import List,Optional
class TimeMap:
    # class Entry:
    #     def __init__(self,val,timeStamp):
    #         self.time=timeStamp
    #         self.val=val
    #     def __str__(self) -> str:
    #         return self.val+" "+self.timeStamp

    def __init__(self):
        self.db={}
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        print("set",key,value,timestamp)
        if self.db.get(key)!=None:
            self.db[key].append((value,timestamp))
        else:
            self.db[key]=[(value,timestamp)]
            
        # print(self.db)

    def get(self, key: str, timestamp: int) -> str:
        
        if self.db.get(key)==None:
            return ""
        
        currList=self.db[key]
        l=0
        r=len(currList)-1
        
        
        while l<=r:
            m=l+(r-l)//2
            if currList[m][1]>timestamp:
                r=m-1
            elif currList[m][1]<timestamp:
                l=m+1
            else:
                break
            
        xm=m
        hold=xm
        xm-=1
        for i in range(2):
            if xm<0 or xm>=len(currList) or currList[xm][1]>timestamp:
                break
            else:
                hold=xm
                xm+=1
        
        if hold==0 and currList[hold][1]>timestamp:
            return ""
        return currList[hold][0]
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

tm = None
instructions=["TimeMap", "set", "get", "get", "set", "get", "get"]
input=[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]


instructions=["TimeMap","set","set","set","set","set","get","get","get","get","get","get","get","get"]
input=[[],["love","eight",8],["love","ten",10],["love","fifteen",15],["love","eighteen",18],["love","twenty",20],["love",5],["love",9],["love",10],["love",15],["love",20],["love",25],["love",16],["love",17]]
for i in range(len(instructions)):
    if instructions[i]!="TimeMap":
        if instructions[i]=="get":
            ### get
            print("get",input[i][0],"||||",input[i][1])
            print("===out ",tm.get(input[i][0],input[i][1]))
        else:
            ### set
            tm.set(input[i][0],input[i][1],input[i][2])
    else:
        tm=TimeMap()
