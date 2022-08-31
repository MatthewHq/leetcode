def jumpingOnClouds(c):
    # Write your code here
    i=0
    counter=0
    while i<len(c)-3:
        counter+=1
        if c[i+2]==1:
            i+=1
        else:
            i+=2
    return counter+1

            
        



# c=[0,1,0,0,0,1,0]
c=[0,1,0,0,0,0,1,0,0]
c=[0,1,0,0,0,0,0,0,1,0]
c=[0,1,0,0,0,0,1,0,0]
# c=[0,1,0,0,0,1,0]
# c=[0,0,0,1,0,0]
print(jumpingOnClouds(c))

#00
#01
#10