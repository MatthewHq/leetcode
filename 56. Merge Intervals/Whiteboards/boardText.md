# Notes

# Edge Cases
- Ranges with exact overlaps ie: 
  - [1,3] [3,4] - End = Start
  - [1,3] [1,5] - Start = Start
  - [1,3] [2,3] - End = End

---

## Approach 1
Can be done with sorted list
- would need some sort of tag for start numbers and end numbers 
  

### Runtime
- initial sort will be (nlogn)
- 