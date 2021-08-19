from sys import stdin
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    que = deque()
    que.append((x, y))
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if arr[nx][ny] == 0:
                continue
            if arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] + 1
                que.append((nx, ny))
    return arr[n-1][m-1]

n, m = map(int, stdin.readline().split())
arr = []

for _ in range(n):
    arr.append(list(map(int, stdin.readline().strip())))
print(bfs(0, 0))
