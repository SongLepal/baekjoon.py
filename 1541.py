from sys import stdin

string = stdin.readline().split('-')

total = 0
for i in string[0].split('+'):
    total += int(i)

for i in string[1:]:
    for j in i.split('+'):
        total -= int(j)
        
print(total)
        
