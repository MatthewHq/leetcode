def candies(n,arr):
    back=[1]
    front=[1]

    candyCount=[]

    for i in range(1,len(arr)):
        if arr[i-1]<arr[i]:
            front.append(front[i-1]+1)
        else:
            front.append(1)

    for i in reversed(range(1,len(arr))):
        if arr[i]<arr[i-1]:
            back.append(back[len(arr)-i-1]+1)
        else:
            back.append(1)
        
    back.reverse()
    for i in range(len(arr)):
        candyCount.append(max(back[i],front[i]))
    
    print("arr",arr)
    print("bak",back)
    print("frt",front)
    print("can",candyCount)
    return sum(candyCount)
    

arr = [1, 2, 3, 4, 4, 4, 4, 3, 2, 3, 3, 5, 5, 5, 1, 2, 3, 4, 1] #37
arr = [4,6,4,5,6,2] #10
arr=[1,2,2] #4
arr=[2,4,2,6,1,7,8,9,2,1] #19
print(candies(0,arr))
        