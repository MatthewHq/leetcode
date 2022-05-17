#dang, i had to look at the solution for this after HOURS smh


def abbreviation(a, b):
    # Write your code here
    dp = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    dp[0][0]=1

    for i in range(len(a)):
        for j in range(len(b)+1):
            if dp[i][j]:
                if j<len(b) and a[i].upper()==b[j]:
                    dp[i+1][j+1]=1
                if a[i].islower():
                    dp[i+1][j]=1
    for row in dp:
        print(row)
    if dp[len(a)][len(b)]:
        return 'YES'
    else:
        return 'NO'
    

a="dAbC"
b="ABC"
# a='ababbaAbAB' 
# b='AABABB' #false

# a='aAbAb' 
# b='ABAB' #true

# a='baaBa' 
# b='BAAA' #false

# a='abAAb' 
# b='AAA' #true

# a='babaABbbAb' 
# b='ABAA' #false


# a = "beFgH"
# b = "EFG"

print(abbreviation(a, b))