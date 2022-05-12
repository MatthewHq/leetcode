def countSwaps(a):
    swapCount=0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                swapCount+=1
                aPoint = a[j]
                bPoint = a[j+1]
                a[j] = bPoint
                a[j+1] = aPoint

    print("Array is sorted in {} swaps.".format(swapCount))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[len(a)-1]))
    


a = [6, 4, 1]

countSwaps(a)
