#     [P]                 [Q]     [T]
# [F] [N]             [P] [L]     [M]
# [H] [T] [H]         [M] [H]     [Z]
# [M] [C] [P]     [Q] [R] [C]     [J]
# [T] [J] [M] [F] [L] [G] [R]     [Q]
# [V] [G] [D] [V] [G] [D] [N] [W] [L]
# [L] [Q] [S] [B] [H] [B] [M] [L] [D]
# [D] [H] [R] [L] [N] [W] [G] [C] [R]
#  1   2   3   4   5   6   7   8   9 

file = open('input.txt')
var = file.read().splitlines()

stack = [['F','H','M','T','V','L','D'],['P','N','T','C','J','G','Q','H'],['H','P','M','D','S','R',],['F','V','B','L'],['Q','L','G','H','N'],['P','M','R','G','D','B','W'],['Q','L','H','C','R','N','M','G'],['W','L','C'],['T','M','Z','J','Q','L','D','R']]
for i in stack:
    i.reverse()

def move(a,b,c):
    for i in range(a):
        stack[c-1].append(stack[b-1].pop())

for str in var:
    lst =str.split()
    a = int(lst[1])
    b = int(lst[3])
    c = int(lst[5])
    move(a,b,c)

result = ""
for k in stack:
    result += k.pop()
print(result)