from sys import stdin
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if arr[nx][ny] == -1:
                continue
            if arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx, ny))

n, m = map(int, stdin.readline().split())
arr = []
q = deque()

for _ in range(m):
    arr.append(list(map(int, stdin.readline().split(' '))))

for i in range(m):
    for j in range(n):
        if arr[i][j] == 1:
            q.append((i, j))
bfs()
no = 0
result = -99
for i in arr:
    for j in i:
        if j == 0:
            no = 1
            break
        result = max(result, j)
if no:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result - 1)
