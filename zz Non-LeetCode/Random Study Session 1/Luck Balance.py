


def luckBalance(k, contests):
    # Write your code here
    contests.sort(key=lambda x:x[0])
    contests.reverse()
    print(contests)


    luck=0
    for contest in contests:
        if contest[1]==0:
            luck+=contest[0]
        elif contest[1]==1:
            if k>0:
                luck+=contest[0]
                k-=1    
            else:
                luck-=contest[0]
    return luck

k=500
contests = [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]
print(luckBalance(k,contests))