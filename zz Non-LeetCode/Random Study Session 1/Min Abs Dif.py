def minimumAbsoluteDifference(arr):
    # Write your code here
    arr.sort()
    diff=abs(arr[0]-arr[1])
    for i in range(2,len(arr)):
        if diff>abs(arr[i]-arr[i-1]):
            diff=abs(arr[i]-arr[i-1])
    return diff
