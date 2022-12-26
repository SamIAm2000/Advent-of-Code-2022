import re
file = open('test.txt')
var = file.read().splitlines()

biglist=[]
row = 10
for i in range(len(var)):
    biglist.append([int(x) for x in re.findall(r'-?\d+', var[i])])

#function to merge overlapping intervals
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
for i in range(len(biglist)):
    sx = biglist[i][0]
    sy = biglist[i][1]
    bx = biglist[i][2]
    by = biglist[i][3]
    dist = abs(sx-bx) +abs(sy-by)

    xmin = sx-(dist -abs(sy-row))
    xmax = sx + (dist -abs(sy-row))
    rangelist.append([xmin,xmax])

print("original rangedlist:", rangelist)

rangelist = mergeIntervals(rangelist)
print("merged rangedlist:",rangelist)
count = 0
for i in range(len(rangelist)):
    count +=rangelist[i][1]-rangelist[i][0]
print(count)

