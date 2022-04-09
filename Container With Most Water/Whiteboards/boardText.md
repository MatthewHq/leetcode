## Initial Thoughts

Intstantly I think about the bruteforce method probably being O(n^2) and wondering if O(n) is possible, where n is the number of bars

Wondering if O(n) can be achieved, going to mess around in excel
Looks like there is a way to do it in (n*n-1)/2


Notice on pdn and excel sheet working with Figure 3 on pdn and excel has pdn calculations of fig 3 in tab "2"
- Each corresponding square calculates how much water is being held in order to decide what to delete
  - notice the yellow is the initial cleaner
  - the green is where we start to delete

- Small issue with figure 3 where we would have to have O(n*h) where h is the highest height if that approach was taken, so moving on to figure 4


Figure 4:
- As i contemplate figure 4 I notice this problem will take a bit longer than expected if I were to fully dive deep into it, I am going to summarize what I WOULD do if I absolutely had to find the most optimal solution but I will not implement my plan, instead I will move on to looking at solution hints


## Approach findings prior to solution peek:

**Thought process was sort of "simulating" water where we take out the tallest bars that have the least significance as we dwelve down and try and maximize our water containment potential whilst reducing it by removing the tallest bars**

Bit of redundance in that satement but hey these are just my thoughts

Figure 3 shows that we would NEED to know the NEXT tallest bar, we could sort the heights which would take us to nlog(n) or maybe do a binary search on height as we go down each time which might take us to nlog(h) where h is max height
- havem't completely contemplated those runtimes but if it came between anything that replaced n with h, h would probably more desirable as constraints listed on this problem show h having a smaller cap, assuming even & ramdomm distribution of input


## Post Peek
GG I could have just done 2 pointer approach, had a bit more contemplation

What happens when TWO pointer's heights are the same
- Need to think it through a little more, thinking comparing the heights of each of their next ones, but what happens if those next ones are the same etc.

pausing for now

contemplating the same height bar issue a little but not alot, going to just go for it and assume there isn't a problem with picking either of the two first


A bit dissapointed I didn't take a little longer to contemplate the initial solution being two pointers, the only hint I got from peeking was skimming through the titles in discussion and getting the word "two pointers"