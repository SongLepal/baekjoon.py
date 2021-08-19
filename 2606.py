from sys import stdin

def dfs(start, graph):
    for i in graph[start]:
        if i not in visited:
            visited.append(i)
            dfs(i, graph)

node = int(stdin.readline().strip())
n = int(stdin.readline().strip())
graph = {}
for i in range(node):
    graph[i+1] = set()
for i in range(n):
    a, b = map(int, stdin.readline().split())
    graph[a].add(b)
    graph[b].add(a)
    
visited = []
dfs(1, graph)
print(len(visited) - 1)
