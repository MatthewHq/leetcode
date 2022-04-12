# Initial Thoughts
Looking at this problem the first thing that came into my mind as I was reading it was recursion since we are dealing with a file system but then I finished reading it and figured since all the files are given to me in an array I don't particulary have to go looking for them myself, they are already organized for me.

So basically we aren't looking for the files at all, we are lookign AT them.

Another thing that might be advantageous is that fact that these are given in array format and string. The string part is a bit of a whatever kind of but the important one is the array and then the combination of these
- that is because as these file paths and contents are traveresed we can store specific checkpoints regarding where things are with ease and call to them with O(1), so I might be able to take advantage of that

**one key thing here i'm going to avoid is the more advanced string functions, in particular i'm thinking avoiding something like find(',') and actually iterating through the string myself.** 


## As for sorting and comparing:
In order to do it efficiently at least, I'm thinking initial comparisons will best be done based on content LENGTH / SIZE whatever you want to call it.

IF and only IF these lenghts match, then we will want to compare the contents
- The comparison of the contents can be very different in many ways depending on the type of data being stored, if it was formatted data there could be specific locations to look for differences that would be as easy as O(1) though here we have to assume completely RANDOM data where each position matters ie contents can be "abcDeF" and "abcFeD" where we can't get away with tricks of comparing a specific position or segment.


Some ideas are nested linkedlists of same-sized files to be compared and elimited
An interesting one would be a hashing function though with randomized data again it can probably only be used as a filtering method, could be good though.



