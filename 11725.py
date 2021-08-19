from sys import stdin
from collections import deque

def bfs():
    que = deque()
    que.append(1)
    while que:
        v = que.popleft()
        for i in graph[v]:
            if parent[i] == 0:
                parent[i] = v
                que.append(i)
    return parent

n = int(stdin.readline().strip())
graph = [ [] for _ in range(n+1) ]
parent = [0] * (n+1)

for _ in range(n-1):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

bfs()
for i in parent[2:]:
    print(i)
