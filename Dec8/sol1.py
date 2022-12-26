import numpy as np

file = open('test.txt')
var = file.read().splitlines()
var2=[]
for x in var:
    var2.append(list(x))

var2 = np.array(var2)

count =0
a=b=c=d=[]
b=[]
c=[]
d=[]
for i in range(1,len(var2)-1):
    for j in range(1,len(var2[0])-1):
        for x in np.where(var2[i,:] >= var2[i,j])[0]:
            if x < j:
                a.append(var2[i,x])
        for y in np.where(var2[:,j] >= var2[i,j])[0]:
            if y < i:
                b.append(var2[y,j])
        for z in np.where(var2[i,:] >= var2[i,j])[0]:
            if z > j:
                c.append(var2[y,j])
        for w in np.where(var2[:,j] >= var2[i,j])[0]:
            if w > i:
                d.append(var2[y,j])
        if  not a or not b or not c or not d:
            count +=1
        a=[]
        b=[]
        c=[]
        d=[]

count =count + len(var2)*2 + len(var2[0])*2 -4
print(len(var2)*2 + len(var2[0])*2 -4)
print(count)

