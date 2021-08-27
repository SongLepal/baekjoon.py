from sys import stdin
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find():
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 'O':
                q.append((i, j))

def put():
    for i in range(r):
        for j in range(c):
            if arr[i][j] != 'O':
                  arr[i][j] = 'O'

def bomb():
    while q:
        x, y = q.popleft()
        arr[x][y] = '.'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if arr[nx][ny] == 'O':
                arr[nx][ny] = '.'
                
arr = []
r, c, n = map(int, stdin.readline().split(' '))
q = deque()

for _ in range(r):
    arr.append(list(stdin.readline().strip()))
n -= 1

for i in range(n):
    if i % 2 == 0:
        find()
        put()
    else:
        bomb()

for i in range(r):
    for j in range(c):
        print(arr[i][j], end = '')
    print()
