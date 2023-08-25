# Approach Brainstorm

- Adding up every combo of 2 with indexing data and comparing against a hashmap
  - O(n^2)

- Can either hashmap the calculations with its 2 indices or the negative of `nums` with one index, so we will go with the latter as it will be more mem efficient
  - this is weak when `nums` has almost all of the same number, where the other option would be weaker when most combinations of 2 `nums` entries adds up to the same number, which is more unlikely and therefore could increase performance? Perhaps not because of the way it would not iterate an extra O(n) over ALL the cases, just a few...unless 0s. `Note[1]`
    - In the case of 0s I could suspect an O(n^3) edge case, this means the ORDER is not being covered in my approach is what I am realizing right now.

  - if the first performs badly, i will perhaps do the other

- Notice in `Note[1]` that order can be addressed by checking the case of nums being `[0,0,0,0]` where we can see our first case of [0,1,2] being repeated later on as `[0,2,1]` which we can then solve by only checking indices that are larger on the next rounds. So not a comparison of `!=` but more of `>`
  - Additionally we don't consider the last combination of calculations because at that point they have been considered.