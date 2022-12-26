file = open('input.txt')
var = file.read()
lst=[]
for i in range(13, len(var)):
    for j in range(14):
        lst.append(var[i-j])
    if len(set(lst)) == 14:
        print(lst)
        break
    lst=[]
print(i+1)