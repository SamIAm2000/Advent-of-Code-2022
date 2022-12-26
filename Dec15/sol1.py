import re
file = open('input.txt')
var = file.read().splitlines()

biglist=[]
row = 2000000
for i in range(len(var)):
    biglist.append([int(x) for x in re.findall(r'-?\d+', var[i])])
print(biglist)
maxX=0
minX=0
for x in range(len(biglist)):
    if biglist[x][0] > maxX:
        maxX = biglist[x][0]
    if biglist[x][0] < minX:
        minX = biglist[x][0]
for x in range(len(biglist)):
    if biglist[x][2] > maxX:
        maxX = biglist[x][2]
    if biglist[x][2] < minX:
        minX = biglist[x][2]
print(maxX, minX)

noblst=[0]*(maxX-minX+1000000)
for i in range(len(biglist)):
    sx = biglist[i][0]
    sy = biglist[i][1]
    bx = biglist[i][2]
    by = biglist[i][3]
    dist = abs(sx-bx) +abs(sy-by)
    for x in range(minX-500000,maxX+500000):
        if (abs(sx-x) + abs(row-sy)) <= dist and (x != bx or by != row):
            noblst[x] = 1

print(sum(noblst))






