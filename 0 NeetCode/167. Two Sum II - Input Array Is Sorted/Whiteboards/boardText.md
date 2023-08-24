
Initially thinking two pointers that will move from out to in and we will use smallest as anchor. Thus the biggest number will have to go left until it reaches a possibility
    1. After the right pointer reaches said location, if it is smaller than the number, it will be the new anchor and the left pointer will now move in. 
        - the way the pointers move in might be best with binary search? Though on some edge cases it will be marginally slower than moving sequentially one at a time
        - for sake of not going too crazy we will move one at a time and see how that goes


## Looking at this constraint *2 <= numbers.length <= 3 * 10^4* 
We can see that it might be VERY beneficial to do binary search

Perhaps I will dive into implementing binary search or leetcode might force me anyway by telling me it took to long to do the easier sequential moving