file = open('input.txt')
var = file.read().splitlines()
headX=0
headY=0
tailX=0
tailY=0

n_set = set()
n_set.add((0,0))
def sign(i):
    if i > 0:
        return 1
    elif i < 0:
        return -1
    else:
        return 0

for str in var:
    if str[0] == 'R':
        x = int(str[2:])
        s = 1
    elif str[0] == 'L':
        x = int(str[2:])
        s = -1
    elif str[0] == 'U': 
        y = int(str[2:])
        s = 1
    elif str[0] == 'D':
        y = int(str[2:])
        s = -1
    
    if x != 0:
        for i in range(x):
            headX +=s
            difX = headX - tailX 
            difY = headY - tailY
            if abs(difX) > 1 or abs(difY) >1:
                tailX +=s
                tailY +=sign(difY)
                n_set.add((tailX,tailY))
            elif abs(difX) >1:
                tailX += s
                n_set.add((tailX,tailY))
    else:
        for i in range(y):
            headY +=s
            difX = headX - tailX 
            difY = headY - tailY
            print(difX,difY)
            if abs(difX) > 1 or abs(difY) >1:
                tailX +=sign(difX)
                tailY += s
                print((tailX,tailY))
                n_set.add((tailX,tailY))
            elif abs(difY) >1:
                tailY += s
                n_set.add((tailX,tailY))
    x=y=0

print(len(n_set))
    



