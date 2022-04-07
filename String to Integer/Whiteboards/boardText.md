There are couple features to be implemented that I will organize / discuss

    1. "Read in and ignore any leading whitespace." 
        "Do not ignore any characters other than the leading whitespace or the rest of the string after the digits."

        - Will have a loop implementation checking for whitespaces
        - Then will fall into another FOR loop checking for integers. 
            I say for loop because a 32-bit integer can only hold so many digits
                Given a large string with 100k integer characters would be an edge case that can be avoided with this for loop
    
    2. Check for '+' or '-' or neither for data regarding positive or negative
        This will be handled as a flag and loop checks on character feed
            - Flag 1 will assume there is no sign interpreted, if there is, it will be true if negative, false if positive
            - Checks for these sign indicators will be implemented at the end of the whitespace while loop or may vary depending on a few things
                - Integer interpretation implementation
                - Rules on input such as "     ++++--++1231231" etc
    3. "Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored."
        - Regarding the END of a string, cases such as  "....123123" and "...123124 awidifn awd wad" will be considered
        - Probably baked into a for loop situation going the length of the input

    4. Convert Digits to integer
        -Have't thought of how I'm going to implement this one in terms of registering each integer
            - might look at ascii character values 0-9, I am hesitatnt to use "toString" for for each individual character, feels like i'd be making a hammer "from scratch" with a hammer
                - after testing it looks like ascii implemnentation per character will be very easy
                - 0-9 is 48-57 so just a simple shift will work
    5.  "If no digits were read, then the integer is 0. Change the sign as necessary"
        - as the initial for loop checking to filter out ALL digits occurs, each character will be popped into a list, if the list is empty, the returned value will be 0


    6. "Clamping" integers out of 32bit range
        - there is no mention of larger integers being able to be held by the assumed system so I will not be very harsh in coding this part besides a character limit mentioned above and a final comparison to the MAX_VAL
            - If there is a problem with it not being an accepted answer, then I will implement a check on the value as a left-truncated item along with a check on the truncated particle
                - Consider the range of a 32-bit integer [-2147483648 , 2147483647]
                    - given "2147483648" (max possible + 1) we can truncate from left side as we build 2147483648 --> 2 | 147483648
                        - check if 147483648 > 147483647 and checking if that left particle is "2" , making the check 32-bit friendly



After submission looks like I misunderstood that THERE CAN ONLY BE whitespace at the start, no words, if there are words it should default to 0

It also appears that there can only be ONCE sign specifier, else default to 0

Running into so many edge cases, continued to add solution modifcations

Another edge case of having a decimal input as a string

another edge case: "00000-42a1234"