from sys import stdin

n = int(stdin.readline().strip())
num = list(map(int, stdin.readline().split()))

result = [-1 for _ in range(n)]
stack = []

for i in range(n):
    while stack and num[stack[len(stack)-1]] < num[i]:
        result[stack.pop()] = num[i]
    stack.append(i)

for i in result:
    print(i, end = ' ')
