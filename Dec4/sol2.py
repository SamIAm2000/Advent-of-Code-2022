file = open('input.txt')
var = file.read().splitlines()
count=0
for i in var:
    i=i.replace('-', ',')
    list=i.split(',')
    list2 = [eval(j) for j in list]
    print(list2)
    if (list2[0]>=list2[2] and list2[0]<=list2[3]) or (list2[1]>=list2[2] and list2[0]<=list2[3]):
        count +=1
print(count)