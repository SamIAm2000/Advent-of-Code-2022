from collections import OrderedDict
import string

file = open('input.txt')
var = file.read().splitlines()

list1 = []
list2 = []
for i in range(len(var)//3):
    templist=[]
    i=3*i
    for n in var[i]:
        if n in var[i+1] and n in var[i+2]:
            templist.append(n)
    
    list1.append(templist)

for m in range(len(list1)):
    list2.append(list1[m][0])

list3=[]
alphaValueDict = OrderedDict.fromkeys(string.ascii_letters,range(0))
i = 1

for k,v in alphaValueDict.items():
    alphaValueDict[k] = [i]
    i += 1

for l in range(len(list2)):
    list3.append(alphaValueDict[list2[l]][0])

print(sum(list3))
