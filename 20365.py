from sys import stdin

n = int(stdin.readline().strip())

string = list(stdin.readline().strip())
string.append(' ')
cnt = [1, 1]
for i in range(n):
    if string[i] == 'R':
        cnt[0] += 1
        if string[i+1] == 'R':
            cnt[0] -= 1
    if string[i] == 'B':
        cnt[1] += 1
        if string[i+1] == 'B':
            cnt[1] -= 1
print(min(cnt))
