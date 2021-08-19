from sys import stdin
from collections import deque

def bfs(com):
    check = [0] * n
    que = deque()
    que.append(com)
    check[com] = 1
    cnt = 1
    while que:
        v = que.popleft()
        for i in graph[v]:
            if check[i] == 0:
                cnt += 1
                check[i] = 1
                que.append(i)
    return cnt
    
n, m = map(int, stdin.readline().split())

graph = [ [] for _ in range(n) ]

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[b-1].append(a-1)

result = []
for i in range(n):
    result.append(bfs(i))
for i in range(n):
    if result[i] == max(result):
        print(i+1, end = ' ')
