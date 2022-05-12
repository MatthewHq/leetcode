def maximumToys(prices, k):
    # Write your code here
    currSum=0
    toyCount=0
    prices.sort()
    for i in range(len(prices)):
        newPrice=currSum+prices[i]
        if newPrice<k:
            currSum=newPrice
            toyCount+=1
        else:
            return toyCount
        
    return toyCount

k=50
prices=[1, 12, 5, 111, 200, 1000, 10]

print(maximumToys(prices,k))