from sys import stdin
from collections import deque

def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if arr[x][y] == 1:
        arr[x][y] = 0
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        result[cnt] += 1
        return True
    return False

n = int(stdin.readline().strip())
arr = []
cnt = 0
result = [0]
for _ in range(n):
    arr.append(list(map(int, stdin.readline().strip())))
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            cnt += 1
            result.append(0)
            
print(cnt)
result.sort()
for i in range(1, cnt+1):
    print(result[i])
