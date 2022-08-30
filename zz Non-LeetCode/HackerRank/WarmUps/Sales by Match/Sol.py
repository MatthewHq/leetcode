def sockMerchant(n, ar):
    # Write your code here
    pairCount=0
    sockpairs={}
    for i in range(len(ar)):
        if sockpairs.get(ar[i]):
            sockpairs[ar[i]]+=1
        else:
            sockpairs[ar[i]]=1
    for val in sockpairs.values():
        pairCount+=(int)(val/2)
    return pairCount

arr=[1,2,1,2,1,3,2]
sockMerchant(1,arr)

