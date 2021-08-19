from sys import stdin

duck = list(stdin.readline().strip())


min_num = 0
q = 'quack'
end = 0
quack = []
cnt = 0
ducks = 1
for i in duck:
    if i == 'q':
        quack.append([])
for i in duck:
    if i == 'q'  :
        end += 1
        if end > min_num:
            min_num = end
    if i == 'k':
        end -= 1
    put = 0
    for j in range(len(quack)):
        #print(, j, i, quack)
        if len(quack[j]) != 5:
            if i == q[len(quack[j])]:
                quack[j].append(i)
                put = 1
                break
    if not put:
        res = 0
        put = 0
        break


for i in quack:
    if len(i) != 5:
        res = 0
        break
    res = 1

if len(duck) % 5:
    res = 0
if res and put:
    print(min_num)
else:
    print(-1)


