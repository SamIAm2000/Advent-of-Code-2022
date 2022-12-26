import re
file = open('test.txt')
var = file.read().splitlines()

biglist= []
emptylist = []
for i in range(4):
    emptylist.append([])
newlist = emptylist
m =[0,0,0,0,]

for i in range(len(var)):
    if i %7 == 1:
        biglist.append([int(x) for x in re.findall(r'\d+', var[i])])
print(biglist)
def monk0(x):
    if x % 23 ==0:
        return 2
    else: 
        return 3
def monk1(x):
    if x % 19 ==0:
        return 2
    else: 
        return 0
def monk2(x):
    if x % 13 ==0:
        return 1
    else: 
        return 3
def monk3(x):
    if x % 17 ==0:
        return 0
    else: 
        return 1


for q in range(20):
    for i in range(len(biglist)):
        while len(biglist[i]) != 0:
            item = biglist[i].pop(0)
            if i ==0:
                item = 19*item//3
                x = monk0(item)
                m[0]+=1
            elif i ==1:
                item = (item+6)//3
                x = monk1(item)
                m[1]+=1
            elif i ==2:
                item = item*item//3
                x = monk2(item)
                # print(item)
                # print(x)
                m[2]+=1
            elif i ==3:
                item = (3+item)//3
                x = monk3(item)
                # print(item)
                # print(x)
                m[3]+=1
            biglist[x].append(item)

print(biglist)
print("length of big list:", len(biglist))
print(m)
m.sort()
print(m)
print(m[3]*m[2])

