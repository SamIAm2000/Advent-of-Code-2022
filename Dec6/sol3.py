from collections import Counter

file = open('input2.txt')
var = file.read().splitlines()

lst=[]
most_common = ""
least_common = ""
for i in range(8):
    for j in range(len(var)):
        lst.append(var[j][i])
    counter = Counter(lst)
    most_common += counter.most_common(1)[0][0]
    least_common += counter.most_common()[-1][0]

    lst=[]
print(most_common)
print(least_common)
