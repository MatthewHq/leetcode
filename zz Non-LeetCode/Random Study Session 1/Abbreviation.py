def abbreviation(a, b):
    # Write your code here
    dp = []
    letterCountB = {}
    letterCheckA={}

    currRow = []

    # for i in range(len(b)):
    for c in b:
        if letterCheckA.get(c) == None:
            letterCheckA[c] = 1
        if letterCountB.get(c) == None:
            letterCountB[c] = 1
        else:
            letterCountB[c] += 1
    print(letterCheckA,"AAAA")

    for i in range(len(a)):
        c = a[i]
        # print(i,currRow)
        if c == (b[0].lower()):  # a is lowerCase
            if i == 0:
                currRow.append(1)
            else:
                currRow.append(max(currRow[i-1], 1))
        elif c == b[0]:  # a is uppercase
            if c in letterCountB.keys():
                letterCountB[c] -= 1
                if letterCountB[c] == -1:
                    print('NO')
                    return 'NO'
            if i == 0 or currRow[i-1] < 2:
                currRow.append(2)
            else:
                currRow.append(0)
        elif c.isupper():
            currRow.append(0)
        elif i != 0 and currRow[i-1] >= 1:
            currRow.append(currRow[i-1])
        else:
            currRow.append(0)
    letterCheckA.pop(b[0])

    dp.append(currRow)

    for i in range(1, len(b)):
        toMatch = b[i]
        currRow = []
        countOnes = True
        if letterCountB[b[i-1]] == 0:
            countOnes = False
        for j in range(len(a)):
            c = a[j]
            if c == toMatch.lower() and dp[i-1][j-1]:
                if i == 0:
                    currRow.append(1)
                else:
                    if countOnes:
                        currRow.append(max(currRow[j-1], 1))
                    elif dp[i-1][j-1] == 2:
                        currRow.append(1)
                    else:
                        if currRow[j-1] == 2:
                            currRow.append(2)
                        else:
                            currRow.append(0)

            elif c == toMatch and dp[i-1][j-1]:
                if c in letterCountB.keys():
                    print(letterCountB)
                    if toMatch in letterCheckA.keys():
                        letterCountB[c] -= 1
                        if letterCountB[c] == -1:
                            print('NO')
                            return 'NO'
                if j == 0 or currRow[j-1] < 2:
                    currRow.append(2)
                else:
                    currRow.append(0)
            elif c.isupper():
                currRow.append(0)
            elif j != 0 and currRow[j-1] >= 1:
                currRow.append(currRow[j-1])
                # if i==len(b)-1:
                # flag=True
            else:
                currRow.append(0)
            print("===",letterCheckA)
        if toMatch in letterCheckA.keys():
            letterCheckA.pop(toMatch)
        print("POPPED",toMatch,letterCheckA)
        dp.append(currRow)

    print(b)
    print(a)
    print(letterCountB)
    for row in dp:
        print(row)

    if dp[len(b)-1][len(a)-1]:
        print('YES')
        return 'YES'
    else:
        print('NO')
        return 'NO'

a = 'ebeffeefggee'
b = 'EFGE'

# a = 'EbefFeefgGeE'
# b = 'EFGE'

# a = 'beFgEefg'
# b = 'EFGE'


abbreviation(a, b)
