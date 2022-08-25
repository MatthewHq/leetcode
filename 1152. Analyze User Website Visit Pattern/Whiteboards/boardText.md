# Notes

- Pattern is a list of 3 websites
- score: **NUMBER OF USERS**


## Edge Cases
- [ ] Timestamps are out of order?
- [ ] 
## Approach

For each username there will be a unique queue of size 3 properties of FIFO.

As each entry is processed, a **hashmap** will be used to retain the pattern scores, however the high scorer will be updated during each entry process iteration
  - The hashmap will comprise of <Pattern : [List of Users]>

- Highscore: will be kept in a list that can contain multiple entries
