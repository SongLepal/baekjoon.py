from sys import stdin

n = int(stdin.readline().strip())
num = list(map(int, stdin.readline().split()))

result = [-1 for _ in range(n)]
stack = []
cnt = dict()
for i in num:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in range(n):
    while stack and cnt[num[stack[len(stack)-1]]] < cnt[num[i]]:
        result[stack.pop()] = num[i]
    stack.append(i)

for i in result:
    print(i, end = ' ')
