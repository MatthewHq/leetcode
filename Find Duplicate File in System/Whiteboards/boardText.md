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



So now picking this problem back up lets organize some of the things that I want to do in order to approach this problem

- Deciding on a structure to organize my data as I parse through it.
    - I need to organize my data with it being centric to the text files and their content
    - I need to be able to easily **reference** parent directory path for when I finally print out the whole paths
      - I don't want to attach the same path to all the files as per constraint: <br>
        `` <= paths[i].length <= 3000 ``
        - this is slight overkill optimization and covering some weird edge cases where the path is insanely deep to where it takes most of the 3000 alloted chars lol, I might skip it
        - I ended up planning it for now, I will have an array of indices of each parent corresponding to each grouped input. This will save some space as I already have the initial data in the input. This is also possible because: <br>
          ``You may assume each given directory info represents a unique directory. `` 
    - I also need to **group** by content size in order to make my comparisons efficient
      - For this I am thinking along the lines of json or a multilevel structure.
      - **this part im very excited about my implementation:**<br>
        ``dictionary``<br>	``Key: int size``<br>
        ``Value: int double array[[parentID,namestart,nameEnd,contentStart,contentEnd]]``<br>
        The reason we can do this is because we can reference the original string input in subtring form, though it is very important we don't actually use substring() and instead use ``string[lowerIndex:UpperIndex]`` because of runtime + space reasons
    

    Now that I have my structure all I need to do is:

    1. Go through each string by iterating through each character and sort them into their respective sizes in the dictionary. 
    2. Once all datapoints are collected, we go through ONLY the size sets that have more than one entry in the value double array<br>
       - potential for messing around with hashing but I don't know if I'll add that filter really  
    3. If they match add them to a similar "output" structure consisting of the same things that is just processed at the end, **with most of the space still in the actual input!!!**