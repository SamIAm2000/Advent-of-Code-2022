import re
file = open('input.txt')
var = file.read().splitlines()
biglist=[]
for i in range(len(var)):
    biglist.append([int(x) for x in re.findall(r'-?\d+', var[i])])

#function to merge overalpping intervals
def mergeIntervals(intervals):
    intervals.sort()
    stack = []
    stack.append(intervals[0])
    for i in intervals[1:]:
        if stack[-1][0] <= i[0] <= stack[-1][-1]:
            stack[-1][-1] = max(stack[-1][-1], i[-1])
        else:
            stack.append(i)
    return stack

rangelist = []
cleanRangeList = []
finalrow = 0
x = 0
for row in range(0,4000001):
    for i in range(len(biglist)):
        sx = biglist[i][0]
        sy = biglist[i][1]
        bx = biglist[i][2]
        by = biglist[i][3]
        dist = abs(sx-bx) +abs(sy-by)

        xmin = sx-(dist -abs(sy-row))
        xmax = sx + (dist -abs(sy-row))
        rangelist.append([xmin,xmax])
    rangelist = mergeIntervals(rangelist)
    for i in range(len(rangelist)):
        if rangelist[i][0]<0:
            rangelist[i][0]=0
        if rangelist[i][1]>4000000:
            rangelist[i][1]=4000000
        if rangelist[i][0] > 4000000 or rangelist[i][1] > 4000000:
            break
        cleanRangeList.append(rangelist[i])        
    if len(cleanRangeList) > 1:
        finalrow = row
        break
    cleanRangeList=[]
    rangelist = []

x = cleanRangeList[0][1]+1
print(x)
print(finalrow)
print(x*4000000+finalrow)

