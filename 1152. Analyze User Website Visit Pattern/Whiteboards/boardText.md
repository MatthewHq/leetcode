# Notes

## **we will begin with the assumption that timestamp is always in order, it only makes sense**

<br>

- Pattern is a list of 3 websites
- score: **NUMBER OF USERS**


## Edge Cases
- [ ] Timestamps are out of order?
- [ ] Visiting patter can count nonconsecutive visits ie
  - [a,b,c,d] produces [a,b,c] and [a,c,d] and [a,b,d]

## Approach

For each username there will be a unique queue of size 3 properties of FIFO.

As each entry is processed, a **hashmap** will be used to retain the pattern scores, however the high scorer will be updated during each entry process iteration
  - The hashmap will comprise of <Pattern : SET() of users>

- Highscore: will be kept in a list that can contain multiple entries



Building round robin username structure


