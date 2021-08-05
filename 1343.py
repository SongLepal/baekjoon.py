from sys import stdin

string = stdin.readline().strip()
poly = []
cnt = 0
can = 1
for i in range(len(string)):
    if string[i] == 'X':
        cnt += 1
    elif string[i] == '.':
        for _ in range(cnt // 4):
            poly.append('AAAA')
        cnt %= 4
        for _ in range(cnt // 2):
            poly.append('BB')
        cnt %= 2
        if cnt % 2:
            can = 0
            break
        poly.append('.')
        cnt = 0

for _ in range(cnt // 4):
    poly.append('AAAA')
cnt %= 4

for _ in range(cnt // 2):
    poly.append('BB')
cnt %= 2

if cnt % 2:
    can = 0

if can:
    for i in range(len(poly)):
        print(poly[i], end = '')   
else:
    print(-1)
