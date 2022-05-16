from sympy import checkodesol


def abbreviation(a, b):
    # Write your code here
    dp = []
    letterCountB = {}
    capsOnly = []

    currRow = []

    for c in b:  # populating letterCountB
        # c=b[]
        if letterCountB.get(c) == None:
            letterCountB[c] = 1
        else:
            letterCountB[c] += 1

    for c in a:  # counting through letterCountB to check diag matches and impossibilities
        if c.isupper():
            if c in letterCountB.keys():
                letterCountB[c] -= 1
                if letterCountB[c] == -1:
                    print('NO')
                    return 'NO'
                elif letterCountB[c] == 0:
                    capsOnly.append(c)
            else:
                print('NO')
                return 'NO'

    for i in range(len(b)):  # populating dyn prog double array
        match = b[i]
        # print(i,"==================",i,match)
        caps = b[i] in capsOnly
        row = []
        for j in range(len(a)):  # going to fill up individual rows
            c = a[j]
            if j != 0 and row[j-1] == 1:
                row.append(1)
            else:
                # print(c,"===",c)
                if c.isupper():  # a is upper case
                    if c == match:  # a == b and UPPER case
                        # either first row or anything past 2nd col with diag match
                        if i == 0 or (j != 0 and dp[i-1][j-1]):
                            row.append(1)
                        else:  # can be combined down maybe
                            row.append(0)
                    else:
                        row.append(0)
                else:  # a is lower case
                    # print(i,j,c,match,caps)
                    if c == match.lower() and not caps:  # a == b and lower case
                        # either first row or anything past 2nd col with diag match
                        if i == 0 or (j != 0 and dp[i-1][j-1]):
                            row.append(1)  # copy prior unless first col
                        else:
                            row.append(0)
                    else:
                        row.append(0)
        dp.append(row)

    # ===================
    print(b)
    print(a)
    print(letterCountB)
    print(capsOnly)
    for i in range(len(dp)):
        print(b[i], dp[i])

    if dp[len(b)-1][len(a)-1]:
        print('YES')
        return 'YES'
    else:
        print('NO')
        return 'NO'


# =======================================
# a = 'ebeffeefggee'
# b = 'EFGE'

# a = 'EbefFeefgGeE'
# b = 'EFGE'

# a = 'beFgEefg'
# b = 'EFGE'

# a="EqefFxefeqqgEGeQFq"
# b="EFEQEGQFQ"

a='ababbaAbAB' 
b='AABABB' #false

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
