# Initial Thoughts

Honestly right off the bat this seems like a VERY straightforward question, almost feels like it should be an easy, which makes me then think that it might be harder than usual if I can't see any complications yet AHH!

So first thought is an O(n) solution where I just go and subtract each element from its previous and have a counter running...

Assuming the subsequence definition from what I can tell is CONTINUOUS arithmetic differences, otherwise we can just throw a hashmap at it



``Recall that a subsequence of an array nums is a list nums[i1], nums[i2], ..., nums[ik] with 0 <= i1 < i2 < ... < ik <= nums.length - 1``



Ok this part was a little ambiguous with how ``nums[i1], nums[i2], ..., nums[ik] `` kinda implies they are CONTINUOUS but looking at an example 

``` 
Example 2:
Input: nums = [9,4,7,2,10]
Output: 3
Explanation: 
The longest arithmetic subsequence is [4,7,10].
```

Shows that it doesn't have to be continuous so we are going to throw a hasmap in there.



Ok I now understand the complication once I understood the subsequence did not have to be immediately continuous


Now we know the bruteforce method is checking each possible difference, I'm wondering if theres a dynamic programming solution to this and a small inkling that there could be a recursive one or combo of them both, we shall see

Now I'm thinking best I can do is O(n^2) with a sort of dynamic programming approach except I use a hashmap to hit repeat values

# Implementation Stage

Looks like the O(n^2) DP method worked for the most part except I failed in considering that two occurences of the same difference can happened in an "intertwined manner which doesn't count as a sequence so I have to protect against that counting in.


After messing around in excel looks like for the incrementer to count upward, there needs to be a specific level of stepping that is valid which is either 2 down or two right at LEAST. 
- Now I also realize there is another edge case to consider where two patterns of the same value are fighting for the top, how to detect against those, sometimes a value might have more than one pattern
    - Dove into this particular edge case and it opened up a ton of them that need to be handled, visualized it out on excel but sitting on solution considerations for a bit here.

I am thinking of two approaches that might need to be combined or might be exclusive.
1. One of the biggest properties is that once I know ONE difference, i can cache it's next awaited solution and see if I spot it in the future and cache the next one as i incremet etc 

2. With the excel visualization I can save the coordinates of each difference when the difference is the same and track its lineage, it will have a feeling of a linkedlist of sorts.

Looks like I'm going with the first approach combined with a hashmap because each anticipated number can be looked up this way and the "lineage" of a specific sequence can be caught in this manner without much else