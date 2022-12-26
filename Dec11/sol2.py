import re
file = open('input.txt')
var = file.read().splitlines()

biglist= []
emptylist = []
for i in range(8):
    emptylist.append([])
newlist = emptylist
m =[0,0,0,0,0,0,0,0]

for i in range(len(var)):
    if i %7 == 1:
        biglist.append([int(x) for x in re.findall(r'\d+', var[i])])
# print(biglist)
def monk0(x):
    if x % 13 ==0:
        return 1
    else: 
        return 7
def monk1(x):
    if x % 2 ==0:
        return 7
    else: 
        return 5
def monk2(x):
    if x % 7 ==0:
        return 3
    else: 
        return 4
def monk3(x):
    if x % 17 ==0:
        return 4
    else: 
        return 6
def monk4(x):
    if x % 5 ==0:
        return 6
    else: 
        return 0
def monk5(x):
    if x % 11 ==0:
        return 2
    else: 
        return 3
def monk6(x):
    if x % 3 ==0:
        return 1
    else: 
        return 0
def monk7(x):
    if x % 19 ==0:
        return 2
    else: 
        return 5

bignum = 13*2*7*17*5*11*3*19

print(biglist)
for q in range(10000):
    for i in range(len(biglist)):
        while len(biglist[i]) != 0:
            item = biglist[i].pop(0)
            if i ==0:
                item = (item*3)%bignum
                x = monk0(item)
                m[0]+=1
            elif i ==1:
                item = (item+8)%bignum
                x = monk1(item)
                m[1]+=1
            elif i ==2:
                item = (item*item)%bignum
                x = monk2(item)
                m[2]+=1
            elif i ==3:
                item = (2+item)%bignum
                x = monk3(item)
                m[3]+=1
            elif i ==4:
                item = (3+item)%bignum
                x = monk4(item)
                m[4]+=1
            elif i ==5:
                item = (17*item)%bignum
                x = monk5(item)
                m[5]+=1
            elif i ==6:
                item = (6+item)%bignum
                x = monk6(item)
                m[6]+=1
            elif i ==7:
                item = (1+item)%bignum
                x = monk7(item)
                m[7]+=1
            biglist[x].append(item)


# print("length of big list:", len(biglist))
# 14398560027 too low
print(m)
m.sort()
print(m)
print(m[7]*m[6])

