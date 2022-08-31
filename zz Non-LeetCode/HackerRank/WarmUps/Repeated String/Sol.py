def repeatedString(s, n):
    # Write your code here
    steps = []
    for i in range(len(s)):
        if s[i] == 'a':
            steps.append(i)
    print(steps,len(steps))

    div = (int)(n/len(s))
    mod = n % len(s)-1
    print(div, mod)

    x = 0
    maxed=mod==-1
    while not maxed and steps[x]<= mod:
        x += 1 
        if x>=len(steps):
            maxed=True
    print("x",x)



    # print(steps)
    return len(steps)*div+(x)
    # 111122223


s = 'a'
s = 'a'
n = 4

print(repeatedString(s, n))
