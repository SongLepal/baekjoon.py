from sys import stdin
from collections import deque

ox = [ -1, -1, -1,  0,  1,  0]
oy = [ -1,  0,  1,  1,  0, -1]

ex = [  0, -1,  0,  1,  1,  1]
ey = [ -1,  0,  1,  1,  0, -1]

def next(x, y, i):
    if y % 2 == 0:
        nx = x + ex[i]
        ny = y + ey[i]
    elif y % 2 == 1:
        nx = x + ox[i]
        ny = y + oy[i]
    return nx, ny

def bfs_wall():
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(6):
            nx, ny = next(x, y, i)
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                cnt += 1
                continue
            if arr[nx][ny] == -1:
                cnt += 1
                #continue
    return cnt

def bfs_find():
    while q:
        x, y = q.popleft()
        for i in range(6):
            nx, ny = next(x, y, i)
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if arr[nx][ny] == 0:
                arr[nx][ny] = -1
                q.append((nx, ny))
                #continue

n, m = map(int, stdin.readline().split())
_input = []

q = deque()

for _ in range(m):
    _input.append(list(map(int, stdin.readline().split(' '))))
arr = list(map(list, zip(*_input)))

for i in range(n):
    for j in range(m):
        if (i == 0 or j == 0 or (i + 1) == n or (j + 1) == m) and arr[i][j] == 0:
            arr[i][j] = -1
            q.append((i, j))

bfs_find()

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i, j))

print(bfs_wall())

