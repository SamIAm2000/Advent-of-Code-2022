from collections import OrderedDict
import string

file = open('input.txt')
var = file.read().splitlines()

list1 = []
list2 = []
list3 = []
for i in range(len(var)):
    count = len(var[i])//2
    list1.append(var[i][:count])
    list2.append(var[i][count:])

for j in range(len(list1)):
    tempList =[]
    for k in list1[j]:
        if k in list2[j]:
            tempList.append(k)
    list3.append(tempList)

list5=[]
for m in range(len(list3)):
    list5.append(list3[m][0])

list4=[]
alphaValueDict = OrderedDict.fromkeys(string.ascii_letters,range(0))
i = 1
for k,v in alphaValueDict.items():
    alphaValueDict[k] = [i]
    i += 1

for l in range(len(list5)):
    list4.append(alphaValueDict[list5[l]][0])

print(sum(list4))
