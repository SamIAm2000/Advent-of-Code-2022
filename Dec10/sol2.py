file = open('input.txt')
var = file.read().splitlines()
cycle=0
bigX=1
mylist = []

for str in var:
    if str == "noop":
        cycle += 1
        mylist.append(bigX)
        # print(bigX)
    elif str[:4] == "addx":
        x = int(str[5:])
        mylist.append(bigX)
        # print(bigX)
        mylist.append(bigX)
        # print(bigX)
        bigX+=x

total = 0
for i in [20,60,100,140,180,220]:
    # print(mylist[i])
    total += i*mylist[i-1]
print(total)

for i in range(len(mylist)):
    x=(i) % 40
    if x ==0:
        print("\n",end = '')
    if x in range(mylist[i]-1,mylist[i]+2):
        print("#",end = '')
    else:
        print('.',end = '')