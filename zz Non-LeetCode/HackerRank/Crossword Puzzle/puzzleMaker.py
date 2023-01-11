f = open("puzzle.txt", "r")

puzzle="\""

line=f.readline()
while line!="":
    puzzle+=line.strip()+"\"+\"\\n\"+\""
    line=f.readline()
    # print(line)

puzzle=puzzle[0:len(puzzle)-7]
print(puzzle)

f.close()
f = open("puzzle.txt", "r")
line=f.readline().strip()
while line!="":
    newLine=""
    for c in line:
        newLine+=c
        newLine+="#"
    print(newLine)
    line=f.readline().strip()
    