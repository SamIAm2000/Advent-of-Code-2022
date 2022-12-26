import numpy as np

file = open('input.txt')
var = file.read().splitlines()
var2=[]
for x in var:
    var2.append(list(x))

var2 = np.array(var2)

count =[]
a=b=c=d=1
for i in range(1,len(var2)-1):
    for j in range(1,len(var2[0])-1):
        a = j
        b = i
        c = len(var2[0])-1 -j
        d = len(var2)-1 -i
        for x in np.where(var2[i,:] >= var2[i,j])[0]:
            if x < j:
                a =j-x
        for y in np.where(var2[:,j] >= var2[i,j])[0]:
            if y < i:
                b = i-y
        for z in np.where(var2[i,:] >= var2[i,j])[0]:
            if z > j:
                c = z-j
                break
        for w in np.where(var2[:,j] >= var2[i,j])[0]:
            if w > i:
                d=w-i
                break
        count.append(a*b*c*d)
        a=b=c=d=1

print(max(count))

