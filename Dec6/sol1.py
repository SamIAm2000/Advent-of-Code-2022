file = open('input.txt')
var = file.read()

for i in range(3, len(var)-3):
    set = {var[i-3],var[i-2],var[i-1],var[i]}
    if len(set) == 4:
        break

print(i+1)
