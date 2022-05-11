

from multiprocessing.dummy import current_process


def minimumBribes(q):
    # Write your code here
    swapCount=0
    bribeCount = {}
    # sortedArr=sorted(q)
    currPos = [None for x in range(len(q))]
    for i in range(len(q)):
        currPos[q[i]-1] = i
    for i in range(len(q)):
        ind = currPos[i]
        # print(i)
        # print("index",ind)
        # print(q)
        while ind > i:
            a = q[ind]
            b = q[ind-1]
            # print(q)
            if b in bribeCount.keys():
                bribeCount[b] += 1
                # print(5,bribeCount[b])
                if bribeCount[b] == 3:
                    print('Too chaotic')
                    return
            else:
                bribeCount[b] = 1

            currPos[q[ind-1]-1] = ind

            q[ind] = b
            q[ind-1] = a
            # print(q)
            # print("=============")
            ind -= 1
            swapCount+=1
    # print(q)
    # print(bribeCount)

    print(swapCount)



q = [2, 5, 1, 3, 4]
q=[1, 2, 5, 3, 7, 8, 6, 4]
minimumBribes(q)
